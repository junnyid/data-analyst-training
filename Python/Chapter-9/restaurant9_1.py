class Restaurant:

    def __init__(self, name, type):
        self.name = name
        self.type = type

    def describe(self):
        print(f"The {self.name} serves cuisine {self.type} type.")

    def open(self):
        print(f"The restaurant opens 9am in the morning!")


my_restaurant = Restaurant("Korean Chicken", "Korean food")
your_restaurant = Restaurant("Bún ốc tôi yêu", "Bún ốc, riêu")

print(f"My restaurant's name is {my_restaurant.name}")
my_restaurant.describe()
my_restaurant.open()

print(f"Your restauran's name is {your_restaurant.name}")
your_restaurant.describe()
your_restaurant.open()
