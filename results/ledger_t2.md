# T2 ledger: screening decisions saved (exploratory)

15 reviews, 15,121 records in total; $1.83 per screening decision. Labels are screenings of pool items, so they add no cost. Mean over 500 draws; a draw that certifies nothing saves nothing. Best certified cell per (method, B) by records saved; picked after seeing results.

| method | f | B | reviews able to run B | reviews certifying | records saved (all reviews) | share of all records | $ saved |
|---|---|---|---|---|---|---|---|
| bgeL_logreg | 0.10 | 25 | 14 | 0 | 0 | 0.0% | $0 |
| bgeL_logreg | 0.10 | 50 | 13 | 0 | 0 | 0.0% | $0 |
| bgeL_logreg | 0.10 | 100 | 11 | 0 | 0 | 0.0% | $0 |
| bgeL_logreg | 0.10 | 200 | 8 | 0 | 0 | 0.0% | $0 |
| bgeL_logreg | 0.10 | 400 | 6 | 0 | 0 | 0.0% | $0 |
| bgeL_logreg | 0.10 | 800 | 3 | 1 | 226 | 1.5% | $414 |
| bge_logreg | 0.10 | 25 | 14 | 0 | 0 | 0.0% | $0 |
| bge_logreg | 0.10 | 50 | 13 | 0 | 0 | 0.0% | $0 |
| bge_logreg | 0.10 | 100 | 11 | 0 | 0 | 0.0% | $0 |
| bge_logreg | 0.10 | 200 | 8 | 0 | 0 | 0.0% | $0 |
| bge_logreg | 0.10 | 400 | 6 | 0 | 0 | 0.0% | $0 |
| bge_logreg | 0.10 | 800 | 3 | 1 | 234 | 1.5% | $429 |
| gemma_features | 0.10 | 25 | 14 | 0 | 0 | 0.0% | $0 |
| gemma_features | 0.10 | 50 | 13 | 0 | 0 | 0.0% | $0 |
| gemma_features | 0.10 | 100 | 11 | 0 | 0 | 0.0% | $0 |
| gemma_features | 0.10 | 200 | 8 | 0 | 0 | 0.0% | $0 |
| gemma_features | 0.10 | 400 | 6 | 0 | 0 | 0.0% | $0 |
| gemma_features | 0.10 | 800 | 3 | 1 | 577 | 3.8% | $1,057 |
| gemma_features_judge | 0.10 | 25 | 14 | 0 | 0 | 0.0% | $0 |
| gemma_features_judge | 0.10 | 50 | 13 | 0 | 0 | 0.0% | $0 |
| gemma_features_judge | 0.10 | 100 | 11 | 0 | 0 | 0.0% | $0 |
| gemma_features_judge | 0.10 | 200 | 8 | 0 | 0 | 0.0% | $0 |
| gemma_features_judge | 0.10 | 400 | 6 | 0 | 0 | 0.0% | $0 |
| gemma_features_judge | 0.10 | 800 | 3 | 1 | 576 | 3.8% | $1,056 |
| gemma_judge_0shot | 0.00 | 25 | 14 | 0 | 0 | 0.0% | $0 |
| gemma_judge_0shot | 0.00 | 50 | 13 | 0 | 0 | 0.0% | $0 |
| gemma_judge_0shot | 0.00 | 100 | 11 | 0 | 0 | 0.0% | $0 |
| gemma_judge_0shot | 0.00 | 200 | 8 | 0 | 0 | 0.0% | $0 |
| gemma_judge_0shot | 0.00 | 400 | 6 | 0 | 0 | 0.0% | $0 |
| gemma_judge_0shot | 0.00 | 800 | 3 | 0 | 0 | 0.0% | $0 |
| tfidf_logreg | 0.10 | 25 | 14 | 0 | 0 | 0.0% | $0 |
| tfidf_logreg | 0.10 | 50 | 13 | 0 | 0 | 0.0% | $0 |
| tfidf_logreg | 0.10 | 100 | 11 | 0 | 0 | 0.0% | $0 |
| tfidf_logreg | 0.10 | 200 | 8 | 0 | 0 | 0.0% | $0 |
| tfidf_logreg | 0.10 | 400 | 6 | 0 | 0 | 0.0% | $0 |
| tfidf_logreg | 0.10 | 800 | 3 | 1 | 135 | 0.9% | $248 |

Best cell per review:

| review | records | method | f | B | useful | records saved | $ saved |
|---|---|---|---|---|---|---|---|
| Moran_2020 | 1992 | gemma_features | 0.10 | 800 | 1.00 | 577 | $1,057 |
| Abgaz_2023 | 288 | nothing certifies at any B | | | | 0 | $0 |
| Attai_2022 | 1726 | nothing certifies at any B | | | | 0 | $0 |
| Boersma-van_Dam_2024 | 578 | nothing certifies at any B | | | | 0 | $0 |
| Bosch_2021 | 1716 | nothing certifies at any B | | | | 0 | $0 |
| Chakraborty_2023 | 2000 | nothing certifies at any B | | | | 0 | $0 |
| Chueca_2023 | 609 | nothing certifies at any B | | | | 0 | $0 |
| Harms_2024 | 840 | nothing certifies at any B | | | | 0 | $0 |
| Lewowski_2021 | 329 | nothing certifies at any B | | | | 0 | $0 |
| Menon_2022 | 485 | nothing certifies at any B | | | | 0 | $0 |
| Parodis_2023b | 1679 | nothing certifies at any B | | | | 0 | $0 |
| Toffalini_2021 | 328 | nothing certifies at any B | | | | 0 | $0 |
| Tumkaya_2018 | 481 | nothing certifies at any B | | | | 0 | $0 |
| Walker_2018 | 2000 | nothing certifies at any B | | | | 0 | $0 |

Too small for any budget (B + 100 unlabeled > pool): Theobald_2021.
