#Working with Multiple Files
from importlib.resources import contents
from itertools import count
from os import path
from pathlib import Path

def count_words(path):
    """Count the approximate number of words in a file."""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, the file {path} does not exist.")
    else:
        #Count the approximate number of words in the file:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")
path = Path('Chapter-10/alice.txt')
count_words(path)
    
filenames = ['Chapter-10/alice.txt', 'Chapter-10/guest.txt', 'Chapter-10/learning_python.txt']
for filename in filenames:
    path = Path(filename)
    count_words(path)