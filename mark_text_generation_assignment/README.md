# 🍏🍌 **The Unigram Model: Apples vs. Bananas Showdown** 🍌🍏

The files within the folder presents my analysis of a unigram model applied to a simple vocabulary of **Apples** and **Bananas**. 🥊 I have completed the tasks of proving the optimality of probabilities and visualizing the results.

---

## 📚 **The Mission**
The goal of this assignment was to:
1. 🧠 **Prove** that the given probability $p$ (based on word frequency) is optimal.
2. 📈 **Plot** the probability of observations as a function of $p_\text{apple}$ to analyze the relationship.

---

## 🍏 **The Setup**

The vocabulary consisted of two tokens:
- 🍎 **Apples**: Appeared 6 times.
- 🍌 **Bananas**: Appeared 4 times.

The observations were as follows:

```python
["apple", "apple", "apple", "apple", "apple", "apple",
 "banana", "banana", "banana", "banana"]
