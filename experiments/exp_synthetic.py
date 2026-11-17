"""Experiment 1: randomized SVD vs. exact truncated SVD on synthetic matrices.

Run from the repo root:  python -m experiments.exp_synthetic
"""
import time
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.utils.extmath import randomized_svd

from src.rsvd import rsvd

OUT_FIG = Path("results/figures")
OUT_TAB = Path("results/tables")
OUT_FIG.mkdir(parents=True, exist_ok=True)
OUT_TAB.mkdir(parents=True, exist_ok=True)


def make_matrix(m, n, decay="fast", seed=0):
    """Random matrix with a chosen singular value decay."""
    rng = np.random.default_rng(seed)
    r = min(m, n)
    U, _ = np.linalg.qr(rng.standard_normal((m, r)))
    V, _ = np.linalg.qr(rng.standard_normal((n, r)))
    i = np.arange(r)
    s = np.exp(-i / 10) if decay == "fast" else 1.0 / (i + 1)  # exponential vs. slow (1/i)
    return (U * s) @ V.T


def rel_error(A, U, s, Vt):
    return np.linalg.norm(A - (U * s) @ Vt) / np.linalg.norm(A)


def main():
    m, n = 2000, 1000
    ranks = [5, 10, 20, 50, 100]
    rows = []

    for decay in ["fast", "slow"]:
        A = make_matrix(m, n, decay)
        t0 = time.perf_counter()
        Uf, sf, Vtf = np.linalg.svd(A, full_matrices=False)
        t_full = time.perf_counter() - t0

        for k in ranks:
            err_opt = rel_error(A, Uf[:, :k], sf[:k], Vtf[:k])  # best possible (Eckart-Young)
            for q in [0, 1, 2]:
                t0 = time.perf_counter()
                U, s, Vt = rsvd(A, k, p=10, q=q, seed=42)
                t = time.perf_counter() - t0
                rows.append(dict(decay=decay, k=k, method=f"rsvd q={q}",
                                 rel_err=rel_error(A, U, s, Vt), opt_err=err_opt,
                                 time_s=t, speedup=t_full / t))

            t0 = time.perf_counter()
            U, s, Vt = randomized_svd(A, k, n_oversamples=10, n_iter=2, random_state=42)
            t = time.perf_counter() - t0
            rows.append(dict(decay=decay, k=k, method="sklearn", rel_err=rel_error(A, U, s, Vt),
                             opt_err=err_opt, time_s=t, speedup=t_full / t))

    df = pd.DataFrame(rows)
    df.to_csv(OUT_TAB / "synthetic.csv", index=False)
    print(df.round(4).to_string(index=False))

    fig, axes = plt.subplots(1, 2, figsize=(10, 4), sharey=False)
    for ax, decay in zip(axes, ["fast", "slow"]):
        d = df[df.decay == decay]
        opt = d.drop_duplicates("k")
        ax.semilogy(opt.k, opt.opt_err, "k--", label="exact SVD (optimal)")
        for method, g in d.groupby("method"):
            ax.semilogy(g.k, g.rel_err, "o-", label=method)
        ax.set_title(f"{decay} singular value decay")
        ax.set_xlabel("rank k")
        ax.set_ylabel("relative Frobenius error")
        ax.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(OUT_FIG / "synthetic_error_vs_rank.png", dpi=200)
    print(f"\nSaved figure and table to {OUT_FIG} and {OUT_TAB}")


if __name__ == "__main__":
    main()
