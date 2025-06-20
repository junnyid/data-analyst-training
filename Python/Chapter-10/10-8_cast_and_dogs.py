from pathlib import Path

filenames = ["Chapter-10/cats.txt", "Chapter-10/dogs.txt"]


def count_words(path):
    try:
        contents = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")


for filename in filenames:
    path = Path(filename)
    count_words(path)
