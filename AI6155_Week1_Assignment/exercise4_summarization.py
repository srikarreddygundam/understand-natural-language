# Exercise 4: Text Summarization with Sumy
# This program summarizes a paragraph into two sentences.

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

# Sample text from the exercise
text = """
Natural Language Processing (NLP) is a fascinating field at the intersection of
computer science, artificial intelligence, and linguistics. It enables machines to
understand, interpret, and generate human language, opening up a world of possibilities
for applications ranging from chatbots and translation services to sentiment analysis
and beyond. The evolution of NLP has been driven by significant advances in machine
learning and deep learning, which have enabled more sophisticated and accurate models
for language understanding. This book aims to bring these cutting-edge techniques to
you in an accessible and practical way, regardless of your current level of expertise.
"""

# Parse the text
parser = PlaintextParser.from_string(text, Tokenizer("english"))

# Create the summarizer
summarizer = LsaSummarizer()

# Generate a two-sentence summary
summary = summarizer(parser.document, 2)

# Display the summary
print("Summary:")

for sentence in summary:
    print(sentence)