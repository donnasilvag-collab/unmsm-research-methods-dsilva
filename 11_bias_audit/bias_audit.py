"""Create reproducible audit artifacts for the public repository benchmark.

The benchmark is descriptive. This script validates and exports its observed
stratum differences; it does not calculate person-level fairness metrics.
"""

from __future__ import annotations

import csv
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "05_pipeline" / "results" / "benchmark_summary_seed_42.csv"
OUTPUT_CSV = Path(__file__).with_name("bias_audit_splits.csv")
OUTPUT_CHART = Path(__file__).with_name("before_after_chart.png")
REQUIRED_COLUMNS = {
    "dimension",
    "peru_repository_mean",
    "benchmark_repository_mean",
    "difference_peru_minus_benchmark",
    "bootstrap_ci_95_lower",
    "bootstrap_ci_95_upper",
}


def load_rows() -> list[dict[str, str]]:
    with SOURCE.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    if len(rows) != 4:
        raise ValueError(f"Expected four observed dimensions; found {len(rows)}.")
    if not REQUIRED_COLUMNS.issubset(rows[0]):
        raise ValueError("The benchmark summary is missing required audit columns.")
    return rows


def write_csv(rows: list[dict[str, str]]) -> None:
    fields = [
        "dimension",
        "peru_repository_mean",
        "benchmark_repository_mean",
        "difference_peru_minus_benchmark",
        "bootstrap_ci_95_lower",
        "bootstrap_ci_95_upper",
        "interpretation_limit",
    ]
    with OUTPUT_CSV.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow(
                {
                    **{field: row[field] for field in fields[:-1]},
                    "interpretation_limit": (
                        "Public observability proxy; not a measure of an "
                        "organization's internal control."
                    ),
                }
            )


def write_chart(rows: list[dict[str, str]]) -> None:
    labels = [row["dimension"].replace("_observed", "").replace("_", " ") for row in rows]
    peru = [float(row["peru_repository_mean"]) for row in rows]
    benchmark = [float(row["benchmark_repository_mean"]) for row in rows]

    image = Image.new("RGB", (1200, 700), "white")
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    title_font = ImageFont.truetype("arial.ttf", 22)
    left, top, right, bottom = 95, 115, 1140, 555
    plot_height = bottom - top
    peru_color = "#2E74B5"
    benchmark_color = "#C97A30"

    draw.text((95, 38), "Public repository observability by stratum", fill="#0B2545", font=title_font)
    draw.text((95, 68), "Observed composite score (0 to 10); descriptive benchmark only", fill="#3B4A5A", font=font)

    for value in range(0, 11, 2):
        y = bottom - (value / 10) * plot_height
        draw.line((left, y, right, y), fill="#D8E0E8", width=1)
        draw.text((55, y - 5), str(value), fill="#3B4A5A", font=font)

    draw.line((left, top, left, bottom), fill="#1E2D3D", width=2)
    draw.line((left, bottom, right, bottom), fill="#1E2D3D", width=2)

    group_width = (right - left) / len(rows)
    bar_width = 58
    for index, (label, peru_value, benchmark_value) in enumerate(zip(labels, peru, benchmark)):
        center = left + group_width * (index + 0.5)
        peru_top = bottom - (peru_value / 10) * plot_height
        benchmark_top = bottom - (benchmark_value / 10) * plot_height
        draw.rectangle((center - bar_width - 5, peru_top, center - 5, bottom), fill=peru_color)
        draw.rectangle((center + 5, benchmark_top, center + bar_width + 5, bottom), fill=benchmark_color)
        draw.text((center - bar_width - 5, peru_top - 16), f"{peru_value:.2f}", fill=peru_color, font=font)
        draw.text((center + 5, benchmark_top - 16), f"{benchmark_value:.2f}", fill=benchmark_color, font=font)

        words = label.split()
        midpoint = max(1, len(words) // 2)
        first_line = " ".join(words[:midpoint])
        second_line = " ".join(words[midpoint:])
        draw.text((center - 55, bottom + 16), first_line, fill="#1E2D3D", font=font)
        draw.text((center - 55, bottom + 31), second_line, fill="#1E2D3D", font=font)

    draw.rectangle((830, 75, 846, 91), fill=peru_color)
    draw.text((854, 77), "Peru stratum", fill="#1E2D3D", font=font)
    draw.rectangle((990, 75, 1006, 91), fill=benchmark_color)
    draw.text((1014, 77), "International benchmark", fill="#1E2D3D", font=font)
    image.save(OUTPUT_CHART)


def main() -> None:
    rows = load_rows()
    write_csv(rows)
    write_chart(rows)
    print(f"Wrote {OUTPUT_CSV.name} and {OUTPUT_CHART.name} from {SOURCE.name}.")


if __name__ == "__main__":
    main()
