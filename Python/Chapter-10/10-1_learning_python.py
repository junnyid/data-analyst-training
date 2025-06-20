from importlib.resources import contents
from pathlib import Path
from re import split

path = Path("Chapter-10/learning_python.txt")
contents = path.read_text()
print(contents)
# Vong lap cac dong
lines = contents.splitlines()
for line in lines:
    print(line)
