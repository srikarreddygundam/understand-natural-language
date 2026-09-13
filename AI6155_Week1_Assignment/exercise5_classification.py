# Exercise 5: Text Classification with scikit-learn
# This program trains a Naive Bayes classifier and predicts sentiment.

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Training text
texts = [
    "I love this product",
    "This is the worst experience",
    "Absolutely fantastic!",
    "Not good at all"
]

# 1 = positive, 0 = negative
labels = [1, 0, 1, 0]

# Convert the text into numerical features
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

# Create and train the classifier
classifier = MultinomialNB()
classifier.fit(X, labels)

# New text to classify
new_text = ["This experience was fantastic"]

# Convert the new text using the same vectorizer
X_new = vectorizer.transform(new_text)

# Predict the sentiment
prediction = classifier.predict(X_new)

# Display the result
print("Prediction:")
print(prediction)

if prediction[0] == 1:
    print("Sentiment: Positive")
else:
    print("Sentiment: Negative")