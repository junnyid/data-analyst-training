#TUPLE
#Python refers to values that cannot change as immutable, and an immutable list is called a tuple
dimensions = (200, 50)          #using parentheses instead od square brackets
print(dimensions[0])
print(dimensions[1])

#looping through all values in a tuple
for dimension in dimensions:
    print(dimension)

#writing over a tuple
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)