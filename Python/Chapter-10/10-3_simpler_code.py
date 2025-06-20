from importlib.resources import contents
from pathlib import Path

path = Path("Chapter-10/pi_digits.txt")
contents = path.read_text()
pi_string = ""
for line in contents.splitlines():
    pi_string += line.lstrip()

print(line)
print(f"{pi_string[:52]}...")
print(len(pi_string))
