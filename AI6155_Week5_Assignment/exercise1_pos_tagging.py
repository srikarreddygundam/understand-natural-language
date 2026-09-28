# Exercise 1: Parts of Speech (POS) Tagging
# This program performs POS tagging on a sample sentence.

import nltk
from nltk import word_tokenize, pos_tag

# Download required NLTK resources
nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("averaged_perceptron_tagger")
nltk.download("averaged_perceptron_tagger_eng")

# Sample text from the exercise
text = "The quick brown fox jumps over the lazy dog."

# Tokenize the text into words
tokens = word_tokenize(text)

# Perform POS tagging
pos_tags = pos_tag(tokens)

# Display the result
print("POS Tags:")
print(pos_tags)