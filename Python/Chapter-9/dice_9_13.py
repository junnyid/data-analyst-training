from random import randint
import re
from unittest import result


class Die:
    """Represent a dice, which can be rolled."""

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)


sides6 = Die()

result = []
for roll in range(10):
    roll_result = sides6.roll_die()
    result.append(roll_result)
print("10 rolls of a 20-sided die:")
print(result)
