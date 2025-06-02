from pathlib import Path

from matplotlib import lines

path = Path('Chapter-10/pi_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()
    
print(pi_string)
print(f"{pi_string[:52]}...")
print(len(pi_string))