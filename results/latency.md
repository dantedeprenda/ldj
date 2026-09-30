# Latency per call

Measured from the call cache on every real call made (cached calls keep their original latency).
Indicative, not a controlled benchmark: calls ran at different concurrency, rate limits and times
of day.

| Model | Calls | p50 | p95 |
|---|---|---|---|
| Jev (jev-1.13.0, TypeSafe) | 4,999 | 0.28 s | 0.39 s |
| Llama 3.3 70B (OpenRouter) | 5,294 | 0.90 s | 3.54 s |
| Gemma 4 26B (OpenRouter) | 79,688 | 1.50 s | 6.93 s |
