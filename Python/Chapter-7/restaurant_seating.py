seating = input("How many people are in their dinner group?")
seating = int(seating)

if seating >= 8:
    print(f"\nThey'll have to wait for a table. ")
else:
    print(f"\nTheir table is ready! ")