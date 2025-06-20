from pathlib import Path

path = Path("Chapter-10/pi_digits.txt")
contents = path.read_text()
lines = contents.splitlines()
for line in lines:
    print(line)

print(contents)
