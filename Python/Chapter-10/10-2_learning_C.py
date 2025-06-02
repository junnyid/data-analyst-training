from importlib.resources import contents
from pathlib import Path
path = Path('Chapter-10/learning_python.txt')
contents = path.read_text()

lines = contents.splitlines()
for line in lines:
    line = line.replace('Python', 'C')
    print(line)