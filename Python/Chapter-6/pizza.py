# Store information about a pizza being ordered
pizza = {
    'crust': 'thick',
    'toppings': ['mushroom', 'extra cheese'],
    }
# Summarize the order
print(f"You order a {pizza['crust']}-crust pizza "
      "with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")
    