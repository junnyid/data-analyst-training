#Removing all instances of Specific Values from a List
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
print(pets)
