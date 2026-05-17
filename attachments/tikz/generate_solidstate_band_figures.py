#!/usr/bin/env python3
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


OUT = Path(__file__).resolve().parent
PI = np.pi

plt.rcParams.update(
    {
        "figure.dpi": 150,
        "savefig.dpi": 300,
        "font.family": "serif",
        "font.size": 7.3,
        "mathtext.fontset": "cm",
        "axes.linewidth": 0.38,
        "xtick.major.width": 0.34,
        "ytick.major.width": 0.34,
        "xtick.major.size": 1.8,
        "ytick.major.size": 1.8,
    }
)


def nearly_free_bands(q_values, harmonics=4):
    """Plane-wave diagonalization for V(x)=2 sum_r V_r cos(r G x)."""
    ns = np.arange(-harmonics, harmonics + 1)
    G = 2 * PI
    couplings = {1: 0.18, 2: 0.055, 3: 0.022}
    bands = []
    for q in q_values:
        diag = 0.048 * (q + ns * G) ** 2
        H = np.diag(diag)
        for r, value in couplings.items():
            for i, ni in enumerate(ns):
                for j, nj in enumerate(ns):
                    if abs(ni - nj) == r:
                        H[i, j] += value
        bands.append(np.linalg.eigvalsh(H)[:5])
    bands = np.asarray(bands)
    return bands - bands[:, 0].min()


def style_axes(ax, xlabel=True):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("0.20")
    ax.spines["bottom"].set_color("0.20")
    ax.tick_params(colors="0.18", labelsize=6.9, pad=1.5)
    ax.set_yticks([])
    ax.set_ylabel(r"$E$", rotation=0, labelpad=4, fontsize=8)
    if xlabel:
        ax.set_xlabel(r"$k$", labelpad=1, fontsize=8)


def reduced_data():
    q = np.linspace(-PI, PI, 520)
    bands = nearly_free_bands(q)
    return q, bands


def extended_branch(k, q, bands, band_index):
    q_fold = ((k + PI) % (2 * PI)) - PI
    order = np.argsort(q)
    return np.interp(q_fold, q[order], bands[order, band_index])


def draw_extended():
    q, bands = reduced_data()
    fig, ax = plt.subplots(figsize=(4.95, 2.30), constrained_layout=True)
    colors = ["#2f5aa6", "#2a776e", "#7a4a8f"]

    ax.axvspan(-1, 1, color="0.965", zorder=0)
    for n in range(-3, 4):
        ax.axvline(n, color="0.76", lw=0.24, ls=(0, (4, 3)), zorder=0)

    # Faint free-electron parabolas show where the avoided crossings came from.
    kref = np.linspace(-3.0, 3.0, 800)
    for m in range(-3, 4):
        y = 0.048 * (PI * kref + 2 * PI * m) ** 2
        ax.plot(kref, y, color="0.80", lw=0.20, ls=(0, (2, 3)), alpha=0.52, zorder=0)

    segments = [
        (-PI, PI, 0),
        (PI, 2 * PI, 1),
        (-2 * PI, -PI, 1),
        (2 * PI, 3 * PI, 2),
        (-3 * PI, -2 * PI, 2),
    ]
    for lo, hi, idx in segments:
        k = np.linspace(lo, hi, 260)
        y = extended_branch(k, q, bands, idx)
        ax.plot(k / PI, y, lw=0.52, color=colors[idx], solid_capstyle="round")

    for x, i, dy in [(1, 0, 0.12), (2, 1, 0.17), (3, 2, 0.18)]:
        low = extended_branch(np.array([x * PI - 1e-4]), q, bands, i)[0]
        high = extended_branch(np.array([x * PI + 1e-4]), q, bands, i + 1)[0]
        ax.annotate(
            "",
            xy=(x, high),
            xytext=(x, low),
            arrowprops=dict(arrowstyle="<->", lw=0.34, color="0.25", shrinkA=0, shrinkB=0),
        )
        ax.text(x + 0.06, (low + high) / 2 + dy, rf"$2|V_{i+1}|$", fontsize=6.2, va="center", color="0.20")

    ax.set_xlim(-3.08, 3.08)
    ax.set_ylim(-0.06, 4.75)
    ax.set_xticks(range(-3, 4))
    ax.set_xticklabels(
        [r"$-3\pi/a$", r"$-2\pi/a$", r"$-\pi/a$", r"$0$", r"$\pi/a$", r"$2\pi/a$", r"$3\pi/a$"]
    )
    ax.text(0, -0.43, "1st Brillouin zone", ha="center", va="top", fontsize=5.7)
    ax.text(1.5, -0.43, "2nd", ha="center", va="top", fontsize=5.6)
    ax.text(2.5, -0.43, "3rd", ha="center", va="top", fontsize=5.6)
    ax.text(-1.5, -0.43, "2nd", ha="center", va="top", fontsize=5.6)
    ax.text(-2.5, -0.43, "3rd", ha="center", va="top", fontsize=5.6)
    ax.text(3.12, -0.03, r"$k$", ha="left", va="top", fontsize=8)
    style_axes(ax, xlabel=False)
    fig.savefig(OUT / "solidstate-nearly-free-band-extended.png", transparent=True)
    plt.close(fig)


def draw_zone_schemes():
    q, bands = reduced_data()
    colors = ["#2f5aa6", "#2a776e", "#7a4a8f"]
    fig, axes = plt.subplots(
        1,
        2,
        figsize=(6.3, 2.55),
        width_ratios=[3.0, 1.0],
        constrained_layout=True,
    )

    ax = axes[0]
    ax.set_title("extended-zone scheme", loc="left", fontsize=7.8, pad=2)
    for n in range(-3, 4):
        ax.axvline(n, color="0.76", lw=0.24, ls=(0, (4, 3)), zorder=0)
    for lo, hi, idx in [
        (-PI, PI, 0),
        (PI, 2 * PI, 1),
        (-2 * PI, -PI, 1),
        (2 * PI, 3 * PI, 2),
        (-3 * PI, -2 * PI, 2),
    ]:
        k = np.linspace(lo, hi, 260)
        ax.plot(k / PI, extended_branch(k, q, bands, idx), lw=0.52, color=colors[idx], solid_capstyle="round")
    ax.set_xlim(-3.08, 3.08)
    ax.set_ylim(-0.06, 4.75)
    ax.set_xticks(range(-3, 4))
    ax.set_xticklabels(
        [r"$-3\pi/a$", r"$-2\pi/a$", r"$-\pi/a$", r"$0$", r"$\pi/a$", r"$2\pi/a$", r"$3\pi/a$"]
    )
    style_axes(ax)

    ax = axes[1]
    ax.set_title("reduced-zone scheme", loc="left", fontsize=7.8, pad=2)
    ax.axvspan(-1, 1, color="0.965", zorder=0)
    ax.axvline(-1, color="0.76", lw=0.24, ls=(0, (4, 3)), zorder=0)
    ax.axvline(1, color="0.76", lw=0.24, ls=(0, (4, 3)), zorder=0)
    for i, color in enumerate(colors):
        ax.plot(q / PI, bands[:, i], lw=0.52, color=color, solid_capstyle="round")
        label = "1st band" if i == 0 else "2nd band" if i == 1 else "3rd band"
        ax.text(1.04, bands[-1, i], label, color=color, fontsize=6.3, va="center")
    ax.set_xlim(-1.12, 1.18)
    ax.set_ylim(-0.06, 4.75)
    ax.set_xticks([-1, 0, 1])
    ax.set_xticklabels([r"$-\pi/a$", r"$0$", r"$\pi/a$"])
    style_axes(ax)
    fig.savefig(OUT / "solidstate-zone-schemes.png", transparent=True)
    plt.close(fig)


if __name__ == "__main__":
    draw_extended()
    draw_zone_schemes()
