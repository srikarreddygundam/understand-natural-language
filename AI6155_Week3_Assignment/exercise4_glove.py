# Exercise 4: GloVe
# This program loads pretrained GloVe embeddings and displays a word vector.

import gensim.downloader as api

# Load a pretrained GloVe model
glove_model = api.load("glove-wiki-gigaword-50")

# Get the vector for the word "language"
word_vector = glove_model["language"]

# Display the result
print("GloVe Vector for 'language':")
print(word_vector)