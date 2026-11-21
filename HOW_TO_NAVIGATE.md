# How to navigate this repo

This file explains what lives where in `rsvd-lowrank` and how to contribute.

## The big picture

```
src/  →  experiments/  →  results/  →  paper/
(algorithm)  (tests)     (plots, tables)  (LaTeX)
```

`src/` holds the algorithm, `experiments/` runs it, `results/` stores what comes out, and that goes into the paper.

## What is where

| Path | What it is | Edit it? |
| --- | --- | --- |
| `src/rsvd.py` | The randomized SVD algorithm (about 15 lines) | Only after agreeing |
| `src/__init__.py` | Empty file that makes `src` importable | No |
| `experiments/exp_synthetic.py` | Benchmark on generated matrices: error and speed vs. rank | Yes, via branch |
| `experiments/exp_sir.py` | SIR epidemic application (coming) | Yes, via branch |
| `results/figures/` | Plots made by the scripts | Never by hand |
| `results/tables/` | CSV tables made by the scripts | Never by hand |
| `paper/` | LaTeX source of the paper | Yes |
| `README.md` | Front page of the repo | Yes |
| `requirements.txt` | Library list with exact versions | Only when adding a library |
| `.gitignore` | Files git must not upload (like `.venv/`) | Rarely |

## How `rsvd.py` works

1. Multiply the matrix `A` by a small random matrix to sample its most important directions.
2. Orthonormalize the result with a QR decomposition to get a basis `Q`. With power iterations, repeat this `q` times for more accuracy.
3. Compute the SVD of the small matrix `Qᵀ A` and map it back with `Q`.

Parameters: `k` = target rank, `p` = oversampling (extra random directions), `q` = power iterations.

## One-time setup

```bash
git clone https://github.com/kyoxxa/rsvd-lowrank.git
cd rsvd-lowrank
python -m venv .venv
source .venv/Scripts/activate      # Mac/Linux: source .venv/bin/activate
pip install -r requirements.txt
git config --global user.name "your-github-username"
git config --global user.email "your GitHub no-reply email"
python -m experiments.exp_synthetic  # check that everything runs
```

## How to contribute

1. Get the latest version: `git checkout main` then `git pull`
2. Make a branch for your task: `git checkout -b my-task-name`
3. Work, then save: `git add .` and `git commit -m "Short description"`
4. Upload: `git push -u origin my-task-name`
5. On GitHub, click **Compare & pull request**. The other person reviews and clicks **Merge**.

## Rules

- Never push straight to `main`. Always branch + pull request.
- One person per file at a time, to avoid conflicts.
- Commit messages say what changed.
- Every figure and table must come from a script in `experiments/`, with fixed random seeds.
