"""SetFit: contrastive fine-tuning of a sentence encoder on the k labels, then a logistic head.

The standard few-shot text classifier (Tunstall et al. 2022). Pair sampling grows with k, so
training is capped at ``max_steps`` for the large budgets; the cap is part of the method's
definition and is reported with the results.
"""

from __future__ import annotations

import tempfile

import numpy as np

from ldj.methods.base import Method
from ldj.task import fit_text


class SetFit(Method):
    def __init__(
        self,
        model: str = "sentence-transformers/paraphrase-mpnet-base-v2",
        label: str = "setfit",
        max_chars: int = 2000,
        num_iterations: int = 20,
        max_steps: int = 500,
        batch_size: int = 16,
        seed: int = 0,
    ):
        super().__init__()
        self.model, self.max_chars = model, max_chars
        self.num_iterations, self.max_steps, self.batch_size, self.seed = (
            num_iterations,
            max_steps,
            batch_size,
            seed,
        )
        self.name = label

    def fit(self, task, lab):
        y = task.y[lab].astype(int)
        if y.min() == y.max():
            self.const_ = float(y[0])
            return self
        self.const_ = None
        from datasets import Dataset
        from setfit import SetFitModel, Trainer, TrainingArguments

        train = Dataset.from_dict(
            {
                "text": [fit_text(task.texts[i], self.max_chars) for i in lab],
                "label": y.tolist(),
            }
        )
        self.model_ = SetFitModel.from_pretrained(self.model)
        args = TrainingArguments(
            batch_size=self.batch_size,
            num_iterations=self.num_iterations,
            # one epoch over the sampled pairs, capped at max_steps for large k
            max_steps=min(self.max_steps, -(-self.num_iterations * 2 * len(lab) // self.batch_size))
            if self.num_iterations * 2 * len(lab) > self.max_steps * self.batch_size
            else -1,
            seed=self.seed,
            report_to="none",
            save_strategy="no",  # no checkpoints (about 1 GB each)
            output_dir=tempfile.mkdtemp(prefix="setfit_"),
        )
        Trainer(model=self.model_, args=args, train_dataset=train).train()
        return self

    def predict(self, task, idx):
        if self.const_ is not None:
            return np.full(len(idx), self.const_)
        texts = [fit_text(task.texts[i], self.max_chars) for i in idx]
        return np.asarray(self.model_.predict_proba(texts))[:, 1]
