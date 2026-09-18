# Exercise 5: BERT Embeddings
# This program generates a BERT embedding for a sample sentence.

from transformers import BertTokenizer, BertModel
import torch

# Load pretrained BERT tokenizer and model
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertModel.from_pretrained("bert-base-uncased")

# Sample text
text = "Natural Language Processing is interesting."

# Convert the text into BERT input tokens
inputs = tokenizer(text, return_tensors="pt")

# Generate embeddings
with torch.no_grad():
    outputs = model(**inputs)

# Get the embedding for the [CLS] token
embedding = outputs.last_hidden_state[:, 0, :]

# Display the result
print("BERT Embedding Shape:")
print(embedding.shape)

print("\nFirst 10 values of the BERT embedding:")
print(embedding[0][:10])