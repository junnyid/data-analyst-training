# Writing a Single Line
from importlib.resources import contents
from pathlib import Path

contents = "I love programming.\n"
contents += "I love creating new game.\n"
contents += "I also love working with data.\n"
contents += "I love Python!"

path = Path("Chapter-10/programming.txt")
path.write_text(contents)
