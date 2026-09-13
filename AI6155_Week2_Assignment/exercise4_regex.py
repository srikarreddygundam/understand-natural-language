# Exercise 4: Regular Expressions
# This program extracts dates in YYYY-MM-DD format.

import re

# Sample text from the exercise
text = "The project started on 2021-01-15 and ended on 2021-12-31."

# Regex pattern for dates in YYYY-MM-DD format
pattern = r"\b\d{4}-\d{2}-\d{2}\b"

# Find all matching dates
dates = re.findall(pattern, text)

# Display the result
print("Extracted Dates:")
print(dates)