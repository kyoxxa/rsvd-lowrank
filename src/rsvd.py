"""Randomized SVD (Halko, Martinsson & Tropp, 2011)."""
import numpy as np


def rsvd(A, k, p=10, q=2, seed=None):
    """Rank-k approximation A ~ U @ diag(s) @ Vt.

    Parameters
    ----------
    A    : (m, n) array
    k    : target rank
    p    : oversampling (extra random directions, usually 5-10)
    q    : power iterations (helps when singular values decay slowly)
    seed : random seed for reproducibility
    """
    rng = np.random.default_rng(seed)
    m, n = A.shape
    l = min(k + p, m, n)

    # Stage A: find an orthonormal basis Q for the range of A
    Omega = rng.standard_normal((n, l))      # random test matrix
    Q, _ = np.linalg.qr(A @ Omega)           # sample the range of A
    for _ in range(q):                       # power iterations (re-orthonormalize each time for stability)
        Z, _ = np.linalg.qr(A.T @ Q)
        Q, _ = np.linalg.qr(A @ Z)

    # Stage B: SVD of the small matrix B = Q^T A  (size l x n)
    B = Q.T @ A
    Ub, s, Vt = np.linalg.svd(B, full_matrices=False)
    U = Q @ Ub

    return U[:, :k], s[:k], Vt[:k, :]
