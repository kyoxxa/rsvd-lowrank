# How to navigate this repo

This file explains what lives where in `rsvd-lowrank` and how to contribute.

## The big picture

```
src/  →  experiments/  →  results/  →  paper/
(algorithm)  (tests)     (plots, tables)  (LaTeX)
```

`src/` holds the algorithm, `experiments/` runs it, `results/` stores what comes out, and that goes into the paper.

## What is where

```
rsvd-lowrank/
├── src/                     # the algorithm
│   ├── rsvd.py              # randomized SVD (edit only after agreeing)
│   └── __init__.py          # makes src importable, don't touch
├── experiments/             # scripts that test the algorithm
│   ├── exp_synthetic.py     # error and speed on generated matrices
│   └── exp_sir.py           # SIR epidemic application (coming)
├── results/                 # created by the scripts, never edit by hand
│   ├── figures/             # plots for the paper
│   └── tables/              # CSV results
├── paper/                   # LaTeX source of the paper
├── README.md                # front page of the repo
├── HOW_TO_NAVIGATE.md       # this guide
├── requirements.txt         # libraries + versions
└── .gitignore               # files git must not upload
```

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
