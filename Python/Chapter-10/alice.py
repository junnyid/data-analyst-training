# Handling the FileNotFoundError Exception
from importlib.resources import contents
from pathlib import Path

path = Path("Chapter-10/alice.txt")
try:
    contents = path.read_text(encoding="utf-8")
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")
else:
    # Count the approximate number of words in the file:
    words = contents.split()
    num_words = len(words)
    print(f"The file {path} has about {num_words} words.")
