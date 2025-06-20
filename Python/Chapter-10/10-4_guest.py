from importlib.resources import contents
from os import path
from pathlib import Path

contents = "Hello, my name is Junny.\n"
contents += "I love Python!\n"
contents += "I love chilling in my room."

path = Path("Chapter-10/guest.txt")
path.write_text(contents)
