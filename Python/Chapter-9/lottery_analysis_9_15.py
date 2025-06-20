import random

lottery_numbers = list(range(1, 11)) + list("ABCDE")
my_ticket = random.sample(lottery_numbers, 4)
print("Your ticket:", my_ticket)

attempts = 0
found = False

while not found:
    attempts += 1
    win_ticket = random.sample(lottery_numbers, 4)
    if win_ticket == my_ticket:
        found = True

print("Winning ticket:", win_ticket)
print(f"It took {attempts} attempts to win the lottery.")
