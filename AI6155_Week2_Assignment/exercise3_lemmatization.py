# Exercise 3: Lemmatization
# This program reduces words to their base dictionary form.

import nltk
from nltk.stem import WordNetLemmatizer

# Download required WordNet resources
nltk.download('wordnet')
nltk.download('omw-1.4')

# Sample words
words = ["cars", "running", "better", "feet"]

# Create the lemmatizer
lemmatizer = WordNetLemmatizer()

# Lemmatize the words
lemmatized_words = [
    lemmatizer.lemmatize("cars"),
    lemmatizer.lemmatize("running", pos="v"),
    lemmatizer.lemmatize("better", pos="a"),
    lemmatizer.lemmatize("feet")
]

# Display the results
print("Original Words:")
print(words)

print("\nLemmatized Words:")
print(lemmatized_words)