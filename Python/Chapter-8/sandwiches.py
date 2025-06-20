def make_sandwich(*toppings):
    print("\nAdding toppings into your sandwich:")
    for topping in toppings:
        print(topping)
    print("Your sandwich is ready!")


make_sandwich("beef", "egg", "salad", "chili", "majo")
make_sandwich("tuna", "majo", "salad")
make_sandwich("strawberry", "orange", "blueberry jam")
