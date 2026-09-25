# Exercise 1: N-grams
# This program generates trigrams from the given text.

import nltk
from nltk import ngrams

# Download required tokenizer resources
nltk.download("punkt")
nltk.download("punkt_tab")

# Sample text from the exercise
text = "Natural Language Processing with Python"

# Tokenize the text into words
tokens = nltk.word_tokenize(text)

# Generate trigrams
trigrams = list(ngrams(tokens, 3))

# Display the trigrams
print("Trigrams:")
for trigram in trigrams:
    print(trigram)