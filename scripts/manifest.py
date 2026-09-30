"""Evidence manifest: what every data and result file is, where it came from, its
licence, whether it may be redistributed, and its SHA-256.

    uv run python scripts/manifest.py

Writes release/manifest.json and release/MANIFEST.md (committed; the files themselves stay local
under the gitignored data/ and results/). Re-run after any result changes; a changed hash means a
changed file. Licence notes were checked on the date in LICENCES below; re-check at release.
"""

from __future__ import annotations

import datetime
import hashlib
import json
import subprocess
from fnmatch import fnmatch
from pathlib import Path

# (pattern, role, source, licence key, redistributable)
RULES = [
    (
        "data/t0/*.npz",
        "T0 input: routing tasks, per-model correctness/cost, Jev answers",
        "jev-routing-paper export",
        "t0",
        "no (contains raw Jev answers)",
    ),
    (
        "data/t1/measuring-hate-speech.parquet",
        "T1 input: comments and annotations",
        "ucberkeley-dlab/measuring-hate-speech",
        "mhs",
        "yes, with attribution",
    ),
    (
        "data/t2/*",
        "T2 input: SYNERGY records (build cache)",
        "SYNERGY+ v3.0 via OpenAlex",
        "synergy",
        "no (abstracts)",
    ),
    (
        "data/audit/*_claude.csv",
        "Audit: Claude's proposed labels",
        "this project",
        "mixed",
        "no (T1 texts offensive; T2 abstracts)",
    ),
    (
        "data/audit/*.csv",
        "Audit: author-checked labels with item texts",
        "this project",
        "mixed",
        "no (T2 abstracts); labels and ids only",
    ),
    ("results/audit_*.json", "Audit agreement and disagreeing ids", "this project", "code", "yes"),
    (
        "results/t1/*",
        "T1 pre-registered run outputs",
        "this project",
        "t1_out",
        "yes (predictions, incl. Gemma judge probabilities)",
    ),
    (
        "results/t2/*",
        "T2 pre-registered run outputs",
        "this project",
        "t2_out",
        "yes (scores and ids only; no abstracts)",
    ),
    (
        "results/t*_repro_h1/*",
        "Reproduction checks (fresh process)",
        "this project",
        "t_out",
        "yes",
    ),
    (
        "results/t0_reproduce/*",
        "T0 reproduction of the routing paper",
        "this project",
        "t0_out",
        "check (predictions from Jev features)",
    ),
    ("results/x1_*/*", "X1 exploratory outputs", "this project", "t_out", "yes"),
    (
        "results/x4_*/*",
        "X4 exploratory allocation rows and summaries",
        "this project",
        "t_out",
        "yes",
    ),
    ("results/bridge_t0/*", "W1 E-bridge reports", "this project", "t0_out", "yes (derived)"),
    ("results/ledger_*", "W3 whole-workflow ledger", "this project", "t_out", "yes"),
    ("results/t*_smoke/*", "Smoke tests (not results)", "this project", "t_out", "not needed"),
]

LICENCES = {
    "checked": "2026-09-30",
    "code": "Apache-2.0 (this repository)",
    "mhs": "CC-BY-4.0 (Measuring Hate Speech corpus); attribute Kennedy et al. 2020",
    "synergy": "SYNERGY labels CC0; abstracts come from OpenAlex/publishers and are not "
    "redistributed: ship ids + a rebuild script + derived features",
    "t0": "LLMRouterBench MIT; routing paper code MIT; Jev answers under TypeSafe's MCA, not "
    "published (derived metrics only)",
    "t1_out": "Apache-2.0 for our code's outputs; Gemma outputs: Google claims no rights in "
    "outputs and they are not model derivatives (Gemma Terms of Use, last modified 2026-04-01); "
    "use stays subject to Gemma's prohibited-use policy; provider (OpenRouter) terms: re-check "
    "at release",
    "t2_out": "as t1_out; no SYNERGY abstracts inside",
    "t_out": "as t1_out",
    "t0_out": "derived from Jev features and public benchmark outcomes; publish derived metrics "
    "only unless TypeSafe agrees otherwise",
    "mixed": "item texts keep their source licence (MHS CC-BY-4.0; SYNERGY abstracts not "
    "redistributable)",
}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    rows = []
    for path in sorted(p for d in ("data", "results") for p in Path(d).rglob("*") if p.is_file()):
        if path.name == ".DS_Store" or ".cache" in path.parts:
            continue
        rule = next((r for r in RULES if fnmatch(str(path), r[0])), None)
        role, source, lic, redist = rule[1:] if rule else ("UNCLASSIFIED", "?", "?", "check")
        rows.append(
            {
                "path": str(path),
                "bytes": path.stat().st_size,
                "sha256": sha256(path),
                "role": role,
                "source": source,
                "licence": lic,
                "redistributable": redist,
            }
        )
    commit = subprocess.run(
        ["git", "rev-parse", "--short", "HEAD"], capture_output=True, text=True, check=False
    ).stdout.strip()
    out = Path("release")
    out.mkdir(exist_ok=True)
    manifest = {
        "generated": datetime.datetime.now(tz=datetime.UTC).date().isoformat(),
        "git_commit": commit,
        "licences": LICENCES,
        "files": rows,
    }
    (out / "manifest.json").write_text(json.dumps(manifest, indent=1))
    lines = [
        "# Evidence manifest",
        "",
        (
            f"Generated {manifest['generated']} at commit `{commit}` by `scripts/manifest.py`. The "
            "files live under the gitignored `data/` and `results/`; this list records what they "
            "are and their hashes."
        ),
        "",
        "## Licences (checked " + LICENCES["checked"] + ")",
        "",
    ]
    lines += [f"- **{k}**: {v}" for k, v in LICENCES.items() if k != "checked"]
    lines += [
        "",
        "## Files",
        "",
        "| file | role | licence | redistributable | sha256 (12) |",
        "|---|---|---|---|---|",
    ]
    for r in rows:
        lines.append(
            f"| `{r['path']}` | {r['role']} | {r['licence']} | {r['redistributable']} | "
            f"`{r['sha256'][:12]}` |"
        )
    unclassified = [r["path"] for r in rows if r["role"] == "UNCLASSIFIED"]
    (out / "MANIFEST.md").write_text("\n".join(lines) + "\n")
    print(f"{len(rows)} files; unclassified: {unclassified or 'none'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
