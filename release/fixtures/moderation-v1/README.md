# Fixture moderation-v1

The T1 (content moderation) pre-registered result, packaged for `ldj reproduce --fixture
moderation-v1`. It rebuilds `results/t1/analysis.md` (H1–H3) and an audit demo offline.

- `task.npz`: for the 2,000 test comments: ids, the consensus label (hate speech score > 0.5),
  platform category, one real annotator's correctness, review and automation costs. No texts.
- `preds.npz`, `records.json`: every method's saved test predictions and run records.
- `config.yaml`: the pre-registered T1 config. `expected.json`: the outputs to match.

Data: Measuring Hate Speech corpus (Kennedy et al. 2020, CC-BY-4.0), ucberkeley-dlab. Gemma judge
probabilities are model outputs; Google claims no rights in Gemma outputs (Gemma Terms of Use).
Code: Apache-2.0.
