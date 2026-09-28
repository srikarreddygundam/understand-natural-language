# Exercise 3: Training a Custom NER Model
# This program trains a custom NER model to recognize GADGET entities.

import random
import spacy
from spacy.training import Example
from spacy.util import minibatch, fix_random_seed

# Make the training result more consistent
fix_random_seed(42)
random.seed(42)

# Create a blank English model
nlp = spacy.blank("en")

# Add Named Entity Recognition to the pipeline
ner = nlp.add_pipe("ner")

# Add the custom entity label
ner.add_label("GADGET")

# Training data from the exercise
TRAIN_DATA = [
    (
        "Apple is releasing a new iPhone.",
        {"entities": [(25, 31, "GADGET")]}
    ),
    (
        "The new iPad Pro is amazing.",
        {"entities": [(8, 16, "GADGET")]}
    )
]

# Convert the training data into spaCy examples
examples = []

for text, annotations in TRAIN_DATA:
    doc = nlp.make_doc(text)
    example = Example.from_dict(doc, annotations)
    examples.append(example)

# Initialize the model
optimizer = nlp.initialize(
    get_examples=lambda: examples
)

# Train the model
for epoch in range(50):
    random.shuffle(examples)
    losses = {}

    for batch in minibatch(examples, size=2):
        nlp.update(
            batch,
            sgd=optimizer,
            drop=0.2,
            losses=losses
        )

    # Display progress every 10 epochs
    if (epoch + 1) % 10 == 0:
        print("Epoch", epoch + 1, "Losses:", losses)

# Test the trained model
test_text = "I just bought a new iPhone."
doc = nlp(test_text)

# Display detected entities
print("\nNamed Entities:")
for ent in doc.ents:
    print(ent.text, ent.label_)