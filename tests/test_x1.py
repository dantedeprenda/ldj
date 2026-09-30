import numpy as np

from ldj.methods.llm import JudgePlatt, QuestionsPlusJudge
from ldj.task import Task


class FakeJudge:
    name = "fake_0shot"

    def __init__(self, p):
        self.p = np.asarray(p, float)

    def fit(self, task, lab):
        return self

    def predict(self, task, idx):
        self.cost_ = np.full(len(idx), 0.01)
        return self.p[idx]


class FakeAnswerer:
    def __init__(self, x):
        self.x = np.asarray(x, float)

    def matrix(self, task, idx):
        return self.x[idx], np.full(len(idx), 0.02)


def _task(n=60, seed=0):
    rng = np.random.default_rng(seed)
    y = (rng.random(n) < 0.4).astype(float)
    ids = [str(i) for i in range(n)]
    train, test = list(range(40)), list(range(40, n))
    return Task("toy", ids, [""] * n, y, [""] * n, train, test, 1.0, 1.0), rng


def test_platt_keeps_ranking_and_changes_scale():
    t, rng = _task()
    p = np.clip(0.3 * t.y + 0.35 + 0.3 * rng.random(len(t.y)), 0, 1)
    m = JudgePlatt(FakeJudge(p)).fit(t, np.arange(40))
    out = m.predict(t, t.test)
    assert np.array_equal(np.argsort(out, kind="stable"), np.argsort(p[t.test], kind="stable"))
    assert not np.allclose(out, p[t.test])
    assert np.allclose(m.cost_, 0.01)


def test_platt_keeps_raw_score_with_one_outcome():
    t, rng = _task()
    lab = np.flatnonzero(t.y[:40] == 0)
    p = rng.random(len(t.y))
    m = JudgePlatt(FakeJudge(p)).fit(t, lab)
    assert np.allclose(m.predict(t, t.test), p[t.test])


def test_questions_plus_judge_adds_one_feature_and_sums_cost():
    t, rng = _task()
    x = rng.random((len(t.y), 3))
    x[5, 1] = np.nan  # a failed answer: dropped in training, 0.5 at test
    judge = FakeJudge(t.y * 0.8 + 0.1)
    m = QuestionsPlusJudge(FakeAnswerer(x), judge, "q").fit(t, np.arange(40))
    assert m.head_.model_.coef_.shape == (1, 4)
    out = m.predict(t, t.test)
    assert out.shape == (20,) and np.allclose(m.cost_, 0.03)
    assert m.head_.model_.coef_[0, -1] > 0  # the (perfect) judge column carries the signal
