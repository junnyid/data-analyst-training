from importlib.resources import contents
from pathlib import Path
import json

from numpy import number

path = Path("numbers.json")
contents = path.read_text()
numbers = json.loads(contents)

print(numbers)
