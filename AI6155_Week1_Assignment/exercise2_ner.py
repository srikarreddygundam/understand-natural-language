# Exercise 2: Named Entity Recognition with spaCy
# This program identifies named entities such as organizations and people.

import spacy

# Load the English language model
nlp = spacy.load("en_core_web_sm")

# Sample text from the exercise
text = "Google was founded by Larry Page and Sergey Brin while they were Ph.D. students at Stanford University."

# Process the text
doc = nlp(text)

# Display the named entities
print("Named Entities:")

for ent in doc.ents:
    print(ent.text, ent.label_)