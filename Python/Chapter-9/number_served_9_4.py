class Restaurant:

    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.number_served = 0

    def describe(self):
        print(f"The {self.name} serves cuisine {self.type} type.")

    def open(self):
        print(f"The restaurant opens 9am in the morning!")

    def read_number(self):
        print(
            f"The number of customers the restaurant has served is {self.number_served}."
        )

    def set_number_served(self, number):
        """set method called set_number_served"""
        if number >= self.number_served:
            self.number_served = number
        else:
            print("Sold out!")

    def increment_number_served(self, number):
        self.number_served += number


my_restaurant = Restaurant("Korean Chicken", "Korean food")
your_restaurant = Restaurant("Bún ốc tôi yêu", "Bún ốc, riêu")

print(f"My restaurant's name is {my_restaurant.name}")
my_restaurant.describe()
my_restaurant.open()
my_restaurant.number_served = 123
my_restaurant.set_number_served(123)
my_restaurant.read_number()


print(f"Your restauran's name is {your_restaurant.name}")
your_restaurant.describe()
your_restaurant.open()
your_restaurant.number_served = 99
your_restaurant.set_number_served(99)
your_restaurant.read_number()
