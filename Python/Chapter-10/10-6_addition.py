try:
    first_number = input("\nFirst number: ")
    second_number = input("Second number: ")
except ValueError:
    print("Give me a number, not a string!")
else:
    answer = int(first_number) + int(second_number)
    print(answer)