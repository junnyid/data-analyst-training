age = 75

vower = ["u", "e", "o", "a", "i"]

if age < 2:
    stage = "baby"
elif age < 4:
    stage = "toddler"
elif age < 13:
    stage = "kid"
elif age < 20:
    stage = "teenager"
elif age < 65:
    stage = "adult"
else:
    stage = "elder"

print(f"The person is {'an' if stage[0] in vower else 'a'} {stage}.")  # using string
