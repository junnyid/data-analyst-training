#Storing Data
#The JSON(JaveScript Object Notation) format was originally developed for JavaScript. It has since become a common format used by many languages, including Python.

#Using json.dumps() and json.loads()
"""The json.dumps() function takes one argument"""
from pathlib import Path
import json

numbers = [2, 3, 5, 7, 11, 13]

path = Path('numbers.json')
contents = json.dumps(numbers)
path.write_text(contents)