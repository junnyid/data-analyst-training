#using multiple lists
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requedted_topping in requested_toppings:
    if requedted_topping in available_toppings:
        print(f"Adding {requedted_topping}")
    else:
        print(f"Sorry, we don't have {requedted_topping}.")
    
print("\nFinished making your pizza!")      