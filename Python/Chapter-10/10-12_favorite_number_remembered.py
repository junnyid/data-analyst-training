from fileinput import filename
import json
from traceback import print_tb

from numpy import number

filename = 'number.json'

try:
    with open('nunber.json') as f:
        number = json.load(f)
except FileNotFoundError:
    number = input('Give me your favorite number: ')
    with open('number.json', 'w') as f:
        json.dump(number, f)
    print("Thanks, I'll remember that.")
else:
    print(f"I know your favorite number! It's {number}.")