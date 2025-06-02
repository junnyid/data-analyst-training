#Importing Classes
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
#Default value
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        """"Return a neatly formated descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

#Setting a Default Value for an Attribute
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

#Modifying an Attribute's Value Through a Method
    def update_odometer(self, mileage):
        """Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

#Incrementing an Attribute's Value Through a Method
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

#Importing a Single Class
from car import Car

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()