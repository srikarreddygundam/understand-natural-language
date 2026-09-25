# Exercise 4: Simple RNN for Text Generation
# This program trains a simple RNN to predict the next character.

import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, SimpleRNN
from tensorflow.keras.utils import to_categorical

# Sample text from the exercise
text = "hello world"

# Create a character-level vocabulary
chars = sorted(set(text))
char_to_idx = {char: idx for idx, char in enumerate(chars)}
idx_to_char = {idx: char for char, idx in char_to_idx.items()}

# Create input-output pairs for training
sequence_length = 3
X = []
y = []

for i in range(len(text) - sequence_length):
    X.append([char_to_idx[char] for char in text[i:i + sequence_length]])
    y.append(char_to_idx[text[i + sequence_length]])

# Convert to numpy arrays
X = np.array(X)
y = to_categorical(y, num_classes=len(chars))

# Reshape input for the RNN
X = X.reshape((X.shape[0], X.shape[1], 1))

# Create the RNN model
model = Sequential()
model.add(SimpleRNN(50, input_shape=(sequence_length, 1)))
model.add(Dense(len(chars), activation="softmax"))

# Compile the model
model.compile(
    optimizer="adam",
    loss="categorical_crossentropy"
)

# Train the model
model.fit(X, y, epochs=200, verbose=0)

# Generate text
seed = "hel"
generated_text = seed

for _ in range(4):
    input_sequence = [
        char_to_idx[char] for char in seed
    ]

    input_sequence = np.array(input_sequence)
    input_sequence = input_sequence.reshape(
        (1, sequence_length, 1)
    )

    prediction = model.predict(
        input_sequence,
        verbose=0
    )

    next_char = idx_to_char[np.argmax(prediction)]

    generated_text += next_char
    seed = seed[1:] + next_char

# Display the result
print("Generated text:")
print(generated_text)