# T1 whole-workflow ledger (exploratory; certified arm, error <= 0.10)

Human checks saved vs always-review, as a share of V (mean over draws; draws that certify nothing save nothing and still pay for labels), the share of draws that save anything, and dollars saved at $0.25 per review. Best cell per (labels, B) by saved share at V = 10k, plus the direct judge. **Descriptive: picked after seeing results.**

| labels | method | f | B | break-even V | saved @1k | @10k | @100k | P(win) @10k | $ saved @10k | @100k |
|---|---|---|---|---|---|---|---|---|---|---|
| consensus | bgeL_logreg | 0.10 | 25 | never | -14.1% | -1.4% | -0.1% | 0% | $-35 | $-35 |
| consensus | gemma_judge_0shot | 0.00 | 25 | never | -14.1% | -1.4% | -0.1% | 0% | $-36 | $-37 |
| consensus | bgeL_logreg | 0.10 | 50 | never | -28.3% | -2.8% | -0.3% | 0% | $-71 | $-71 |
| consensus | gemma_judge_0shot | 0.00 | 50 | never | -28.3% | -2.8% | -0.3% | 0% | $-71 | $-72 |
| consensus | gemma_judge_0shot | 0.00 | 100 | 52,656 | -55.5% | -4.6% | +0.5% | 2% | $-115 | $126 |
| consensus | gemma_features_judge | 0.25 | 200 | 2,884 | -73.9% | +27.9% | +38.1% | 75% | $698 | $9,524 |
| consensus | gemma_judge_0shot | 0.00 | 200 | 22,001 | -108.1% | -6.2% | +4.0% | 13% | $-154 | $1,002 |
| consensus | gemma_features_judge | 0.25 | 400 | 3,948 | -169.0% | +34.7% | +55.1% | 92% | $867 | $13,764 |
| consensus | gemma_judge_0shot | 0.00 | 400 | 23,806 | -216.9% | -13.1% | +7.2% | 24% | $-328 | $1,810 |
| consensus | gemma_features_judge | 0.50 | 800 | 6,681 | -385.0% | +22.5% | +63.2% | 97% | $562 | $15,805 |
| consensus | gemma_judge_0shot | 0.00 | 800 | 23,715 | -433.7% | -26.2% | +14.6% | 18% | $-655 | $3,640 |
| consensus @3 (too low) | bgeL_logreg | 0.10 | 25 | never | -7.5% | -0.8% | -0.1% | 0% | $-19 | $-19 |
| consensus @3 (too low) | gemma_judge_0shot | 0.00 | 25 | never | -7.5% | -0.8% | -0.1% | 0% | $-19 | $-20 |
| consensus @3 (too low) | bgeL_logreg | 0.10 | 50 | never | -15.0% | -1.5% | -0.1% | 0% | $-38 | $-38 |
| consensus @3 (too low) | gemma_judge_0shot | 0.00 | 50 | never | -15.0% | -1.5% | -0.1% | 0% | $-38 | $-39 |
| consensus @3 (too low) | gemma_judge_0shot | 0.00 | 100 | 27,910 | -28.9% | -1.9% | +0.8% | 2% | $-48 | $192 |
| consensus @3 (too low) | gemma_features_judge | 0.25 | 200 | 1,528 | -20.7% | +33.3% | +38.7% | 75% | $831 | $9,657 |
| consensus @3 (too low) | gemma_judge_0shot | 0.00 | 200 | 11,661 | -54.9% | -0.9% | +4.5% | 13% | $-21 | $1,135 |
| consensus @3 (too low) | gemma_features_judge | 0.25 | 400 | 2,092 | -62.6% | +45.4% | +56.1% | 94% | $1,133 | $14,030 |
| consensus @3 (too low) | gemma_judge_0shot | 0.00 | 400 | 12,618 | -110.5% | -2.5% | +8.3% | 24% | $-62 | $2,076 |
| consensus @3 (too low) | gemma_features_judge | 0.50 | 800 | 3,541 | -172.2% | +43.8% | +65.4% | 97% | $1,094 | $16,337 |
| consensus @3 (too low) | gemma_judge_0shot | 0.00 | 800 | 12,570 | -220.9% | -4.9% | +16.7% | 49% | $-123 | $4,172 |
| one annotator | bge_logreg | 0.10 | 25 | never | -2.5% | -0.2% | -0.0% | 0% | $-6 | $-6 |
| one annotator | gemma_judge_0shot | 0.00 | 25 | never | -2.5% | -0.2% | -0.0% | 0% | $-6 | $-8 |
| one annotator | bge_logreg | 0.10 | 50 | never | -5.0% | -0.5% | -0.1% | 0% | $-12 | $-12 |
| one annotator | gemma_judge_0shot | 0.00 | 50 | never | -5.0% | -0.5% | -0.1% | 0% | $-13 | $-14 |
| one annotator | gemma_features | 0.10 | 100 | 24,390 | -9.6% | -0.6% | +0.3% | 1% | $-15 | $72 |
| one annotator | gemma_judge_0shot | 0.00 | 100 | never | -10.0% | -1.0% | -0.1% | 0% | $-25 | $-26 |
| one annotator | gemma_features | 0.25 | 200 | 1,697 | -8.2% | +9.8% | +11.6% | 25% | $244 | $2,891 |
| one annotator | gemma_judge_0shot | 0.00 | 200 | 33,653 | -19.4% | -1.4% | +0.4% | 2% | $-35 | $97 |
| one annotator | gemma_features | 0.25 | 400 | 2,121 | -21.1% | +14.9% | +18.5% | 46% | $371 | $4,610 |
| one annotator | gemma_judge_0shot | 0.00 | 400 | 50,704 | -39.2% | -3.2% | +0.4% | 2% | $-80 | $96 |
| one annotator | gemma_features | 0.50 | 800 | 2,803 | -51.5% | +20.5% | +27.7% | 63% | $513 | $6,929 |
| one annotator | gemma_judge_0shot | 0.00 | 800 | 86,515 | -79.1% | -7.1% | +0.1% | 3% | $-177 | $30 |
