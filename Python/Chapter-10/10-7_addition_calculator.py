print("Give me two numbers, and I'll add them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == "q":
        break
    second_number = input("Second number: ")
    if second_number == "q":
        break
    answer = int(first_number) + int(second_number)

    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("Give me a number, not a string!")
    else:
        print(answer)
