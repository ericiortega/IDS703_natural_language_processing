import numpy as np
import matplotlib.pyplot as plt

## Eric Ortega Rodriguez
## Natural Language Processing | ECE 684.01.Fa24
## Assignment #1: The Unigram Model

# Observations per word
num_apple = 6
num_ban = 4

# Looking at x axis (apple probability)
prob_apple = np.linspace(0, 1, 1000)
prob_ban = 1 - prob_apple

accuracy = (prob_apple**num_apple) * (prob_ban**num_ban)

# Plotting
plt.plot(prob_apple, accuracy)
plt.xlabel("Probability of Apple")
plt.ylabel("Optimized Accuracy")
plt.title("Accuracy and Probability")
plt.show()
