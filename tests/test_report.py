import re

import numpy as np
import pandas as pd

from ldj.allocate import Policy
from ldj.audit import audit
from ldj.report import audit_html, bridge_html, bridge_result, replay_html


def _no_external(html: str) -> None:
    assert not re.search(r"(src|href)\s*=", html)
    assert "http://" not in html and "https://" not in html
    assert "<script" not in html


def _audit(n_audit, seed=0):
    rng = np.random.default_rng(seed)
    n = n_audit + 5000  # same draws as tests/test_audit.py
    s = rng.random(n)
    y = (rng.random(n) >= 0.02 + 0.6 * (1 - s)).astype(float)
    return audit(s[:n_audit], y[:n_audit], s[n_audit:], Policy("accept", alpha=0.10))


def test_audit_html_supported_and_insufficient():
    ok = audit_html(_audit(1500))
    assert "Evidence supports this policy" in ok and "Assumptions this tool cannot check" in ok
    no = audit_html(_audit(30))
    assert "Insufficient evidence" in no and "at least 29 audit items" in no
    assert "not a promise about the share of issued certificates" in no
    assert "nothing about any single automated item" in no
    for h in (ok, no):
        _no_external(h)
        assert h.startswith("<!doctype html>") and "prefers-color-scheme: dark" in h


def test_audit_html_escapes_text():
    r = _audit(30)
    r["assumptions"] = ["<script>alert(1)</script> & more"]
    h = audit_html(r)
    assert "<script>alert" not in h and "&lt;script&gt;alert(1)&lt;/script&gt; &amp; more" in h


def test_bridge_html_from_csv(tmp_path):
    f = tmp_path / "p.csv"
    pd.DataFrame(
        {
            "default_ok": [1, 1, 0, 0, 0, 1],
            "fallback_ok": [1, 0, 1, 0, 1, 1],
            "default_cost": [1.0] * 6,
            "fallback_cost": [10.0] * 6,
            "risk": [0.1, 0.9, 0.8, 0.5, 0.7, 0.2],
        }
    ).to_csv(f, index=False)
    res = bridge_result(str(f), ["risk"], [0.5])
    assert res["table"]["only_fallback_right"] == 2 and len(res["rows"]) == 3
    h = bridge_html(res)
    assert "Escalation value" in h and "+0.167" in h and "oracle" in h
    _no_external(h)


def test_replay_html():
    demo = [
        {
            "alpha": 0.1,
            "audit_size": 50,
            "verdict": "insufficient evidence",
            "automated_share": 0.0,
            "what_would_help": "needs <more> labels",
        },
        {
            "alpha": 0.21,
            "audit_size": 50,
            "verdict": "supported",
            "automated_share": 0.75,
            "what_would_help": None,
        },
    ]
    h = replay_html("moderation-v1", True, True, 87.0, demo)
    assert "Every number matches" in h and "needs &lt;more&gt; labels" in h and "75.0%" in h
    _no_external(h)
    assert "MISMATCH" in replay_html("x", False, True, 1.0, demo)
