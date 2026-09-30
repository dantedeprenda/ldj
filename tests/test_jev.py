import json

import numpy as np
import pytest

from ldj import jev
from ldj.cache import CallCache
from ldj.llm import json_schema
from ldj.methods.llm import LLMAnswerer, LLMJudge
from ldj.task import Task


class FakeJev(jev.JevBackend):
    """No network: answers every noul question with a fixed P(yes) per question id."""

    def __init__(self, cache, **kw):
        super().__init__(cache=cache, **kw)
        self.posts = []

    def _post(self, req):
        self.posts.append(req)
        answers = {
            q: {"type": "noul", "noul": 0.1 * (i + 1)} for i, q in enumerate(req["questions"])
        }
        return {"model": "jev-test", "answers": answers, "usage": {"input_tokens": 1000}}, 0.01


def _task():
    return Task(
        "toy",
        ["a", "b"],
        ["first comment", "second comment"],
        [0.0, 1.0],
        ["", ""],
        [0],
        [1],
        1.0,
        1.0,
    )


def test_answerer_and_judge_run_on_jev_and_cache(tmp_path):
    cache = CallCache(tmp_path / "c.sqlite")
    b = FakeJev(cache, price_per_m_input=1.0)
    ans = LLMAnswerer(b, {"q1": "Is it rude?", "q2": "Is it long?"}, "Context.")
    x, cost = ans.matrix(_task(), np.array([0, 1]))
    assert np.allclose(x, [[0.1, 0.2], [0.1, 0.2]]) and np.allclose(cost, 0.001)
    sent = b.posts[0]
    assert sent["state"] == "first comment" and sent["model"] == "jev-1.13.0"
    assert sent["questions"]["q1"] == {"type": "noul", "instructions": "Is it rude?"}
    judge = LLMJudge(b, "Is this hate speech?")
    p = judge.fit(_task(), np.array([], int)).predict(_task(), np.array([0, 1]))
    assert np.allclose(p, 0.1)
    assert b.posts[-1]["questions"] == {
        "decision": {"type": "noul", "instructions": "Is this hate speech?"}
    }
    n = len(b.posts)
    ans2 = LLMAnswerer(FakeJev(cache), {"q1": "Is it rude?", "q2": "Is it long?"}, "Context.")
    ans2.matrix(_task(), np.array([0, 1]))  # served from the cache
    off = FakeJev(cache, offline=True)
    assert (
        json.loads(off.complete(ans.system, "### Item\nfirst comment", ans.format)[0])["q1"] == 0.1
    )
    assert (
        n == len(b.posts) and b.models_seen == {"jev-test"} and b.new_spend == pytest.approx(0.004)
    )


def test_offline_uncached_raises_and_uncached_ask_skips_cache(tmp_path):
    cache = CallCache(tmp_path / "c.sqlite")
    off = FakeJev(cache, offline=True)
    with pytest.raises(RuntimeError):
        off.ask("x", {"d": {"type": "noul", "instructions": "?"}})
    on = FakeJev(cache)
    on.ask("x", {"d": {"type": "noul", "instructions": "?"}}, use_cache=False)
    assert (
        cache.get(on.backend_id, on.request("x", {"d": {"type": "noul", "instructions": "?"}}))
        is None
    )


def test_unknown_format_rejected():
    with pytest.raises(ValueError):
        jev.jev_questions("x", json_schema("other", {"a": {"type": "number"}}))
