"""ldj run <config.yaml> | ldj bridge <paired.csv> | ldj audit <predictions.csv> |
ldj reproduce --fixture <name> | ldj split <events.csv> --time COL"""

from __future__ import annotations

import argparse
import logging
import os
from pathlib import Path

import yaml

from ldj.run import run


def load_dotenv(path: str = ".env") -> None:
    """KEY=value lines into the environment (existing variables win). Values are never printed."""
    p = Path(path)
    if not p.exists():
        return
    for line in p.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip().strip("\"'"))


def main() -> int:
    load_dotenv()
    logging.basicConfig(level=logging.WARNING, format="%(asctime)s %(name)s %(message)s")
    ap = argparse.ArgumentParser(prog="ldj")
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("run", help="run a config")
    r.add_argument("config")
    r.add_argument("--out", default="results")
    b = sub.add_parser("bridge", help="value of escalation from a paired-outcome CSV")
    b.add_argument("csv")
    b.add_argument("--score", action="append", default=[], help="score column (repeatable)")
    b.add_argument("--rates", default="0.1,0.2,0.3,0.5", help="escalation rates, comma-separated")
    b.add_argument("--md", help="also write the report to this file")
    b.add_argument("--html", help="also write a self-contained HTML report")
    b.add_argument("--json", help="also write the result as JSON")
    a = sub.add_parser("audit", help="certify one fixed system from a random audit sample")
    a.add_argument("csv", help="columns: score, role (audit|deploy), label (audit rows)")
    a.add_argument("--kind", choices=["accept", "classify", "recall"], required=True)
    a.add_argument("--alpha", type=float, help="risk target (accept, classify)")
    a.add_argument("--target", type=float, default=0.95, help="recall target (recall)")
    a.add_argument("--delta", type=float, default=0.05)
    a.add_argument("--cut", type=float, default=0.5, help="classify: decision cut on the score")
    a.add_argument("--md", help="also write the report to this file")
    a.add_argument("--json", help="also write the result as JSON")
    a.add_argument("--html", help="also write a self-contained HTML report")
    rp = sub.add_parser("reproduce", help="replay a packaged result offline")
    rp.add_argument("--fixture", default="moderation-v1", help="name or path of a fixture")
    rp.add_argument("--out", help="output folder (default results/reproduce/<name>)")
    sp = sub.add_parser("split", help="chronological, grouped dev/eval split with an audit cohort")
    sp.add_argument("csv")
    sp.add_argument("--time", required=True, help="event time column")
    sp.add_argument("--group", help="group column (order, shipment) kept within one period")
    sp.add_argument("--dev-until", help="boundary date; default: --dev-share of groups by start")
    sp.add_argument("--dev-share", type=float, default=0.6)
    sp.add_argument(
        "--cohort-share", type=float, default=0.2, help="random audit share of eval groups/rows"
    )
    sp.add_argument(
        "--cohort-unit", choices=["group", "row"], default="group", help="sampling unit"
    )
    sp.add_argument(
        "--one-per-group", action="store_true", help="one random audit row per cohort group"
    )
    sp.add_argument("--seed", type=int, default=0)
    sp.add_argument("--spanning", choices=["later", "drop"], default="later")
    sp.add_argument("--decision-time", help="with --available-at: flag information after decision")
    sp.add_argument("--available-at")
    sp.add_argument("--out", required=True, help="output CSV")
    rc = sub.add_parser("recommend", help="the frozen default rule for a task and label budget")
    rc.add_argument("--task", choices=["classify", "accept", "recall"], required=True)
    rc.add_argument("--budget", type=int, required=True, help="human labels available (B)")
    rc.add_argument("--alpha", type=float, default=0.10, help="error target (classify, accept)")
    rc.add_argument("--delta", type=float, default=0.05)
    rc.add_argument("--target", type=float, default=0.95, help="recall target (recall)")
    rc.add_argument("--prevalence", type=float, help="share of relevant items (recall)")
    rc.add_argument(
        "--label-source", choices=["consensus", "single", "majority"], default="consensus"
    )
    rc.add_argument("--json", action="store_true", help="print JSON instead of text")
    args = ap.parse_args()
    if args.cmd == "recommend":
        import json

        from ldj.recommend import recommend, text

        r = recommend(
            args.task,
            args.budget,
            args.alpha,
            args.delta,
            args.prevalence,
            args.label_source,
            args.target,
        )
        print(json.dumps(r, indent=1) if args.json else text(r))
        return 0
    if args.cmd == "split":
        import json

        import pandas as pd

        from ldj.split import split

        try:
            out, rep = split(
                pd.read_csv(args.csv),
                args.time,
                args.group,
                dev_until=args.dev_until,
                dev_share=args.dev_share,
                cohort_share=args.cohort_share,
                seed=args.seed,
                spanning=args.spanning,
                decision_time=args.decision_time,
                available_at=args.available_at,
                cohort_unit=args.cohort_unit,
                one_per_group=args.one_per_group,
            )
        except ValueError as e:
            raise SystemExit(f"{args.csv}: {e}") from e
        out.to_csv(args.out, index=False)
        print(json.dumps(rep, indent=1))
        return 0
    if args.cmd == "reproduce":
        from ldj.reproduce import reproduce

        return 0 if reproduce(args.fixture, args.out) else 1
    if args.cmd == "run":
        run(yaml.safe_load(Path(args.config).read_text()), args.out)
    elif args.cmd == "bridge":
        from ldj.bridge import report_csv

        rates = [float(x) for x in args.rates.split(",")]
        text = report_csv(args.csv, args.score, rates)
        print(text)
        if args.md:
            Path(args.md).write_text(text)
        if args.html or args.json:
            import json

            from ldj.report import bridge_html, bridge_result

            res = bridge_result(args.csv, args.score, rates)
            if args.html:
                Path(args.html).write_text(bridge_html(res))
            if args.json:
                Path(args.json).write_text(json.dumps(res, indent=1, default=float))
    elif args.cmd == "audit":
        import json

        import pandas as pd

        from ldj.allocate import Policy
        from ldj.audit import audit, markdown

        df = pd.read_csv(args.csv)
        missing = {"score", "role", "label"} - set(df.columns)
        if missing:
            raise SystemExit(f"{args.csv}: missing columns {sorted(missing)}")
        bad = set(df["role"]) - {"audit", "deploy"}
        if bad:
            raise SystemExit(f"{args.csv}: unknown roles {sorted(bad)}; use audit or deploy")
        au, de = df[df["role"] == "audit"], df[df["role"] == "deploy"]
        if au["label"].isna().any():
            raise SystemExit(f"{args.csv}: every audit row needs a 0/1 label")
        policy = Policy(
            args.kind, alpha=args.alpha, target=args.target, delta=args.delta, cut=args.cut
        )
        result = audit(au["score"], au["label"], de["score"], policy)
        text = markdown(result)
        print(text)
        if args.md:
            Path(args.md).write_text(text)
        if args.json:
            Path(args.json).write_text(json.dumps(result, indent=1, default=float))
        if args.html:
            from ldj.report import audit_html

            Path(args.html).write_text(audit_html(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
