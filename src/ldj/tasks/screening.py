"""T2: systematic-review screening. Should this record go on to full-text review? (SYNERGY+)

SYNERGY+ v3.0 (ASReview, CC0 labels): 114 reviews with an official train/test split of reviews
(``synergy_dataset.TEST_SPLIT``, 23 test reviews), eligibility criteria and research questions per
review. Build it once with ``synergy get -l -o data/t2/synergy`` (run inside data/t2).

**Abstracts may not be republished as plain text** (SYNERGY legal note): they are reconstructed
locally from OpenAlex inverted indexes. Keep data/ out of git and never release abstracts;
derived features are fine.

PROVISIONAL choices, to be frozen in the T2 pre-registration:

- Item text = title + abstract. y = abstract-stage inclusion where the review provides it
  (``label_abstract_included``), else final inclusion (``label_included``); ``meta['target']``
  records which, per review.
- Category = review. Each review's records are split into train pool and test, stratified by y,
  so the k labels are a reviewer's own screening decisions pooled over the chosen reviews.
- The reviewer is a single human screener: right with P = 0.866 on included records and 0.792 on
  excluded ones (Gartlehner et al. 2020), at 60 s and GBP 1.175 per record (Shemilt et al. 2016,
  2013 GBP), converted at ``gbp_usd``. One label costs one screening decision.
- ``category_context`` holds each review's research question and eligibility criteria, which the
  LLM methods receive with every item (a human screener has them too).
"""

from __future__ import annotations

from pathlib import Path

import numpy as np

from ldj.task import Task

SENSITIVITY, SPECIFICITY = 0.866, 0.792  # single reviewer, Gartlehner et al. 2020
GBP_PER_RECORD = 1.175  # Shemilt et al. 2016: 1.0 min at the mean of GBP 0.97 and 1.38 per min


def available_reviews(root: str = "data/t2/synergy", split: str | None = None) -> list[str]:
    import pandas as pd

    meta = pd.read_csv(Path(root) / "metadata" / "review_metadata.csv")
    if split:
        meta = meta[meta.split == split]
    return sorted(k for k in meta.key if (Path(root) / f"{k}.csv").exists())


def load(
    reviews: list[str] | None = None,
    split: str | None = "test",
    root: str = "data/t2/synergy",
    test_frac: float = 0.5,
    max_records: int | None = None,
    seed: int = 0,
    gbp_usd: float = 1.56,
    min_positives: int = 0,
    cap_records: int | None = None,
) -> Task:
    """Records of ``reviews`` (default: every review in the official ``split``).

    ``min_positives`` drops reviews with fewer positives (so both halves can be scored);
    ``cap_records`` draws that many records uniformly from larger reviews (prevalence kept).
    ``max_records`` subsamples each review keeping every included record, for smoke tests only
    (it raises prevalence).
    """
    import pandas as pd

    meta = pd.read_csv(Path(root) / "metadata" / "review_metadata.csv").set_index("key")
    reviews = reviews or available_reviews(root, split)
    rng = np.random.default_rng(seed)
    ids, texts, y, cats, train, test, target = [], [], [], [], [], [], {}
    context = {}
    for r in reviews:
        d = pd.read_csv(Path(root) / f"{r}.csv")
        if "label_abstract_included" in d and d.label_abstract_included.notna().all():
            lab, target[r] = d.label_abstract_included.astype(int), "abstract"
        else:
            lab, target[r] = d.label_included.astype(int), "final"
        if lab.sum() < min_positives:
            del target[r]
            continue
        keep = np.arange(len(d))
        if cap_records and len(d) > cap_records:
            keep = np.sort(rng.choice(len(d), cap_records, replace=False))
        if max_records and len(d) > max_records:
            pos = np.flatnonzero(lab == 1)
            neg = rng.choice(
                np.flatnonzero(lab == 0), max(max_records - len(pos), 0), replace=False
            )
            keep = np.sort(np.concatenate([pos, neg]))
        start = len(ids)
        for i in keep:
            title = d.title.iloc[i] if isinstance(d.title.iloc[i], str) else ""
            abstract = d.abstract.iloc[i] if isinstance(d.abstract.iloc[i], str) else ""
            ids.append(f"{r}/{d.openalex_id.iloc[i].rsplit('/', 1)[-1]}")
            texts.append(f"{title}\n\n{abstract}".strip())
            y.append(int(lab.iloc[i]))
            cats.append(r)
        local = np.arange(start, len(ids))
        yl = np.array(y[start:])
        for outcome in (0, 1):  # stratified split within the review
            members = rng.permutation(local[yl == outcome])
            n_test = round(len(members) * test_frac)
            test.extend(members[:n_test])
            train.extend(members[n_test:])
        m = meta.loc[r]
        context[r] = (
            f"Research question: {m.research_question}\n"
            f"Eligibility criteria: {m.eligibility_criteria}"
        )
    y = np.array(y, dtype=float)
    return Task(
        name="t2_screening",
        ids=ids,
        texts=texts,
        y=y,
        categories=np.array(cats),
        train=np.sort(train),
        test=np.sort(test),
        review_cost=GBP_PER_RECORD * gbp_usd,
        human_correct=np.where(y == 1, SENSITIVITY, SPECIFICITY),
        label_cost=GBP_PER_RECORD * gbp_usd,
        auto_negative=True,
        meta={"target": target, "category_context": context, "split": split, "seed": seed},
    )
