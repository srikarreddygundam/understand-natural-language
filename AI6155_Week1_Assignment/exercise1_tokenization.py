# Exercise 1: Tokenization with NLTK
# This program breaks a sentence into individual tokens.

import nltk
from nltk.tokenize import word_tokenize

# Download required tokenizer resources
nltk.download('punkt')
nltk.download('punkt_tab')

# Sample text
text = "Natural Language Processing enables computers to understand human language."

# Tokenize the text
tokens = word_tokenize(text)

# Display the tokens
print("Tokens:")
print(tokens)