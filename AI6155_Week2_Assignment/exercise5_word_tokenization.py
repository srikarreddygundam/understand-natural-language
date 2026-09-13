# Exercise 5: Word Tokenization
# This program breaks a sentence into individual words.

import nltk
from nltk.tokenize import word_tokenize

# Download required tokenizer resources
nltk.download('punkt')
nltk.download('punkt_tab')

# Sample text
text = "Tokenization is the first step in text preprocessing."

# Tokenize the text into words
tokens = word_tokenize(text)

# Display the result
print("Original Text:")
print(text)

print("\nWord Tokens:")
print(tokens)