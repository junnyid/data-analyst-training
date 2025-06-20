from importlib.resources import contents
from pathlib import Path


def count_words(filenames, word):
    """Calculating the frequency of occurring words"""
    try:
        with open(filenames, encoding="utf-8") as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        words = contents.count(word)
        print(f"The file {filenames} has about {words} words.")


filenames = [
    "Chapter-10/theAAB.txt",
    "Chapter-10/baartock.txt",
    "Chapter-10/the_cabala.txt",
]
for filename in filenames:
    path = Path(filename)
    count_words(path, "the")
