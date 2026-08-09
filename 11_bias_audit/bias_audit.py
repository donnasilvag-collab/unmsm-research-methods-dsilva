"""Audit dependence and owner influence in the public repository benchmark.

The benchmark has no classifier, protected attribute, or person-level decision.
The appropriate algorithm compares naive and owner-clustered uncertainty, then
tests whether one Peru-stratum owner dominates a descriptive difference.
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
OUTPUT_SPLITS = Path(__file__).with_name("bias_audit_splits.csv")
OUTPUT_INFLUENCE = Path(__file__).with_name("owner_influence_diagnostics.csv")
OUTPUT_SUMMARY = Path(__file__).with_name("bias_audit_summary.csv")
OUTPUT_CHART = Path(__file__).with_name("before_after_chart.png")
RELATIVE_SHIFT_REVIEW_THRESHOLD = 0.25


def bootstrap_intervals(
    peru: pd.DataFrame,
    benchmark: pd.DataFrame,
    dimension: str,
    cluster_column: str,
    iterations: int,
    seed: int,
) -> tuple[tuple[float, float], tuple[float, float]]:
    """Return naive row and owner-clustered 95% bootstrap intervals."""
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
    clustered_interval = tuple(np.quantile(clustered_differences, [0.025, 0.975]))
    return naive_interval, clustered_interval


def owner_influence(
    peru: pd.DataFrame,
    benchmark: pd.DataFrame,
    dimensions: list[str],
    cluster_column: str,
) -> pd.DataFrame:
    """Calculate leave-one-owner-out influence without publishing owner names."""
    owners = sorted(peru[cluster_column].dropna().unique())
    aliases = {owner: f"ORG{index:02d}" for index, owner in enumerate(owners, start=1)}
    rows: list[dict[str, float | bool | str]] = []

    for dimension in dimensions:
        benchmark_mean = float(benchmark[dimension].mean())
        full_difference = float(peru[dimension].mean() - benchmark_mean)
        denominator = max(abs(full_difference), np.finfo(float).eps)
        for owner in owners:
            reduced = peru.loc[peru[cluster_column] != owner]
            reduced_difference = float(reduced[dimension].mean() - benchmark_mean)
            shift = reduced_difference - full_difference
            sign_flip = bool(
                full_difference != 0
                and reduced_difference != 0
                and np.sign(full_difference) != np.sign(reduced_difference)
            )
            rows.append(
                {
                    "dimension": dimension,
                    "omitted_owner_alias": aliases[owner],
                    "full_point_difference": full_difference,
                    "leave_one_owner_out_difference": reduced_difference,
                    "absolute_shift": abs(shift),
                    "relative_shift": abs(shift) / denominator,
                    "sign_flip": sign_flip,
                    "remaining_owner_count": len(owners) - 1,
                }
            )

    result = pd.DataFrame(rows)
    result.to_csv(
        OUTPUT_INFLUENCE,
        index=False,
        float_format="%.6f",
        lineterminator="\n",
    )
    return result


def build_summary(splits: pd.DataFrame, influence: pd.DataFrame) -> pd.DataFrame:
    """Combine interval and leave-one-owner-out diagnostics by dimension."""
    rows: list[dict[str, float | int | str]] = []
    for dimension, dimension_splits in splits.groupby("dimension", sort=False):
        dimension_influence = influence.loc[influence["dimension"] == dimension]
        most_influential = dimension_influence.loc[
            dimension_influence["absolute_shift"].idxmax()
        ]
        naive_width = float(dimension_splits["naive_ci_width"].mean())
        clustered_width = float(dimension_splits["clustered_ci_width"].mean())
        max_relative_shift = float(dimension_influence["relative_shift"].max())
        sign_flips = int(dimension_influence["sign_flip"].sum())
        requires_review = (
            sign_flips > 0 or max_relative_shift > RELATIVE_SHIFT_REVIEW_THRESHOLD
        )
        rows.append(
            {
                "dimension": dimension,
                "point_difference": float(
                    dimension_splits["point_difference"].iloc[0]
                ),
                "mean_naive_ci_width": naive_width,
                "mean_clustered_ci_width": clustered_width,
                "clustered_to_naive_width_ratio": clustered_width / naive_width,
                "most_influential_owner_alias": most_influential[
                    "omitted_owner_alias"
                ],
                "max_absolute_leave_one_owner_out_shift": float(
                    most_influential["absolute_shift"]
                ),
                "max_relative_leave_one_owner_out_shift": max_relative_shift,
                "leave_one_owner_out_sign_flips": sign_flips,
                "sensitivity_flag": (
                    "review_owner_sensitivity"
                    if requires_review
                    else "stable_for_bounded_description"
                ),
            }
        )

    result = pd.DataFrame(rows)
    result.to_csv(
        OUTPUT_SUMMARY,
        index=False,
        float_format="%.6f",
        lineterminator="\n",
    )
    return result


def run_audit() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
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

    dimensions = list(analysis["dimensions"])
    rows: list[dict[str, float | int | str]] = []
    for seed in analysis["seeds"]:
        for dimension in dimensions:
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

    splits = pd.DataFrame(rows)
    splits.to_csv(
        OUTPUT_SPLITS,
        index=False,
        float_format="%.6f",
        lineterminator="\n",
    )
    influence = owner_influence(
        peru=peru,
        benchmark=benchmark,
        dimensions=dimensions,
        cluster_column=analysis["peru_cluster_column"],
    )
    summary = build_summary(splits, influence)
    return splits, influence, summary


def readable_dimension(series: pd.Series) -> pd.Series:
    return (
        series.str.replace("_observed", "", regex=False)
        .str.replace("_", " ", regex=False)
        .str.title()
    )


def write_chart(summary: pd.DataFrame) -> None:
    labels = readable_dimension(summary["dimension"])
    positions = np.arange(len(summary))
    width = 0.34

    figure, axes = plt.subplots(1, 2, figsize=(15, 7))
    figure.patch.set_facecolor("#F7F3EA")
    for axis in axes:
        axis.set_facecolor("#F7F3EA")
        axis.spines[["top", "right"]].set_visible(False)
        axis.grid(axis="y", color="#D8D0C2", linewidth=0.8)
        axis.set_axisbelow(True)

    axes[0].bar(
        positions - width / 2,
        summary["mean_naive_ci_width"],
        width,
        label="Naive row bootstrap",
        color="#A3A3A3",
    )
    axes[0].bar(
        positions + width / 2,
        summary["mean_clustered_ci_width"],
        width,
        label="Owner-clustered bootstrap",
        color="#7A1831",
    )
    axes[0].set_xticks(positions, labels, rotation=18, ha="right")
    axes[0].set_ylabel("Mean 95% interval width across four seeds")
    axes[0].set_title("A. Dependence correction", loc="left", weight="bold")
    axes[0].legend(frameon=False, loc="upper right")

    axes[1].bar(
        positions,
        summary["max_relative_leave_one_owner_out_shift"],
        color="#C49A45",
    )
    axes[1].axhline(
        RELATIVE_SHIFT_REVIEW_THRESHOLD,
        color="#7A1831",
        linestyle=":",
        linewidth=2,
        label="Project review threshold (25%)",
    )
    axes[1].set_xticks(positions, labels, rotation=18, ha="right")
    axes[1].set_ylabel("Largest relative point-estimate shift")
    axes[1].set_title("B. Leave-one-owner-out sensitivity", loc="left", weight="bold")
    axes[1].legend(frameon=False, loc="upper right")

    figure.suptitle(
        "Bias audit of the public repository benchmark",
        x=0.06,
        ha="left",
        fontsize=18,
        weight="bold",
    )
    figure.text(
        0.01,
        0.01,
        "Descriptive observability benchmark. The 25% flag is a review trigger, not a fairness standard.",
        color="#554E45",
        fontsize=9,
    )
    figure.tight_layout(rect=(0, 0.04, 1, 0.94))
    figure.savefig(OUTPUT_CHART, dpi=120)
    plt.close(figure)


def main() -> None:
    splits, influence, summary = run_audit()
    write_chart(summary)
    print(
        f"Wrote {len(splits)} interval rows, {len(influence)} owner diagnostics, "
        f"and {len(summary)} summary rows."
    )


if __name__ == "__main__":
    main()
