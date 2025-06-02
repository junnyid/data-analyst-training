from cmd import PROMPT
from pathlib import Path

path = Path('Chapter-10/guest_book.txt')
PROMPT = "Hello, I'm Junny, comment tu ca va?\n"
PROMPT += "Enter 'quit' if you're the last guest."

guest_names = []
while True:
    name = input(PROMPT)
    if name == 'quit':
        break
    
    print(f"Thanks {name}, we'll add you to the guest book.")
    guest_names.append(name)
    
file_string = ''
for name in guest_names:
    file_string += f"{name}\n"
path.write_text(file_string)