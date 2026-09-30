# Fixture moderation-v2

The T1 (content moderation) X1 run, packaged for `ldj reproduce --fixture moderation-v2`. It
rebuilds `results/x1_t1/analysis.md` (features + judge vs question features, bge-large and the
zero-shot judge; exploratory) and an audit demo of the frozen default rule's method
(features + judge, preregistration/default-rule.md) offline.

- `task.npz`: for the 2,000 test comments: ids, consensus label, platform, one annotator's
  correctness, costs. No texts.
- `preds.npz`, `records.json`: the X1 run's saved test predictions and records.
- `config.yaml`: configs/x1_t1.yaml. `demo.json`: the audit demo. `expected.json`: outputs to match.

Data: Measuring Hate Speech corpus (Kennedy et al. 2020, CC-BY-4.0). Gemma outputs: Google claims
no rights in Gemma outputs (Gemma Terms of Use). Code: Apache-2.0.
