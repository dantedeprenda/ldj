import pytest

from ldj.recommend import fit_share, recommend, text


def test_budget_rules():
    assert recommend("classify", 100)["action"] == "insufficient evidence expected"
    r = recommend("classify", 200)
    assert r["action"] == "fit then certify" and r["fit_share"] == 0.25 and r["n_fit"] == 50
    assert recommend("classify", 400)["fit_share"] == 0.25
    assert recommend("classify", 800)["fit_share"] == 0.50
    assert fit_share(500) == 0.25 and fit_share(700) == 0.50 and fit_share(600) == 0.25
    assert recommend("classify", 400)["zero_error_min_audit"] == 29  # alpha 0.10, delta 0.05


def test_recall_positives_rule():
    low = recommend("recall", 400, prevalence=0.05)  # 0.05 * 0.9 * 400 = 18 expected
    assert low["action"] == "use certified stopping with active learning"
    assert low["zero_miss_positives"] == 59
    high = recommend("recall", 800, prevalence=0.10)  # 72 expected
    assert high["action"] == "certify from a random sample" and high["fit_share"] == 0.10
    assert recommend("recall", 400)["action"] == "need prevalence"


def test_label_source_warnings_and_note():
    r = recommend("classify", 400, label_source="majority")
    assert any("label definition" in w for w in r["warnings"])
    assert "preregistration/W5.md" in text(r)
    with pytest.raises(ValueError):
        recommend("rank", 400)
