# Exercise 4: Dependency Parsing
# This program performs dependency parsing on a sample sentence.

import spacy

# Load the pre-trained spaCy English model
nlp = spacy.load("en_core_web_sm")

# Sample text from the exercise
text = "She enjoys reading books."

# Process the text
doc = nlp(text)

# Display dependency parsing results
print("Dependency Parsing:")
for token in doc:
    print(token.text, token.dep_, token.head.text)