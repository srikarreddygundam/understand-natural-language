# Exercise 2: Stemming
# This program reduces words to their root form using Porter Stemmer.

from nltk.stem import PorterStemmer

# Sample text
text = "running runner runs easily fairly"

# Split the text into words
tokens = text.split()

# Create the stemmer
stemmer = PorterStemmer()

# Stem each word
stemmed_tokens = [stemmer.stem(word) for word in tokens]

# Display the results
print("Original Tokens:")
print(tokens)

print("\nStemmed Tokens:")
print(stemmed_tokens)