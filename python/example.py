import numpy as np
import matplotlib.pyplot as plt
import sys
import os
from scipy.stats import norm, multivariate_normal
sys.path.append(os.path.dirname("/Users/alejandrosanchez/SBND/Work/Tools/"))
import sbnd_style as sbnd


# ============================================================
# Utilities
# ============================================================

def make_legend(ax, loc=(0.65, 0.6)):
    return ax.legend(frameon=False, loc="upper left",
                     bbox_to_anchor=loc)


def gauss_hists(nhists=8, nbins=100):
    hists = []
    xs = np.linspace(-10, 10, 10000)

    for i in range(nhists):
        mu = 2*i - (nhists - 1)
        data = np.random.normal(mu, 1.0, 1000*(i+1))
        hists.append(data)

    return hists


# ============================================================
# 1D histogram example
# ============================================================

def one_d_hist_example():
    fig, ax = plt.subplots()
    mc = np.random.normal(0, 1, 1000)
    data = np.random.normal(0, 1, 1000)
    bins = np.linspace(-5, 5, 21)
    # MC band
    h_mc, _, _ = ax.hist( mc, bins=bins, histtype="stepfilled", alpha=0.4, label="MC"
    )

    # MC stat band
    ax.hist( mc, bins=bins, histtype="step", linewidth=2 )

    # Data
    h_data, bin_edges = np.histogram(data, bins=bins)
    centers = 0.5*(bin_edges[1:] + bin_edges[:-1])
    ax.errorbar(
        centers, h_data,
        yerr=np.sqrt(h_data),
        fmt="o", label="Data"
    )

    ax.set_xlabel("x label")
    ax.set_ylabel("y label")
    sbnd.center_titles(ax)

    make_legend(ax)
    sbnd.sbnd_wip(ax, 0.02, 0.95, fontsize=25)

    fig.savefig("example.hist1D.png")
    plt.close(fig)


# ============================================================
# Data / MC with ratio
# ============================================================

def datamc_example():
    fig = plt.figure()
    ax1, ax2 = sbnd.split_canvas(fig, 0.3)

    data = np.random.normal(0, 1, 1000)
    bins = np.linspace(-5, 5, 51)

    counts, edges = np.histogram(data, bins=bins)
    centers = 0.5*(edges[1:] + edges[:-1])

    # Fit
    mu, sigma = norm.fit(data)
    fit_y = norm.pdf(centers, mu, sigma)
    fit_y *= counts.sum() * (edges[1] - edges[0])

    ax1.errorbar(
        centers, counts,
        yerr=np.sqrt(counts),
        fmt="o", label="Data"
    )
    ax1.plot(centers, fit_y, label="Fit")

    ax1.set_ylabel("y label")
    sbnd.center_titles(ax1)
    make_legend(ax1)

    sbnd.sbnd_preliminary(ax1, 0.02, 0.95)

    # Ratio
    ratio = (counts - fit_y) / fit_y
    ax2.axhline(0)
    ax2.errorbar(
        centers, ratio,
        yerr=np.sqrt(counts)/fit_y,
        fmt="o"
    )

    ax2.set_xlabel("x label")
    ax2.set_ylabel("(Data-Fit)/Fit")
    ax2.set_ylim(-1, 1)

    fig.savefig("example.datamc.png")
    plt.close(fig)


# ============================================================
# 2D example with contours
# ============================================================

def two_d_example():
    sbnd.apply_sea_palette()

    fig, ax = plt.subplots()

    mean = [0.5, -0.5]
    cov = [[1.0, 0.0], [0.0, 1.0]]
    data = np.random.multivariate_normal(mean, cov, 1_000_000)

    h = ax.hist2d(
        data[:, 0], data[:, 1],
        bins=[100, 120]
    )

    sbnd.sbnd_official(ax, 0.02, 0.95)

    # Contours
    levels = [0.682, 0.954, 0.997]
    X, Y = np.meshgrid(
        np.linspace(-5, 5, 200),
        np.linspace(-5, 7, 200)
    )
    pos = np.dstack((X, Y))
    pdf = multivariate_normal(mean, cov).pdf(pos)

    ax.contour(X, Y, pdf,
               levels=np.sort(pdf.max()*np.array(levels)),
               linestyles=["solid", "dotted", "dashed"])

    ax.set_xlabel("x label")
    ax.set_ylabel("y label")
    sbnd.center_titles(ax)

    fig.savefig("example.hist2D.png")
    plt.close(fig)


# ============================================================
# Covariance matrix
# ============================================================

def cov_example():
    sbnd.apply_symmetric_palette()

    fig, ax = plt.subplots()

    dim = 10
    cov = np.eye(dim)
    rng = np.random.default_rng(0)

    for i in range(dim):
        for j in range(i+1, dim):
            cov[i, j] = cov[j, i] = np.clip(rng.normal(0, 0.2), -1, 1)

    im = ax.imshow(cov, vmin=-1, vmax=1)
    fig.colorbar(im, ax=ax)

    ax.set_xlabel("index i")
    ax.set_ylabel("index j")
    sbnd.center_titles(ax)

    sbnd.sbnd_preliminary(ax, 0.02, 0.95)

    fig.savefig("example.histcov.png")
    plt.close(fig)


# ============================================================
# Stacked histograms
# ============================================================

def stacked_example():
    hists = gauss_hists()
    fig, ax = plt.subplots()

    bins = np.linspace(-10, 10, 100)

    ax.hist(
        hists, bins=bins,
        stacked=True, label=[f"Hist #{i+1}" for i in range(len(hists))]
    )

    make_legend(ax)
    sbnd.center_titles(ax)
    sbnd.sbnd_wip(ax, 0.02, 0.95)

    fig.savefig("example.histstacked.png")
    plt.close(fig)


# ============================================================
# Overlay histograms
# ============================================================

def overlay_example():
    hists = gauss_hists()
    fig, ax = plt.subplots()

    bins = np.linspace(-10, 10, 100)

    for i, h in enumerate(hists):
        ax.hist(
            h, bins=bins,
            histtype="step",
            label=f"Hist #{i+1}"
        )

    make_legend(ax)
    sbnd.center_titles(ax)
    sbnd.sbnd_wip(ax, 0.02, 0.95)

    fig.savefig("example.histoverlay.png")
    plt.close(fig)


# ============================================================
# Main
# ============================================================

if __name__ == "__main__":
    one_d_hist_example()
    datamc_example()
    two_d_example()
    cov_example()
    stacked_example()
    overlay_example()
