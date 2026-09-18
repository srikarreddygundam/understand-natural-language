# Exercise 1: Bag of Words
# This program converts text documents into a Bag of Words representation.

from sklearn.feature_extraction.text import CountVectorizer

# Sample text corpus
documents = [
    "Text processing is important for NLP.",
    "Bag of Words is a simple text representation method.",
    "Feature engineering is essential in machine learning."
]

# Create the CountVectorizer
vectorizer = CountVectorizer()

# Convert the documents into numerical features
X = vectorizer.fit_transform(documents)

# Convert the result into an array
bow_array = X.toarray()

# Get the vocabulary
vocab = vectorizer.get_feature_names_out()

# Display the results
print("Vocabulary:")
print(vocab)

print("\nBag of Words Array:")
print(bow_array)