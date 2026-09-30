"""What every method is: learn from k labeled items, score any items.

``predict`` returns P(y = 1) (or any score where higher means more likely positive; the cost
model only thresholds it). ``spent`` accumulates the USD a method paid for external calls, so
total cost counts inference, not only labels and review.
"""

from __future__ import annotations

import numpy as np
from sklearn.linear_model import LogisticRegression, LogisticRegressionCV

from ldj.task import Task


class Method:
    name = "method"
    needs_labels = True

    def __init__(self) -> None:
        self.spent = 0.0

    def fit(self, task: Task, lab: np.ndarray) -> Method:
        return self

    def predict(self, task: Task, idx: np.ndarray) -> np.ndarray:
        raise NotImplementedError


class LogisticHead:
    """Logistic regression, C = 1; a constant when the labels hold one outcome.

    ``tune=True`` picks C by stratified CV on the labeled set only (C = 1 when an outcome has
    fewer than 2 labels). Identical to the routing paper's per-model heads.
    """

    CS = (0.01, 0.1, 1.0, 10.0, 100.0)

    def __init__(self, tune: bool = False):
        self.tune = tune

    def fit(self, x, y: np.ndarray) -> LogisticHead:
        y = (np.asarray(y) >= 0.5).astype(int)
        minority = int(min(y.sum(), len(y) - y.sum()))
        if minority == 0:
            self.model_ = float(y[0])
        elif self.tune and minority >= 2:
            self.model_ = LogisticRegressionCV(
                Cs=list(self.CS), cv=min(5, minority), scoring="roc_auc", max_iter=2000
            ).fit(x, y)
        else:
            self.model_ = LogisticRegression(max_iter=2000, C=1.0).fit(x, y)
        return self

    def predict(self, x) -> np.ndarray:
        if isinstance(self.model_, float):
            return np.full(x.shape[0], self.model_)
        return self.model_.predict_proba(x)[:, 1]


class BaseRate(Method):
    """The labeled share of positives for every item: knows nothing about the text."""

    name = "base_rate"

    def fit(self, task, lab):
        self.rate_ = float(task.y[lab].mean())
        return self

    def predict(self, task, idx):
        return np.full(len(idx), self.rate_)


class CategoryPrior(Method):
    """Labeled positive rate of the item's category, shrunk to the overall rate with one
    pseudo-count. Measures how much of a method's signal is just knowing the category."""

    name = "category_prior"

    def fit(self, task, lab):
        self.overall_ = float(task.y[lab].mean())
        self.rates_ = {}
        for c in np.unique(task.categories[lab]):
            m = task.categories[lab] == c
            self.rates_[c] = (task.y[lab][m].sum() + self.overall_) / (m.sum() + 1)
        return self

    def predict(self, task, idx):
        return np.array([self.rates_.get(c, self.overall_) for c in task.categories[idx]])
