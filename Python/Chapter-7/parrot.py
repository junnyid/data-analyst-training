# USER INPUT AND WHILE LOOPS
# how to accept user input so your program can then work with it

# The input() function: pauses your program, waits for the users
# message = input("Tell me something, and I will repeat it back to you:")
# print(message)

# Letting the user choose when to quit
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""  # keep track value
while message != "quit":
    message = input(prompt)
    if message != "quit":
        print(message)

# active = True  #using the Flag:
# while active:
#     message = input(prompt)

#     if message != 'quit':
#         active = False
#     else:
#         print(message)
