# Exercise 3: Sentiment Analysis with TextBlob
# This program analyzes the sentiment of a sentence.

from textblob import TextBlob

# Sample text from the exercise
text = "I am extremely happy with the service provided."

# Create a TextBlob object
blob = TextBlob(text)

# Analyze the sentiment
sentiment = blob.sentiment

# Display the result
print("Sentiment:")
print(sentiment)