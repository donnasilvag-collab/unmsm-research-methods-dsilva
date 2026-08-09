# Results Directory

This directory is populated by `python src/run_experiments.py`.

- `benchmark_summary_seed_<seed>.csv` contains one repository-level descriptive comparison for each seed.
- `seed_stability.csv` joins the four runs and makes the bootstrap interval variation visible.

The difference is always calculated as **Peru minus Benchmark**. Negative values show that the public signals were lower in the Peru stratum for that observed proxy. They do not imply deficient internal controls, causal effects, or a population-level ranking of companies.

The four point estimates are identical across seeds because only the bootstrap resampling changes. The interval limits vary slightly and remain on the same side of zero in every run. A concise interpretation, including the owner-dependence audit, is available in [`../docs/analysis_report.md`](../docs/analysis_report.md).
