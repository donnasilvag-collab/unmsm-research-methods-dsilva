"""Execute the four-seed public benchmark and record each run in MLflow."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import mlflow
import pandas as pd
import yaml


ROOT = Path(__file__).resolve().parents[1]


def make_plot(summary: pd.DataFrame, destination: Path) -> None:
    latest = summary.loc[summary["seed"] == summary["seed"].max()].copy()
    labels = latest["dimension"].str.replace("_observed", "").str.replace("_", " ").str.title()
    values = latest["difference_peru_minus_benchmark"]
    lower_errors = values - latest["bootstrap_ci_95_lower"]
    upper_errors = latest["bootstrap_ci_95_upper"] - values

    figure, axis = plt.subplots(figsize=(10, 5))
    axis.bar(labels, values, color="#1f5f7a")
    axis.errorbar(labels, values, yerr=[lower_errors, upper_errors], fmt="none", color="#17212b", capsize=5)
    axis.axhline(0, color="#6b7280", linewidth=1)
    axis.set_ylabel("Peru minus benchmark observed score")
    axis.set_title("Public repository benchmark: latest clustered-bootstrap run")
    axis.tick_params(axis="x", rotation=18)
    figure.tight_layout()
    destination.parent.mkdir(parents=True, exist_ok=True)
    figure.savefig(destination, dpi=180)
    plt.close(figure)


def main() -> None:
    params = yaml.safe_load((ROOT / "params.yaml").read_text(encoding="utf-8"))
    analysis = params["analysis"]
    results_dir = ROOT / "results"
    results_dir.mkdir(exist_ok=True)

    tracking_uri = (ROOT / "mlruns").resolve().as_uri()
    mlflow.set_tracking_uri(tracking_uri)
    mlflow.set_experiment("public-security-repository-benchmark")

    run_outputs: list[pd.DataFrame] = []
    for seed in analysis["seeds"]:
        output = results_dir / f"benchmark_summary_seed_{seed}.csv"
        command = [
            sys.executable,
            str(ROOT / "src" / "train.py"),
            "--input",
            str(ROOT / params["dataset"]["output_csv"]),
            "--params",
            str(ROOT / "params.yaml"),
            "--output",
            str(output),
            "--seed",
            str(seed),
        ]
        subprocess.run(command, check=True, cwd=ROOT)
        result = pd.read_csv(output)
        run_outputs.append(result)

        with mlflow.start_run(run_name=f"clustered-bootstrap-seed-{seed}"):
            mlflow.log_params(
                {
                    "seed": seed,
                    "bootstrap_iterations": analysis["bootstrap_iterations"],
                    "analysis_unit": analysis["unit_of_analysis"],
                    "peru_cluster_column": analysis["peru_cluster_column"],
                    "scope": "public_repository_descriptive_benchmark",
                }
            )
            for row in result.itertuples(index=False):
                prefix = row.dimension.replace("_observed", "")
                mlflow.log_metrics(
                    {
                        f"{prefix}_peru_mean": row.peru_repository_mean,
                        f"{prefix}_benchmark_mean": row.benchmark_repository_mean,
                        f"{prefix}_difference": row.difference_peru_minus_benchmark,
                        f"{prefix}_ci_lower": row.bootstrap_ci_95_lower,
                        f"{prefix}_ci_upper": row.bootstrap_ci_95_upper,
                    }
                )
            mlflow.log_artifact(str(output), artifact_path="results")

    summary = pd.concat(run_outputs, ignore_index=True)
    summary.to_csv(results_dir / "seed_stability.csv", index=False, float_format="%.6f")
    make_plot(summary, ROOT / "docs" / "mlflow_runs.png")
    print("Completed four seeded MLflow runs.")


if __name__ == "__main__":
    main()
