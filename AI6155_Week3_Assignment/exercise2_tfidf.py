# Exercise 2: TF-IDF
# This program converts text documents into TF-IDF features.

from sklearn.feature_extraction.text import TfidfVectorizer

# Sample text corpus
documents = [
    "Text processing is important for NLP.",
    "Bag of Words is a simple text representation method.",
    "Feature engineering is essential in machine learning."
]

# Create the TF-IDF vectorizer
vectorizer = TfidfVectorizer()

# Convert the documents into TF-IDF features
X = vectorizer.fit_transform(documents)

# Convert the result into an array
tfidf_array = X.toarray()

# Get the vocabulary
vocab = vectorizer.get_feature_names_out()

# Display the results
print("Vocabulary:")
print(vocab)

print("\nTF-IDF Array:")
print(tfidf_array)