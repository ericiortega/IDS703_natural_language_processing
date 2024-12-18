# Unigram Model Assignment

## Overview
This assignment involves working with a unigram model to optimize probabilities and analyze observations. Specifically, the tasks are:

1. **Prove that the probability vector `p` is optimal** (red task).
2. **Plot the probability of the observations under the unigram model** as a function of `p_apple` (blue task).

---

## Tasks
### 1. Proof of Optimality (Red)
- Prove that the vector `p` with components \( p_k = \frac{n_k}{\sum_k n_k} \) maximizes the probability of the observed set.

### 2. Plot Probability Function (Blue)
- Use **matplotlib** to plot the probability of the observations as a function of \( p_{apple} \), where \( p_{banana} = 1 - p_{apple} \).
- Use only `numpy` and the Python **standard library** for computations.

---

## Input Data
The vocabulary \( V \) and observations are as follows:
- **Vocabulary**: `{"apple", "banana"}`
- **Observations**: `["apple", "apple", "apple", "apple", "apple", "apple", "banana", "banana", "banana", "banana"]`

---

## Deliverables
- **Document** (.txt, .md, or .pdf): Contains the proof of optimality (red task).
- **Python Script** (.py): Implements and plots the probability function (blue task).

---

## Requirements
- Libraries allowed: `numpy`, `matplotlib`, and Python **standard library** only.
- Clearly document your code and steps.
