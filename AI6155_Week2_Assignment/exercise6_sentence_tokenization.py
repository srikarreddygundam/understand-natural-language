# Exercise 6: Sentence Tokenization
# This program breaks a paragraph into individual sentences.

import nltk
from nltk.tokenize import sent_tokenize

# Download required tokenizer resources
nltk.download('punkt')
nltk.download('punkt_tab')

# Sample text
text = "Natural Language Processing is useful. It helps computers understand human language. Python provides many NLP libraries."

# Tokenize the text into sentences
sentences = sent_tokenize(text)

# Display the result
print("Original Text:")
print(text)

print("\nSentence Tokens:")
print(sentences)