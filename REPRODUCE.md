# Reproducing the moderation result

Thank you for trying this. The goal is to check that someone other than the author can rebuild a
headline result from this repository alone, and to record anything that got in the way. It takes
about 5–10 minutes (on an Apple M2: install ~1 min, tests ~75 s, replay ~70 s), needs no API key,
no GPU and no dataset download, and uses about 700 MB of disk.

## What you need

- macOS or Linux, about 2 GB free disk space, an internet connection for installing packages.
- [uv](https://docs.astral.sh/uv/getting-started/installation/) (the Python package manager). The
  repository pins Python 3.13 (`.python-version`); uv fetches it if you don't have it.

## Steps

```bash
git clone https://github.com/dantedeprenda/ldj.git
cd ldj
git rev-parse --short HEAD          # note this commit id
uv sync --extra dev                 # installs the locked package versions
uv run pytest -q                    # all tests should pass
shasum -a 256 -c release/fixtures/moderation-v1/SHA256SUMS   # optional: the fixture is unmodified
uv run ldj reproduce --fixture moderation-v1 2>&1 | tee reproduce.log
```

The last command reruns the pre-registered analysis of the T1 (content moderation) result from the
saved predictions in `release/fixtures/moderation-v1/` and compares every number with the packaged
one. It first prints the analysis tables (about 110 lines); **the verdict is at the end**:

```
- Pre-registered analysis matches the packaged numbers: **yes**
- Audit demo matches: **yes**
```

followed by the audit demo: "insufficient evidence" at error-rate target 0.10 (50 and 1,000 audit
labels) and "supported" at 0.21 (about 75% and 80% of items automated). The command exits with
status 1 if either check says **NO**.

Results are written to `results/reproduce/moderation-v1/` (`replay.md`, `replay.html`,
`analysis.md`, `analysis.json`).

## Reporting your result

Please open a GitHub issue with:

1. The commit id, your operating system and chip (e.g. "macOS 26, Apple M2" or "Ubuntu 24.04,
   x86_64"), and `uv --version`.
2. The output of the test command and `reproduce.log` (or the files in
   `results/reproduce/moderation-v1/`).
3. Anything you had to do that these instructions did not say, anything unclear, and how long it
   took.
4. Whether you are happy to be named in the write-up as the reproducer (optional).

A "NO" in either check line is a useful result too; please report it as is.

## What this does and does not check

It checks that the analysis and the audit command rebuild the published numbers from the saved
predictions. It does not rerun the language-model calls (that needs a paid API key and the
author's call cache) and does not by itself show the method works on new data; the fresh-data test
is separate (`preregistration/W5.md`).
