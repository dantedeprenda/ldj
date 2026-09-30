"""X4: how to split a budget of B human labels between fitting a method and certifying it.

For every budget B, fit share f and resample r:

1. Draw B labels uniformly from the train pool (per category when ``per_category``). The
   first round(f * B) fit the method; the rest are a random certification sample. The same
   draw is shared by every method and every f (nested fit sets), so comparisons are paired.
2. Score the unlabeled rest of the train pool, the certification sample and the test split.
3. Build the threshold grid from the *unlabeled rest* only, certify on the certification
   sample (``ldj.certify``), and score the chosen threshold on the test split.

f = 0 exists only for zero-shot scorers (``needs_labels = False``); learned methods get f > 0.
The heuristic arm reuses all B labels: fit on them, pick the loosest grid threshold whose
cross-fitted empirical risk (or recall) meets the target, and score it the same way. It
carries no guarantee and is there to show how often it breaks.

Policies (``policy.kind``):

- ``accept``: automate items with p >= lambda, wrong when y = 0 (routing: the cheap model).
- ``classify``: automate items with |p - cut| >= lambda as ``p >= cut``; wrong when that
  disagrees with y (moderation).
- ``recall``: auto-reject items with p < t; certified per category (screening reviews).

The test split is used only to score. Violations are judged on test-set risk, a noisy proxy
for the population risk: with a small test split the realized violation rate overstates it.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, replace
from typing import Any

import numpy as np
import pandas as pd

from ldj import certify
from ldj.cost import recall_threshold
from ldj.methods.base import Method
from ldj.run import cross_fit
from ldj.task import Task

_log = logging.getLogger(__name__)

REJECT_SHARES = np.round(np.arange(0.01, 1.0, 0.01), 2)  # recall grid: share auto-rejected


def single_annotator_labels(task: Task) -> Task:
    """The task with train-pool labels replaced by one real annotator's call (the reviewer
    behind ``human_correct``: their label is y where they were right, 1 - y where not). Test
    labels stay the consensus, so certificates built on one annotator are judged against it
    (X7, exploratory). Needs realized 0/1 ``human_correct``, as T1 has."""
    hc = task.human_correct
    if not np.isin(hc, (0.0, 1.0)).all():
        raise ValueError(f"{task.name}: human_correct is a rate, not one annotator's calls")
    y = task.y.copy()
    train = np.asarray(task.train)
    y[train] = np.where(hc[train] == 1, y[train], 1 - y[train])
    return replace(task, y=y)


@dataclass(frozen=True)
class Policy:
    kind: str  # accept | classify | recall
    alpha: float | None = None  # selective-risk target (accept, classify)
    target: float = 0.95  # recall target (recall)
    delta: float = 0.05
    cut: float = 0.5  # classify: decision cut on p
    selection: str = "fixed_sequence"  # or bonferroni

    def __post_init__(self) -> None:
        if self.kind not in ("accept", "classify", "recall"):
            raise ValueError(f"unknown policy kind {self.kind!r}")
        if self.kind != "recall" and self.alpha is None:
            raise ValueError("set policy.alpha: the risk target is fixed before the run")

    def conf_loss(self, p: np.ndarray, y: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
        if self.kind == "accept":
            return p, 1.0 - y
        return np.abs(p - self.cut), ((p >= self.cut) != (y == 1)).astype(float)


def _grid(policy: Policy, p_rest: np.ndarray, n_cert: int) -> np.ndarray:
    """Thresholds from the unlabeled rest of the pool; order as ``ldj.certify`` expects."""
    if policy.kind == "recall":
        s = np.sort(p_rest)
        return s[np.minimum(np.ceil(REJECT_SHARES * len(s)).astype(int), len(s) - 1)]
    conf, _ = policy.conf_loss(p_rest, np.zeros(len(p_rest)))
    cov = certify.coverage_grid(n_cert, policy.alpha, policy.delta)
    return certify.pool_thresholds(conf, cov)


def _outcome(policy: Policy, p, y, threshold: float) -> dict:
    """Test-split outcome of a threshold: share automated, realized risk or recall."""
    if policy.kind == "recall":
        o = certify.recall_outcome(p, y, threshold, policy.target)
        return {"automated": o["work_saved"], "realized": o["recall"], "violated": o["violated"]}
    conf, loss = policy.conf_loss(p, y)
    o = certify.risk_outcome(conf, loss, threshold, policy.alpha)
    return {"automated": o["coverage"], "realized": o["risk"], "violated": o["violated"]}


def certified_threshold(policy: Policy, p_rest, p_cert, y_cert) -> float:
    grid = _grid(policy, p_rest, len(p_cert))
    if policy.kind == "recall":
        cert = certify.certify_recall(
            p_cert, y_cert, grid, policy.target, policy.delta, policy.selection
        )
    else:
        conf, loss = policy.conf_loss(p_cert, y_cert)
        cert = certify.certify_risk(conf, loss, grid, policy.alpha, policy.delta, policy.selection)
    return cert.threshold


def heuristic_threshold(policy: Policy, task: Task, lab, p_lab, p_rest) -> float:
    """Loosest threshold whose empirical (cross-fitted) risk or recall on the B labels meets
    the target. ``p_lab`` None (too few of an outcome to cross-fit) automates nothing."""
    if p_lab is None:
        return float("nan")
    if policy.kind == "recall":
        t_lo, _ = recall_threshold(task, lab, p_lab, policy.target, rule="empirical")
        # recall_threshold rejects p <= t_lo; recall_outcome rejects p < threshold
        return float(np.nextafter(t_lo, np.inf)) if np.isfinite(t_lo) else float("nan")
    grid = _grid(policy, p_rest, len(lab))
    conf, loss = policy.conf_loss(p_lab, task.y[lab])
    best = float("nan")
    for t in grid:
        acc = conf >= t
        if acc.any() and loss[acc].mean() <= policy.alpha:
            best = float(t)  # grid runs strict to loose, so the last pass is the loosest
    return best


class _Frozen:
    """An answerer whose matrix is read once for every item of a task, so refitting a head
    500 times does not re-enter the LLM client (or its thread pool)."""

    def __init__(self, orig, task: Task):
        self.orig, self.task_name = orig, task.name
        self.x, _ = orig.matrix(task, np.arange(task.n))
        self.failed = set(np.flatnonzero(np.isnan(self.x).any(axis=1)).tolist())

    def matrix(self, task, idx):
        if task.name != self.task_name:
            raise RuntimeError(f"frozen for {self.task_name}, asked for {task.name}")
        return self.x[idx], np.zeros(len(idx))


class _FrozenJudge:
    """A zero-shot judge whose scores are read once for every item of a task (used inside
    features + judge, which would otherwise re-query the judge on every refit)."""

    def __init__(self, orig, task: Task):
        self.orig, self.task_name, self.name = orig, task.name, orig.name
        self.p = np.asarray(
            orig.fit(task, np.array([], dtype=int)).predict(task, np.arange(task.n))
        )
        self.failed = set(getattr(orig, "failed", ()))

    def fit(self, task, lab):
        return self

    def predict(self, task, idx):
        if task.name != self.task_name:
            raise RuntimeError(f"frozen for {self.task_name}, asked for {task.name}")
        self.cost_ = np.zeros(len(idx))
        return self.p[idx]


def _freeze(method: Method, task: Task) -> Method:
    """Freeze a question method's answers (and a features + judge method's judge scores) for
    ``task``; re-freezes for each new sub-task."""
    judge = getattr(method, "judge", None)
    if judge is not None:
        if isinstance(judge, _FrozenJudge):
            if judge.task_name != task.name:
                method.judge = _FrozenJudge(judge.orig, task)
        else:
            method.judge = _FrozenJudge(judge, task)
    ans = getattr(method, "answerer", None)
    if ans is None:
        return method
    if isinstance(ans, _Frozen):
        if ans.task_name == task.name:
            return method
        ans = ans.orig
    method.answerer = _Frozen(ans, task)
    if method.answerer.failed:
        _log.warning("%s: %d items without answers", task.name, len(method.answerer.failed))
    return method


def run_group(
    task: Task,
    methods: list[Method],
    policy: Policy,
    budgets: list[int],
    fit_shares: list[float],
    reps: int,
    seed: int = 0,
    group: int = 0,
    min_rest: int = 100,
    heuristic: bool = True,
    volume: float | None = None,
    rep_ids: list[int] | None = None,
    cache: dict | None = None,
) -> list[dict]:
    """Per-resample rows for one task (or one category's sub-task). ``rep_ids`` runs only those
    resamples (each is seeded by (seed, group, B, rep), so any split of the work gives the same
    rows); ``cache`` keeps zero-shot scores across calls in one worker."""
    pool, test = np.asarray(task.train), np.asarray(task.test)
    yt = task.y[test]
    volume = float(volume or len(test))
    everything = np.arange(task.n)
    fixed: dict[str, np.ndarray] = {}
    for m in methods:
        if not m.needs_labels:
            key = (task.name, m.name)
            if cache is not None and key in cache:
                fixed[m.name] = cache[key]
                continue
            fixed[m.name] = np.asarray(m.fit(task, pool[:0]).predict(task, everything), float)
            if cache is not None:
                cache[key] = fixed[m.name]
        else:
            _freeze(m, task)
    rows: list[dict] = []
    for b in budgets:
        if b + min_rest > len(pool):
            _log.info("%s: B=%d leaves < %d unlabeled pool items; skipped", task.name, b, min_rest)
            continue
        for r in rep_ids if rep_ids is not None else range(reps):
            perm = np.random.default_rng([seed, group, b, r]).permutation(pool)
            lab, rest = perm[:b], perm[b:]
            for m in methods:
                base = {"group": task.name, "method": m.name, "B": b, "rep": r}
                zero_shot = m.name in fixed
                shares = [0.0] if zero_shot else [f for f in fit_shares if f > 0]
                for f in shares:
                    n_fit = 0 if zero_shot else min(max(round(f * b), 1), b - 1)
                    fit, cert = lab[:n_fit], lab[n_fit:]
                    if zero_shot:
                        s = fixed[m.name]
                    else:
                        s = np.full(task.n, np.nan)
                        need = np.concatenate([rest, cert, test])
                        s[need] = m.fit(task, fit).predict(task, need)
                    t = certified_threshold(policy, s[rest], s[cert], task.y[cert])
                    rows.append(
                        {
                            **base,
                            "arm": "certified",
                            "f": f,
                            "n_fit": n_fit,
                            "n_cert": len(cert),
                            "cert_pos": int(task.y[cert].sum()),
                            "certified": bool(np.isfinite(t)),
                            "threshold": t,
                            **_outcome(policy, s[test], yt, t),
                        }
                    )
                if heuristic:
                    if zero_shot:
                        s, p_lab = fixed[m.name], fixed[m.name][lab]
                    else:
                        p_lab = cross_fit(m, task, lab)
                        s = np.full(task.n, np.nan)
                        need = np.concatenate([rest, test])
                        s[need] = m.fit(task, lab).predict(task, need)
                    t = heuristic_threshold(policy, task, lab, p_lab, s[rest])
                    rows.append(
                        {
                            **base,
                            "arm": "heuristic",
                            "f": 1.0,
                            "n_fit": b,
                            "n_cert": 0,
                            "cert_pos": 0,
                            "certified": bool(np.isfinite(t)),
                            "threshold": t,
                            **_outcome(policy, s[test], yt, t),
                        }
                    )
    for row in rows:
        row["auto_per_label"] = row["automated"] * volume / row["B"]
    return rows


def run(task: Task, methods: list[Method], cfg: dict[str, Any]) -> pd.DataFrame:
    """All groups of a config; ``cfg`` holds policy, budgets, fit_shares, reps and so on."""
    policy = Policy(**cfg["policy"])
    groups = (
        [task.subset(c) for c in np.unique(task.categories)] if cfg.get("per_category") else [task]
    )
    rows: list[dict] = []
    for gi, sub in enumerate(groups):
        rows += run_group(
            sub,
            methods,
            policy,
            budgets=list(cfg["budgets"]),
            fit_shares=list(cfg["fit_shares"]),
            reps=int(cfg["reps"]),
            seed=int(cfg.get("seed", 0)),
            group=gi,
            min_rest=int(cfg.get("min_rest", 100)),
            heuristic=bool(cfg.get("heuristic", True)),
            volume=cfg.get("volume"),
        )
    return pd.DataFrame(rows)


def summarize(rows: pd.DataFrame, delta: float = 0.05) -> pd.DataFrame:
    """One line per (method, arm, f, B), pooled over groups and resamples.

    - ``useful``: share of resamples whose certificate automates something on test. A threshold
      that automates nothing (the recall grid's first step) is trivially certified; not counted.
    - ``automated`` (mean) and ``auto_p10/p50/p90``: automation across resamples. The mean mixes
      draws that certify with draws that don't; the percentiles show the spread.
    - ``violation``: the unconditional violation rate (a resample that certifies nothing cannot
      violate; the guarantee is about this rate), with a two-sided 95% Clopper-Pearson interval
      ``violation_lo/hi``. ``violation_if_useful`` is the rate among useful certificates, a
      diagnostic, not the guarantee.
    - ``consistent``: ``violation_lo <= delta``, i.e. the resamples do not show the (1 - delta)
      guarantee failing. It is not a proof that it holds. Violations are judged on test-set risk,
      a noisy proxy for population risk, and pooled groups (T2 reviews) are not independent units.
    """
    rows = rows.assign(useful=rows["certified"] & (rows["automated"] > 0))
    g = rows.groupby(["method", "arm", "f", "B"], sort=True)
    out = g.agg(
        n=("rep", "size"),
        useful=("useful", "mean"),
        automated=("automated", "mean"),
        auto_p10=("automated", lambda a: a.quantile(0.10)),
        auto_p50=("automated", "median"),
        auto_p90=("automated", lambda a: a.quantile(0.90)),
        auto_per_label=("auto_per_label", "mean"),
        violations=("violated", "sum"),
    ).reset_index()
    useful_viol = rows[rows["useful"]].groupby(["method", "arm", "f", "B"])["violated"].mean()
    out = out.merge(
        useful_viol.rename("violation_if_useful").reset_index(),
        on=["method", "arm", "f", "B"],
        how="left",
    )
    k, n = out["violations"].to_numpy(float), out["n"].to_numpy(float)
    out["violation"] = k / n
    out["violation_lo"] = certify.cp_lower(k, n, 0.025)
    out["violation_hi"] = certify.cp_upper(k, n, 0.025)
    out["consistent"] = out["violation_lo"] <= delta
    return out.drop(columns="violations")


def b_star(summary: pd.DataFrame) -> tuple[pd.DataFrame, int | None]:
    """Per B, the certified arm (method, f) automating the most among ``consistent`` cells, and
    the smallest B where that best arm spends labels on fitting (f > 0). None: never. A B where
    no arm automates anything has no best arm (every arm ties at zero), so it is left out.

    Descriptive only: the best arm is picked after seeing test automation, so it is a frontier,
    not a deployable choice. A recommended rule must be frozen on development data."""
    cert = summary[
        (summary["arm"] == "certified") & summary["consistent"] & (summary["automated"] > 0)
    ]
    if cert.empty:
        return cert, None
    best = cert.loc[cert.groupby("B")["automated"].idxmax()].sort_values("B")
    fitted = best[best["f"] > 0]
    return best, (int(fitted["B"].iloc[0]) if len(fitted) else None)


def markdown(summary: pd.DataFrame, best: pd.DataFrame, bstar: int | None) -> str:
    head = ["method", "arm", "f", "B", "n", "useful", "automated (mean)", "p10 / p50 / p90"]
    head += ["violation [95% CI]", "violation if useful", "consistent"]
    lines = [
        "# X4 allocation frontier (exploratory)",
        "",
        (
            "`useful`: share of resamples whose certificate automates something. `violation`: "
            "the unconditional rate the guarantee is about, with a Clopper-Pearson interval; "
            "`violation if useful` is a diagnostic. `consistent`: the interval's lower end is "
            "<= delta (the data do not show the guarantee failing; not a proof)."
        ),
        "",
        "| " + " | ".join(head) + " |",
        "|" + "---|" * len(head),
    ]
    for _, r in summary.iterrows():
        vu = r["violation_if_useful"]
        lines.append(
            f"| {r['method']} | {r['arm']} | {r['f']:.2f} | {r['B']} | {r['n']} | "
            f"{r['useful']:.3f} | {r['automated']:.3f} | {r['auto_p10']:.3f} / "
            f"{r['auto_p50']:.3f} / {r['auto_p90']:.3f} | {r['violation']:.3f} "
            f"[{r['violation_lo']:.3f}, {r['violation_hi']:.3f}] | "
            f"{'-' if pd.isna(vu) else f'{vu:.3f}'} | {r['consistent']} |"
        )
    lines += [
        "",
        "## Best certified arm per B (descriptive: picked after seeing test results)",
        "",
    ]
    for _, r in best.iterrows():
        lines.append(f"- B = {r['B']}: {r['method']} at f = {r['f']:.2f}, {r['automated']:.3f}")
    lines += ["", f"B* (smallest B where the best arm fits, f > 0): {bstar}"]
    return "\n".join(lines) + "\n"
