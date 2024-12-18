"""Markov Text Generator.

Eric Ortega Rodriguez, 2024

"""
# Importing all libraries needed for code to run 
import csv
import nltk

import collections
import nltk.tokenize 
import word_tokenize
nltk.download('punkt')

from mtg import finish_sentence

# Defining our corpus as a string 


# Incorporating the test generator
def test_generator():
    """Test Markov text generator."""
    corpus = tuple(
        nltk.word_tokenize(nltk.corpus.gutenberg.raw("austen-sense.txt").lower())
    )

    with open("test_examples.csv") as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=",")
        for row in csvreader:
            words = finish_sentence(
                row["input"].split(" "),
                int(row["n"]),
                corpus,
                randomize=False,
            )
            print(f"input: {row['input']} (n={row['n']})")
            print(f"output: {' '.join(words)}")
            assert words == row["output"].split(" ")


if __name__ == "__main__":
    test_generator()
