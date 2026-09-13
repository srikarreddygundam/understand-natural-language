# Exercise 1: Stop Word Removal
# This program removes common stop words from a sentence.

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download required NLTK resources
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

# Sample text
text = "Natural Language Processing enables computers to understand human language."

# Tokenize the text
tokens = word_tokenize(text)

# Load English stop words
stop_words = set(stopwords.words('english'))

# Remove stop words
filtered_tokens = [
    word for word in tokens
    if word.lower() not in stop_words
]

# Display the results
print("Original Tokens:")
print(tokens)

print("\nFiltered Tokens:")
print(filtered_tokens)