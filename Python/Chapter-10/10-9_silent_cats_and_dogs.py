filenames = ['Chapter-10/cats.txt', 'Chapter-10/dogs.txt']

for filename in filenames:
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        print(f"\nReading File: {filename}")
        print(contents)