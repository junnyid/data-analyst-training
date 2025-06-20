from email import message
from pathlib import Path

# Save favorite number
import json

# prompt the user for their number
number = input("Give me your favorite number: ")

# Save the number
with open("number.json", "w") as f:
    json.dump(number, f)
print("Your favorite number has been saved.")

# read your number
try:
    with open("number.json", "r") as f:
        number = json.load(f)
    print(f"I know your favorite number! It's _____.")
except FileNotFoundError:
    print("I don't know your favorite number yet.")
