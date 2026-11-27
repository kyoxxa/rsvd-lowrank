# rsvd-lowrank
Using randomness to approximate large matrices faster than standard SVD.
This repository contains the code for our paper Track 2: Computational Modeling, Simulation & Applied Mathematics (Numerical and approximation methods).

The idea:

A lot of data is just a big table of numbers (a matrix): an image, a ratings table, or a simulation saved over time.

Most of the information in such a table comes from a few **main patterns**. If we keep only those, we get a much smaller version that is almost as good as the original.

The classic way to find these patterns is called **SVD**. It works well, but it is **slow** for big matrices.

**Randomized SVD** is a faster shortcut:

1. Multiply the matrix by a few random numbers to get a quick "sketch" of it.
2. Find the main patterns in that small sketch instead of the full matrix.

Like a poll: instead of asking everyone, ask a random sample and still get almost the same answer.

## What we test

- How **fast** randomized SVD is compared to normal SVD.
- How **accurate** it is.
- How two settings change the result:
  - `p`: a few extra random samples as a safety margin
  - `q`: repeating the sketch step to make it more accurate
- A real use case: compressing data from an **epidemic spread simulation (SIR model)**.

## How to run

```bash
pip install -r requirements.txt
python -m experiments.exp_synthetic
```

The plots and tables are saved in the `results/` folder.

## Reference

N Halko, P G Martinsson, and J. A. Tropp, "Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions," *SIAM Review*, vol. 53, no. 2, pp. 217–288, 2011.
