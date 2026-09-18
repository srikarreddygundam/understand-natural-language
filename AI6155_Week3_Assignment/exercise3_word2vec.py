# Exercise 3: Word2Vec
# This program trains a simple Word2Vec model and displays a word vector.

from gensim.models import Word2Vec

# Sample sentences
sentences = [
    ["natural", "language", "processing", "is", "interesting"],
    ["machine", "learning", "is", "useful"],
    ["word", "embeddings", "represent", "words", "as", "vectors"]
]

# Create and train the Word2Vec model
model = Word2Vec(
    sentences,
    vector_size=50,
    window=5,
    min_count=1,
    workers=1
)

# Get the vector for the word "language"
word_vector = model.wv["language"]

# Display the result
print("Word Vector for 'language':")
print(word_vector)