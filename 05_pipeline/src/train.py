"""Run one seeded, organization-clustered descriptive benchmark analysis.

The filename follows the course pipeline convention. This script does not train a
predictive model; it summarizes public repository signals and their uncertainty.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd
import yaml


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=Path("data/public_repo_security_benchmark.csv"))
    parser.add_argument("--params", type=Path, default=Path("params.yaml"))
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--seed", type=int, required=True)
    return parser.parse_args()


def clustered_bootstrap_mean(
    cluster_sums: np.ndarray,
    cluster_counts: np.ndarray,
    rng: np.random.Generator,
) -> float:
    """Sample organizations with replacement, retaining all their repositories."""
    indices = rng.integers(0, len(cluster_sums), size=len(cluster_sums))
    return float(cluster_sums[indices].sum() / cluster_counts[indices].sum())


def main() -> None:
    args = parse_args()
    params = yaml.safe_load(args.params.read_text(encoding="utf-8"))
    analysis = params["analysis"]
    frame = pd.read_csv(args.input)

    peru = frame.loc[frame["stratum"] == analysis["peru_label"]].copy()
    benchmark = frame.loc[frame["stratum"] == analysis["benchmark_label"]].copy()
    if peru.empty or benchmark.empty:
        raise ValueError("Both documented strata must be present in the derived dataset.")

    rng = np.random.default_rng(args.seed)
    rows: list[dict[str, float | int | str]] = []
    for dimension in analysis["dimensions"]:
        peru_mean = float(peru[dimension].mean())
        benchmark_mean = float(benchmark[dimension].mean())
        clustered = peru.groupby(analysis["peru_cluster_column"], sort=True)[dimension].agg(["sum", "count"])
        cluster_sums = clustered["sum"].to_numpy(dtype=float)
        cluster_counts = clustered["count"].to_numpy(dtype=float)
        benchmark_values = benchmark[dimension].to_numpy(dtype=float)
        differences = np.empty(analysis["bootstrap_iterations"])
        for index in range(analysis["bootstrap_iterations"]):
            peru_sample = clustered_bootstrap_mean(cluster_sums, cluster_counts, rng)
            benchmark_sample = float(rng.choice(benchmark_values, size=len(benchmark_values), replace=True).mean())
            differences[index] = peru_sample - benchmark_sample

        lower, upper = np.quantile(differences, [0.025, 0.975])
        rows.append(
            {
                "seed": args.seed,
                "dimension": dimension,
                "peru_repository_mean": peru_mean,
                "benchmark_repository_mean": benchmark_mean,
                "difference_peru_minus_benchmark": peru_mean - benchmark_mean,
                "bootstrap_ci_95_lower": float(lower),
                "bootstrap_ci_95_upper": float(upper),
                "peru_repository_count": len(peru),
                "peru_organization_cluster_count": peru[analysis["peru_cluster_column"]].nunique(),
                "benchmark_repository_count": len(benchmark),
                "bootstrap_iterations": analysis["bootstrap_iterations"],
                "analysis_unit": analysis["unit_of_analysis"],
                "scope_note": params["reporting"]["scope_note"],
            }
        )

    result = pd.DataFrame(rows)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    result.to_csv(
        args.output,
        index=False,
        float_format="%.6f",
        lineterminator="\n",
    )
    print(f"Created {args.output} for seed {args.seed}.")


if __name__ == "__main__":
    main()
