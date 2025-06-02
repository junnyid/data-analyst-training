#Passing an Arbitrary Number of Arguments
def make_pizza(size, *toppings):          #the astrisk *toppings: make a tuple called toppings
    """Print the list of toppings that have been requested."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushroom', 'green peppers', 'extra cheese')
