import re
from collections import Counter

# Open the provided file
file_path = "J. K. Rowling - Harry Potter 1 - Sorcerer's Stone.txt"
with open(file_path, "r", encoding="utf-8") as file:
    text = file.read()  # Read the file's content

# Regular expression to match English names (capitalized words)
name_pattern = re.compile(r'\b[A-Z][a-z]+\b')

# Find all matches
names = name_pattern.findall(text)

# Common words to exclude (not actual names)
excludes = {"The", "And", "But", "He", "She", "They", "His", "Her", "It", "This", "That", "You", "I", "We", "A", "An"}

# Filter out unwanted words
filtered_names = [name for name in names if name not in excludes]

# Count the frequencies of each name
name_counts = Counter(filtered_names)

# Get the top 10 most frequent names
top_names = name_counts.most_common(10)

# Print the top names and their counts
print("Top 10 Names in the Book:")
for name, count in top_names:
    print(f"{name:<10} {count}")
