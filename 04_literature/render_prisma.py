"""Render the PRISMA PNG from the machine-readable flow counts."""

from __future__ import annotations

import csv
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


HERE = Path(__file__).resolve().parent
FLOW = HERE / "prisma_flow.csv"
OUTPUT = HERE / "prisma_diagram.png"
BURGUNDY = "#7A1831"
CREAM = "#F7F3EA"
INK = "#24211D"
MUTED = "#5B534A"
EXCLUDE = "#EFE7DD"


def load_counts() -> dict[str, int]:
    with FLOW.open(encoding="utf-8", newline="") as handle:
        return {row["phase"]: int(row["count"]) for row in csv.DictReader(handle)}


def add_box(
    axis: plt.Axes,
    center_x: float,
    center_y: float,
    width: float,
    height: float,
    lines: list[str],
    *,
    included: bool = False,
    excluded: bool = False,
) -> None:
    face = BURGUNDY if included else EXCLUDE if excluded else "#FFFFFF"
    edge = BURGUNDY if not excluded else "#6C655E"
    color = "#FFFFFF" if included else INK
    patch = FancyBboxPatch(
        (center_x - width / 2, center_y - height / 2),
        width,
        height,
        boxstyle="round,pad=0.03,rounding_size=0.12",
        facecolor=face,
        edgecolor=edge,
        linewidth=2.5,
    )
    axis.add_patch(patch)
    line_gap = 0.32
    start_y = center_y + line_gap * (len(lines) - 1) / 2
    for index, line in enumerate(lines):
        axis.text(
            center_x,
            start_y - index * line_gap,
            line,
            ha="center",
            va="center",
            color=color,
            fontsize=15 if not excluded else 12.5,
            fontweight="bold" if included else "normal",
            family="DejaVu Serif",
        )


def arrow(
    axis: plt.Axes,
    start: tuple[float, float],
    end: tuple[float, float],
    *,
    muted: bool = False,
) -> None:
    axis.add_patch(
        FancyArrowPatch(
            start,
            end,
            arrowstyle="-|>",
            mutation_scale=16,
            linewidth=2.3,
            color="#6C655E" if muted else BURGUNDY,
            connectionstyle="arc3,rad=0",
        )
    )


def main() -> None:
    counts = load_counts()
    if counts["primary_source_records"] + counts["additional_records"] != counts["total_identified"]:
        raise ValueError("Identification counts do not add to the total.")
    if counts["full_text_assessed"] - counts["full_text_excluded"] != counts["included_qualitative_synthesis"]:
        raise ValueError("Full-text counts do not add to the included total.")

    figure, axis = plt.subplots(figsize=(16, 11))
    figure.patch.set_facecolor(CREAM)
    axis.set_facecolor(CREAM)
    axis.set_xlim(0, 16)
    axis.set_ylim(0, 11)
    axis.axis("off")
    axis.axvspan(0, 0.22, color=BURGUNDY)

    axis.text(0.85, 10.35, "PRISMA 2020 flow", fontsize=28, fontweight="bold", color=INK, family="DejaVu Serif")
    axis.text(0.85, 9.98, "Preliminary systematic review, validated 8 August 2026", fontsize=15, color=MUTED, family="DejaVu Serif")
    axis.text(0.9, 8.95, "IDENTIFICATION", fontsize=14, fontweight="bold", color=BURGUNDY, family="DejaVu Serif")
    axis.text(0.9, 5.6, "SCREENING", fontsize=14, fontweight="bold", color=BURGUNDY, family="DejaVu Serif")
    axis.text(0.9, 2.1, "INCLUDED", fontsize=14, fontweight="bold", color=BURGUNDY, family="DejaVu Serif")

    add_box(axis, 6.0, 8.75, 4.7, 1.0, ["Primary-source records", f"n = {counts['primary_source_records']}"])
    add_box(axis, 12.0, 8.75, 4.7, 1.15, ["Reference tracking and", "local corpus", f"n = {counts['additional_records']}"])
    add_box(axis, 8.8, 7.15, 4.8, 0.95, ["Total records identified", f"n = {counts['total_identified']}"])
    add_box(axis, 8.8, 5.5, 4.8, 0.95, ["Records screened after", f"deduplication: n = {counts['title_abstract_screened']}"])
    add_box(axis, 13.5, 5.5, 3.8, 1.05, ["Duplicates or redundant", f"versions removed: n = {counts['duplicates_removed']}"], excluded=True)
    add_box(axis, 8.8, 3.85, 4.8, 0.95, ["Full texts assessed", f"n = {counts['full_text_assessed']}"])
    add_box(axis, 3.1, 3.85, 3.9, 1.05, ["Title and abstract records", f"excluded: n = {counts['title_abstract_excluded']}"], excluded=True)
    add_box(axis, 13.5, 3.85, 3.8, 1.05, ["Full texts excluded with", f"recorded reasons: n = {counts['full_text_excluded']}"], excluded=True)
    add_box(axis, 8.8, 1.9, 4.8, 1.15, ["Studies included in", f"qualitative synthesis: n = {counts['included_qualitative_synthesis']}"], included=True)

    arrow(axis, (6.0, 8.22), (8.25, 7.68))
    arrow(axis, (12.0, 8.22), (9.35, 7.68))
    arrow(axis, (8.8, 6.66), (8.8, 5.99))
    arrow(axis, (11.22, 5.5), (11.58, 5.5), muted=True)
    arrow(axis, (8.8, 5.01), (8.8, 4.34))
    arrow(axis, (6.38, 3.85), (5.08, 3.85), muted=True)
    arrow(axis, (11.22, 3.85), (11.58, 3.85), muted=True)
    arrow(axis, (8.8, 3.36), (8.8, 2.5))

    axis.text(0.85, 0.68, "Course-stage review. Full-text decisions and DOI checks are recorded in screening_log.csv.", fontsize=11, color=MUTED, family="DejaVu Serif")
    axis.text(0.85, 0.35, "The complete 43-record database export was not retained and must be recreated for the thesis review.", fontsize=11, color=MUTED, family="DejaVu Serif")
    figure.savefig(OUTPUT, dpi=100, facecolor=figure.get_facecolor())
    plt.close(figure)
    print(f"Wrote {OUTPUT.name} from {FLOW.name}.")


if __name__ == "__main__":
    main()
