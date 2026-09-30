# Evidence manifest

Generated 2026-09-30 at commit `2f69bb2` by `scripts/manifest.py`. The files live under the gitignored `data/` and `results/`; this list records what they are and their hashes.

## Licences (checked 2026-09-30)

- **code**: Apache-2.0 (this repository)
- **mhs**: CC-BY-4.0 (Measuring Hate Speech corpus); attribute Kennedy et al. 2020
- **synergy**: SYNERGY labels CC0; abstracts come from OpenAlex/publishers and are not redistributed: ship ids + a rebuild script + derived features
- **t0**: LLMRouterBench MIT; routing paper code MIT; Jev answers under TypeSafe's MCA, not published (derived metrics only)
- **t1_out**: Apache-2.0 for our code's outputs; Gemma outputs: Google claims no rights in outputs and they are not model derivatives (Gemma Terms of Use, last modified 2026-04-01); use stays subject to Gemma's prohibited-use policy; provider (OpenRouter) terms: re-check at release
- **t2_out**: as t1_out; no SYNERGY abstracts inside
- **t_out**: as t1_out
- **t0_out**: derived from Jev features and public benchmark outcomes; publish derived metrics only unless TypeSafe agrees otherwise
- **mixed**: item texts keep their source licence (MHS CC-BY-4.0; SYNERGY abstracts not redistributable)

## Files

| file | role | licence | redistributable | sha256 (12) |
|---|---|---|---|---|
| `data/audit/t1_audit.csv` | Audit: author-checked labels with item texts | mixed | no (T2 abstracts); labels and ids only | `3310cd28d36d` |
| `data/audit/t1_audit_claude.csv` | Audit: Claude's proposed labels | mixed | no (T1 texts offensive; T2 abstracts) | `e5cec7a10b5f` |
| `data/audit/t2_audit.csv` | Audit: author-checked labels with item texts | mixed | no (T2 abstracts); labels and ids only | `f88b9dae3580` |
| `data/audit/t2_audit_claude.csv` | Audit: Claude's proposed labels | mixed | no (T1 texts offensive; T2 abstracts) | `ddb06844b499` |
| `data/t0/llmrouterbench.npz` | T0 input: routing tasks, per-model correctness/cost, Jev answers | t0 | no (contains raw Jev answers) | `705e00ed7f53` |
| `data/t0/llmrouterbench_pool.npz` | T0 input: routing tasks, per-model correctness/cost, Jev answers | t0 | no (contains raw Jev answers) | `8d69aa5e5aae` |
| `data/t0/twinrouterbench.npz` | T0 input: routing tasks, per-model correctness/cost, Jev answers | t0 | no (contains raw Jev answers) | `c0fae41ddcfd` |
| `data/t1/measuring-hate-speech.parquet` | T1 input: comments and annotations | mhs | yes, with attribution | `6819525ce61b` |
| `data/t2/get.log` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `b4960378db94` |
| `data/t2/synergy/Abgaz_2023.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `c64ad9110467` |
| `data/t2/synergy/Adamo_2021.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `89801cd3d31b` |
| `data/t2/synergy/Ali_2024.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `44af9843a8be` |
| `data/t2/synergy/Anmarkrud_2021.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `8eb1ef3f8f28` |
| `data/t2/synergy/Aouad_2024.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `f44328f4c8b3` |
| `data/t2/synergy/Appenzeller-Herzog_2019.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `a4fe7335fff2` |
| `data/t2/synergy/Attai_2022.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `e547acbb1264` |
| `data/t2/synergy/Bakker-Jacobs_2022.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `2427afaa134a` |
| `data/t2/synergy/Bech_2019.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `74d7adf39a60` |
| `data/t2/synergy/Bindoli_2024a.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `02b314febcc8` |
| `data/t2/synergy/Bindoli_2024b.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `feaf9924fcb1` |
| `data/t2/synergy/Boersma-van_Dam_2024.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `1ed0c4d60e90` |
| `data/t2/synergy/Bos_2018.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `cda3e985bf6e` |
| `data/t2/synergy/Bosch_2021.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `ed67d7d69275` |
| `data/t2/synergy/Bosch_2023.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `f50b39500a42` |
| `data/t2/synergy/Brons_2024.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `11d2456c9ab2` |
| `data/t2/synergy/Brouwer_2019.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `37ee7f5313ae` |
| `data/t2/synergy/Burska_2023.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `974bab630447` |
| `data/t2/synergy/Butink_2023.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `1ab7c53f5801` |
| `data/t2/synergy/Chakraborty_2023.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `e789cc25ce83` |
| `data/t2/synergy/Chueca_2023.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `f5289108bafe` |
| `data/t2/synergy/Cinquin_2018.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `598177762337` |
| `data/t2/synergy/Clarinval_2021.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `57e0012b77f8` |
| `data/t2/synergy/Clark_2021.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `38d89630fec5` |
| `data/t2/synergy/Cozim-Melges_2024.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `d1d0a65ef0b9` |
| `data/t2/synergy/Deckers_2022.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `da71005ba860` |
| `data/t2/synergy/Dolinska_2022.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `8504dc2b0029` |
| `data/t2/synergy/Donners_2021.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `3c072d4ec40a` |
| `data/t2/synergy/Dornauer_2023.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `abee4f9a1cac` |
| `data/t2/synergy/Eggmann_2023.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `d1b4c9b957ad` |
| `data/t2/synergy/Endedijk_2021.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `46db982abc9e` |
| `data/t2/synergy/Farisogullari_2023.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `d4cb4f9c3633` |
| `data/t2/synergy/Fejza_2023.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `872a8b298f1c` |
| `data/t2/synergy/Ferreira_2022.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `7eabbc0d0eb3` |
| `data/t2/synergy/Filges_2018.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `979c5e4b2175` |
| `data/t2/synergy/Filges_2022.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `fe3f73eda628` |
| `data/t2/synergy/Fong_2021.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `dd976e2f9205` |
| `data/t2/synergy/Giesen_2021.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `12e882142258` |
| `data/t2/synergy/Greca_2023.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `103189ed7157` |
| `data/t2/synergy/Hall_2011.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `19527b770a1c` |
| `data/t2/synergy/Hamaker_2022.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `dd0f0f722450` |
| `data/t2/synergy/Hanlon_2022.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `c3570660bec2` |
| `data/t2/synergy/Harms_2024.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `f79ddb0dae54` |
| `data/t2/synergy/Hilfiker_2017.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `10b25a8465b4` |
| `data/t2/synergy/Kapuka_2021.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `f07f0fdd1920` |
| `data/t2/synergy/Kerschbaumer_2022.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `66760f9c1e99` |
| `data/t2/synergy/Kerschbaumer_2024a.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `a1fe84f2c368` |
| `data/t2/synergy/Kerschbaumer_2024b.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `66e9e2fc7512` |
| `data/t2/synergy/Lauper_2021.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `20c5e1bfd1a4` |
| `data/t2/synergy/Leenaars_2019.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `6f6493a6f912` |
| `data/t2/synergy/Leenaars_2020.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `860a4f873f90` |
| `data/t2/synergy/Lewowski_2021.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `8adb9fb44f58` |
| `data/t2/synergy/Low_2023.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `986be98010b8` |
| `data/t2/synergy/Maciel_2024.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `3b01d08e4673` |
| `data/t2/synergy/Marques_2021.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `5d99856b9861` |
| `data/t2/synergy/Meijboom_2021.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `95ed404d89ae` |
| `data/t2/synergy/Mejean_2024.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `d5904aab4e02` |
| `data/t2/synergy/Menon_2022.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `8036bb9027d2` |
| `data/t2/synergy/Mohamed_2023.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `0ca97d29b5af` |
| `data/t2/synergy/Monschau_2025.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `d2791345f064` |
| `data/t2/synergy/Moran_2020.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `9c5130bd8a32` |
| `data/t2/synergy/Moseng_2024.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `5c58aaaa1060` |
| `data/t2/synergy/Muthu_2020.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `8d9633fd88b8` |
| `data/t2/synergy/Nobrega-Dos_Santos_2023.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `ab421945515f` |
| `data/t2/synergy/Noetel_2021.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `c2daf07740a6` |
| `data/t2/synergy/Oliveira_2021.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `d60e6c56e5d8` |
| `data/t2/synergy/Oud_2018.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `4c0df5611a43` |
| `data/t2/synergy/Parodis_2023a.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `11a0adbddd21` |
| `data/t2/synergy/Parodis_2023b.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `d2f22daea64b` |
| `data/t2/synergy/Pijls_2017.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `5f52bdf2bd4f` |
| `data/t2/synergy/Pijls_2018.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `fe6bbb34eb20` |
| `data/t2/synergy/Pinos-Cisneros_2023.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `277a79123e1e` |
| `data/t2/synergy/Quevedo_2023.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `fd5e72f1f19d` |
| `data/t2/synergy/Ramiro_2015.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `9291347e640a` |
| `data/t2/synergy/Rinne_2021.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `a85936c83720` |
| `data/t2/synergy/Roberts_2021.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `e72a8cc68182` |
| `data/t2/synergy/Ruggeri_2019.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `eb9d9e5a8939` |
| `data/t2/synergy/Sanchez-Acedo_2023.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `f292d3b6ff89` |
| `data/t2/synergy/Sanchez-Alvarez_2023.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `8f159a15413e` |
| `data/t2/synergy/Sanchez-Gomez_2024.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `0973f7cff754` |
| `data/t2/synergy/Santos_2018.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `d0c23ecd7b0e` |
| `data/t2/synergy/Seghers_2022.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `bb5abb82643f` |
| `data/t2/synergy/Sep_2021.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `f697aab32bc6` |
| `data/t2/synergy/Sepriano_2020.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `b05128601ecc` |
| `data/t2/synergy/Sepriano_2022.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `ca10f625b97b` |
| `data/t2/synergy/Smid_2019.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `0d4daf2ae375` |
| `data/t2/synergy/Taschner_2024.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `756e26a8a05a` |
| `data/t2/synergy/Tektonidou_2019.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `5546d9b8c580` |
| `data/t2/synergy/Theobald_2021.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `7bdd34b2d212` |
| `data/t2/synergy/Toffalini_2021.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `f10ad03a2370` |
| `data/t2/synergy/Tumkaya_2018.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `aab3125c55d3` |
| `data/t2/synergy/Verdugo-Castro_2022.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `438e55c707bf` |
| `data/t2/synergy/Viguie_2020.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `e635cb5ede78` |
| `data/t2/synergy/Walker_2018.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `590e224004ff` |
| `data/t2/synergy/Ward_2020.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `e71cccd65ca5` |
| `data/t2/synergy/Wassenaar_2017.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `2006923259d1` |
| `data/t2/synergy/Webers_2022.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `b985c060a6f9` |
| `data/t2/synergy/Wijnen_2024.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `3356f351507e` |
| `data/t2/synergy/Williamson_2023.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `57213184ee68` |
| `data/t2/synergy/Wolters_2018.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `cd7a20dcaf97` |
| `data/t2/synergy/Xu_2022.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `843adf2c62ed` |
| `data/t2/synergy/Zakeri-Nasrabadi_2023a.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `ab97d0bc7591` |
| `data/t2/synergy/Zakeri-Nasrabadi_2023b.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `f49945d9630c` |
| `data/t2/synergy/Zanframundo_2022.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `38f51a89f69c` |
| `data/t2/synergy/Zinsser_2022.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `f9989693ff49` |
| `data/t2/synergy/de_Matteis_2024a.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `9699fc93d81d` |
| `data/t2/synergy/de_Matteis_2024b.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `b855f033640c` |
| `data/t2/synergy/metadata/review_metadata.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `7ac63edc310e` |
| `data/t2/synergy/van_Ballegooijen_2024.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `f5bcde55834a` |
| `data/t2/synergy/van_Dis_2019.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `a90a6118e7d1` |
| `data/t2/synergy/van_Heugten_Breurkes_2022.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `6f271290ae7e` |
| `data/t2/synergy/van_Hoorn_2020.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `bcb7fd85415a` |
| `data/t2/synergy/van_de_Schoot_2025.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `90d6dcb772d3` |
| `data/t2/synergy/van_der_Valk_2021.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `f4a1f1cd60c5` |
| `data/t2/synergy/van_der_Waal_2022.csv` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `b051006d3ea1` |
| `data/t2/synergy_cache.sqlite` | T2 input: SYNERGY records (build cache) | synergy | no (abstracts) | `27f713dd49a2` |
| `results/audit_t1.json` | Audit agreement and disagreeing ids | code | yes | `6d21a1522636` |
| `results/audit_t1_claude.json` | Audit agreement and disagreeing ids | code | yes | `151f4ac7f8e8` |
| `results/audit_t2.json` | Audit agreement and disagreeing ids | code | yes | `c013756beee8` |
| `results/audit_t2_claude.json` | Audit agreement and disagreeing ids | code | yes | `c013756beee8` |
| `results/bridge_t0/equal_cost.json` | W1 E-bridge reports | t0_out | yes (derived) | `b230b62cb92a` |
| `results/bridge_t0/equal_cost.md` | W1 E-bridge reports | t0_out | yes (derived) | `452b5da277d9` |
| `results/bridge_t0/report.json` | W1 E-bridge reports | t0_out | yes (derived) | `ca5feb06e649` |
| `results/bridge_t0/report.md` | W1 E-bridge reports | t0_out | yes (derived) | `ff03d760aa64` |
| `results/ledger_t1.csv` | W3 whole-workflow ledger | t_out | yes | `e051b2baf739` |
| `results/ledger_t1.md` | W3 whole-workflow ledger | t_out | yes | `29f29aff6bf4` |
| `results/t0_reproduce/preds.npz` | T0 reproduction of the routing paper | t0_out | check (predictions from Jev features) | `f97db88cb151` |
| `results/t0_reproduce/records.json` | T0 reproduction of the routing paper | t0_out | check (predictions from Jev features) | `55a69efb3da4` |
| `results/t0_reproduce/summary.md` | T0 reproduction of the routing paper | t0_out | check (predictions from Jev features) | `3035f00d8b66` |
| `results/t1/analysis.json` | T1 pre-registered run outputs | t1_out | yes (predictions, incl. Gemma judge probabilities) | `71b301ef0131` |
| `results/t1/analysis.md` | T1 pre-registered run outputs | t1_out | yes (predictions, incl. Gemma judge probabilities) | `3b2acadcd3ae` |
| `results/t1/analysis_audit.json` | T1 pre-registered run outputs | t1_out | yes (predictions, incl. Gemma judge probabilities) | `a6b7b42ce96d` |
| `results/t1/analysis_audit.md` | T1 pre-registered run outputs | t1_out | yes (predictions, incl. Gemma judge probabilities) | `5a271b896752` |
| `results/t1/preds.npz` | T1 pre-registered run outputs | t1_out | yes (predictions, incl. Gemma judge probabilities) | `d4fc1e5122b9` |
| `results/t1/records.json` | T1 pre-registered run outputs | t1_out | yes (predictions, incl. Gemma judge probabilities) | `4201c2ed69b8` |
| `results/t1/summary.md` | T1 pre-registered run outputs | t1_out | yes (predictions, incl. Gemma judge probabilities) | `e83d703a9216` |
| `results/t1_repro_h1/preds.npz` | Reproduction checks (fresh process) | t_out | yes | `890ebf686434` |
| `results/t1_repro_h1/records.json` | Reproduction checks (fresh process) | t_out | yes | `81d9a0c64aca` |
| `results/t1_repro_h1/summary.md` | Reproduction checks (fresh process) | t_out | yes | `a157ce3e8507` |
| `results/t1_smoke/analysis.json` | Smoke tests (not results) | t_out | not needed | `edc13e7428c2` |
| `results/t1_smoke/analysis.md` | Smoke tests (not results) | t_out | not needed | `84c36a62c085` |
| `results/t1_smoke/preds.npz` | Smoke tests (not results) | t_out | not needed | `805c4c5e6aa7` |
| `results/t1_smoke/records.json` | Smoke tests (not results) | t_out | not needed | `7ea077ca3570` |
| `results/t1_smoke/summary.md` | Smoke tests (not results) | t_out | not needed | `d6aa7c5d52fd` |
| `results/t2/analysis.json` | T2 pre-registered run outputs | t2_out | yes (scores and ids only; no abstracts) | `050c87a7e6a8` |
| `results/t2/analysis.md` | T2 pre-registered run outputs | t2_out | yes (scores and ids only; no abstracts) | `b2626c975af8` |
| `results/t2/analysis_audit.json` | T2 pre-registered run outputs | t2_out | yes (scores and ids only; no abstracts) | `36c5b1bd7788` |
| `results/t2/analysis_audit.md` | T2 pre-registered run outputs | t2_out | yes (scores and ids only; no abstracts) | `9bfc1f64b4c0` |
| `results/t2/preds.npz` | T2 pre-registered run outputs | t2_out | yes (scores and ids only; no abstracts) | `287e9f9a0232` |
| `results/t2/records.json` | T2 pre-registered run outputs | t2_out | yes (scores and ids only; no abstracts) | `9481459708ef` |
| `results/t2/summary.md` | T2 pre-registered run outputs | t2_out | yes (scores and ids only; no abstracts) | `0a35c14d2745` |
| `results/t2_repro_h1/preds.npz` | Reproduction checks (fresh process) | t_out | yes | `09e06b7623cf` |
| `results/t2_repro_h1/records.json` | Reproduction checks (fresh process) | t_out | yes | `840f1db52115` |
| `results/t2_repro_h1/summary.md` | Reproduction checks (fresh process) | t_out | yes | `135bd7faf50c` |
| `results/t2_smoke/preds.npz` | Smoke tests (not results) | t_out | not needed | `7f24f5f4d11e` |
| `results/t2_smoke/records.json` | Smoke tests (not results) | t_out | not needed | `8b14aca2718a` |
| `results/t2_smoke/summary.md` | Smoke tests (not results) | t_out | not needed | `197c7ba19528` |
| `results/x1_t1/analysis.json` | X1 exploratory outputs | t_out | yes | `a62597f7229f` |
| `results/x1_t1/analysis.md` | X1 exploratory outputs | t_out | yes | `84a131803261` |
| `results/x1_t1/calibration.md` | X1 exploratory outputs | t_out | yes | `dfe1e13c243c` |
| `results/x1_t1/preds.npz` | X1 exploratory outputs | t_out | yes | `e15310e0fcef` |
| `results/x1_t1/records.json` | X1 exploratory outputs | t_out | yes | `862d127f1726` |
| `results/x1_t1/summary.md` | X1 exploratory outputs | t_out | yes | `60cc27865765` |
| `results/x1_t2/analysis.json` | X1 exploratory outputs | t_out | yes | `f93fbde47257` |
| `results/x1_t2/analysis.md` | X1 exploratory outputs | t_out | yes | `d7b4a5aee936` |
| `results/x1_t2/calibration.md` | X1 exploratory outputs | t_out | yes | `bbb271eb8992` |
| `results/x1_t2/preds.npz` | X1 exploratory outputs | t_out | yes | `ea9c8f387e21` |
| `results/x1_t2/records.json` | X1 exploratory outputs | t_out | yes | `a55509390aa5` |
| `results/x1_t2/summary.md` | X1 exploratory outputs | t_out | yes | `31107174f674` |
| `results/x4_t0/config.json` | X4 exploratory allocation rows and summaries | t_out | yes | `b8230d76fa0b` |
| `results/x4_t0/rows.parquet` | X4 exploratory allocation rows and summaries | t_out | yes | `e81e0338cc7f` |
| `results/x4_t0/summary.csv` | X4 exploratory allocation rows and summaries | t_out | yes | `40d1343e5374` |
| `results/x4_t0/summary.md` | X4 exploratory allocation rows and summaries | t_out | yes | `b27fafeecbf5` |
| `results/x4_t1/config.json` | X4 exploratory allocation rows and summaries | t_out | yes | `754af211f4b3` |
| `results/x4_t1/rows.parquet` | X4 exploratory allocation rows and summaries | t_out | yes | `df4f67ae5143` |
| `results/x4_t1/summary.csv` | X4 exploratory allocation rows and summaries | t_out | yes | `3376061d0ac5` |
| `results/x4_t1/summary.md` | X4 exploratory allocation rows and summaries | t_out | yes | `f7a8830789e2` |
| `results/x4_t1_arms2/config.json` | X4 exploratory allocation rows and summaries | t_out | yes | `c4bc7d606ab4` |
| `results/x4_t1_arms2/rows.parquet` | X4 exploratory allocation rows and summaries | t_out | yes | `016e00b08dac` |
| `results/x4_t1_arms2/summary.csv` | X4 exploratory allocation rows and summaries | t_out | yes | `e53ab0664864` |
| `results/x4_t1_arms2/summary.md` | X4 exploratory allocation rows and summaries | t_out | yes | `fa32dc933f5d` |
| `results/x4_t1_pilot20/config.json` | X4 exploratory allocation rows and summaries | t_out | yes | `6d134de2fd57` |
| `results/x4_t1_pilot20/rows.parquet` | X4 exploratory allocation rows and summaries | t_out | yes | `c79a53394c82` |
| `results/x4_t1_pilot20/summary.csv` | X4 exploratory allocation rows and summaries | t_out | yes | `a581a7a8776a` |
| `results/x4_t1_pilot20/summary.md` | X4 exploratory allocation rows and summaries | t_out | yes | `a78ba2dace9e` |
| `results/x4_t1_single/config.json` | X4 exploratory allocation rows and summaries | t_out | yes | `00a0032ea517` |
| `results/x4_t1_single/rows.parquet` | X4 exploratory allocation rows and summaries | t_out | yes | `a03debd44efb` |
| `results/x4_t1_single/summary.csv` | X4 exploratory allocation rows and summaries | t_out | yes | `b70bce54002d` |
| `results/x4_t1_single/summary.md` | X4 exploratory allocation rows and summaries | t_out | yes | `4373310a12a1` |
| `results/x4_t2/config.json` | X4 exploratory allocation rows and summaries | t_out | yes | `9d8392bb6983` |
| `results/x4_t2/rows.parquet` | X4 exploratory allocation rows and summaries | t_out | yes | `69163bb40456` |
| `results/x4_t2/summary.csv` | X4 exploratory allocation rows and summaries | t_out | yes | `757c99033088` |
| `results/x4_t2/summary.md` | X4 exploratory allocation rows and summaries | t_out | yes | `684bc9971064` |
| `results/x4_t2_arms2/config.json` | X4 exploratory allocation rows and summaries | t_out | yes | `0df8b11e61a8` |
| `results/x4_t2_arms2/rows.parquet` | X4 exploratory allocation rows and summaries | t_out | yes | `3e0872ad90d0` |
| `results/x4_t2_arms2/summary.csv` | X4 exploratory allocation rows and summaries | t_out | yes | `6bdd87af668a` |
| `results/x4_t2_arms2/summary.md` | X4 exploratory allocation rows and summaries | t_out | yes | `9b660b0ebebe` |
