"""Compare naive and owner-clustered uncertainty estimates for the benchmark.

The public benchmark is descriptive and contains no person-level decision or
protected attribute. The before-and-after comparison therefore addresses
repository dependence, not demographic fairness or predictive performance.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yaml


ROOT = Path(__file__).resolve().parents[1]
PIPELINE = ROOT / "05_pipeline"
INPUT = PIPELINE / "data" / "public_repo_security_benchmark.csv"
PARAMS = PIPELINE / "params.yaml"
OUTPUT_CSV = Path(__file__).with_name("bias_audit_splits.csv")
OUTPUT_CHART = Path(__file__).with_name("before_after_chart.png")


def bootstrap_intervals(
    peru: pd.DataFrame,
    benchmark: pd.DataFrame,
    dimension: str,
    cluster_column: str,
    iterations: int,
    seed: int,
) -> tuple[tuple[float, float], tuple[float, float]]:
    """Return naive row-level and owner-clustered 95% bootstrap intervals."""
    naive_rng, clustered_rng, benchmark_rng = [
        np.random.default_rng(child) for child in np.random.SeedSequence(seed).spawn(3)
    ]
    peru_values = peru[dimension].to_numpy(dtype=float)
    benchmark_values = benchmark[dimension].to_numpy(dtype=float)
    clusters = peru.groupby(cluster_column, sort=True)[dimension].agg(["sum", "count"])
    cluster_sums = clusters["sum"].to_numpy(dtype=float)
    cluster_counts = clusters["count"].to_numpy(dtype=float)

    naive_differences = np.empty(iterations)
    clustered_differences = np.empty(iterations)
    for index in range(iterations):
        benchmark_mean = float(
            benchmark_rng.choice(
                benchmark_values, size=len(benchmark_values), replace=True
            ).mean()
        )
        naive_peru_mean = float(
            naive_rng.choice(peru_values, size=len(peru_values), replace=True).mean()
        )
        sampled_clusters = clustered_rng.integers(
            0, len(cluster_sums), size=len(cluster_sums)
        )
        clustered_peru_mean = float(
            cluster_sums[sampled_clusters].sum()
            / cluster_counts[sampled_clusters].sum()
        )
        naive_differences[index] = naive_peru_mean - benchmark_mean
        clustered_differences[index] = clustered_peru_mean - benchmark_mean

    naive_interval = tuple(np.quantile(naive_differences, [0.025, 0.975]))
    clustered_interval = tuple(
        np.quantile(clustered_differences, [0.025, 0.975])
    )
    return naive_interval, clustered_interval


def run_audit() -> pd.DataFrame:
    if not INPUT.exists():
        raise FileNotFoundError(
            f"{INPUT} is missing. Run 'dvc repro' in 05_pipeline first."
        )

    params = yaml.safe_load(PARAMS.read_text(encoding="utf-8"))
    analysis = params["analysis"]
    frame = pd.read_csv(INPUT)
    peru = frame.loc[frame["stratum"] == analysis["peru_label"]].copy()
    benchmark = frame.loc[
        frame["stratum"] == analysis["benchmark_label"]
    ].copy()
    if peru.empty or benchmark.empty:
        raise ValueError("Both documented strata must be present.")

    rows: list[dict[str, float | int | str]] = []
    for seed in analysis["seeds"]:
        for dimension in analysis["dimensions"]:
            naive, clustered = bootstrap_intervals(
                peru=peru,
                benchmark=benchmark,
                dimension=dimension,
                cluster_column=analysis["peru_cluster_column"],
                iterations=analysis["bootstrap_iterations"],
                seed=seed,
            )
            point_difference = float(
                peru[dimension].mean() - benchmark[dimension].mean()
            )
            naive_width = float(naive[1] - naive[0])
            clustered_width = float(clustered[1] - clustered[0])
            rows.append(
                {
                    "seed": seed,
                    "dimension": dimension,
                    "point_difference": point_difference,
                    "naive_ci_95_lower": naive[0],
                    "naive_ci_95_upper": naive[1],
                    "naive_ci_width": naive_width,
                    "clustered_ci_95_lower": clustered[0],
                    "clustered_ci_95_upper": clustered[1],
                    "clustered_ci_width": clustered_width,
                    "width_change_clustered_minus_naive": (
                        clustered_width - naive_width
                    ),
                    "peru_repository_count": len(peru),
                    "peru_owner_count": peru[
                        analysis["peru_cluster_column"]
                    ].nunique(),
                    "benchmark_repository_count": len(benchmark),
                    "bootstrap_iterations": analysis["bootstrap_iterations"],
                }
            )

    result = pd.DataFrame(rows)
    result.to_csv(OUTPUT_CSV, index=False, float_format="%.6f")
    return result


def write_chart(result: pd.DataFrame) -> None:
    plot_data = (
        result.groupby("dimension", sort=False)[
            ["naive_ci_width", "clustered_ci_width"]
        ]
        .mean()
        .reset_index()
    )
    labels = (
        plot_data["dimension"]
        .str.replace("_observed", "", regex=False)
        .str.replace("_", " ", regex=False)
        .str.title()
    )
    positions = np.arange(len(plot_data))
    width = 0.34

    figure, axis = plt.subplots(figsize=(12, 7))
    figure.patch.set_facecolor("#F7F3EA")
    axis.set_facecolor("#F7F3EA")
    axis.bar(
        positions - width / 2,
        plot_data["naive_ci_width"],
        width,
        label="Naive row bootstrap",
        color="#A3A3A3",
    )
    axis.bar(
        positions + width / 2,
        plot_data["clustered_ci_width"],
        width,
        label="Owner-clustered bootstrap",
        color="#7A1831",
    )
    axis.set_xticks(positions, labels, rotation=12, ha="right")
    axis.set_ylabel("Mean 95% confidence-interval width across four seeds")
    axis.set_title(
        "Uncertainty before and after correcting repository dependence",
        loc="left",
        weight="bold",
    )
    axis.legend(frameon=False, loc="upper right")
    axis.spines[["top", "right"]].set_visible(False)
    axis.grid(axis="y", color="#D8D0C2", linewidth=0.8)
    axis.set_axisbelow(True)
    figure.text(
        0.01,
        0.01,
        "Descriptive public-repository benchmark; not a protected-group fairness intervention.",
        color="#554E45",
        fontsize=9,
    )
    figure.tight_layout(rect=(0, 0.04, 1, 1))
    figure.savefig(OUTPUT_CHART, dpi=100)
    plt.close(figure)


def main() -> None:
    result = run_audit()
    write_chart(result)
    print(
        f"Wrote {len(result)} audit rows to {OUTPUT_CSV.name} "
        f"and refreshed {OUTPUT_CHART.name}."
    )


if __name__ == "__main__":
    main()
