# Repository guide

## Layout

```
src/rsvd.py                  randomized SVD implementation
experiments/exp_synthetic.py benchmark on synthetic matrices
results/                     generated figures and tables
paper/                       paper (PDF)
requirements.txt             dependencies
```

`results/` is produced by the scripts in `experiments/` and should not be edited by hand.

## Algorithm

`rsvd(A, k, p, q)` computes a rank-`k` approximation of `A`:

1. Sample the range of `A` with a Gaussian matrix of `k + p` columns and orthonormalize (QR).
2. Optionally refine with `q` power iterations.
3. Compute the SVD of the projected matrix `Qᵀ A` and lift it back with `Q`.

## Setup

```bash
git clone https://github.com/kyoxxa/rsvd-lowrank.git
cd rsvd-lowrank
python -m venv .venv
source .venv/Scripts/activate   # Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
python -m experiments.exp_synthetic
```
