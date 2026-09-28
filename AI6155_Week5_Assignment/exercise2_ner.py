# Exercise 2: Named Entity Recognition (NER)
# This program identifies named entities in a sample sentence.

import spacy

# Load the pre-trained spaCy English model
nlp = spacy.load("en_core_web_sm")

# Sample text from the exercise
text = "Barack Obama was born on August 4, 1961, in Honolulu, Hawaii."

# Process the text
doc = nlp(text)

# Display named entities and their labels
print("Named Entities:")
for ent in doc.ents:
    print(ent.text, ent.label_)