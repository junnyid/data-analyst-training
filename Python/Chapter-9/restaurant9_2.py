class Restaurant:
    
    def __init__(self, name, type):
        self.name = name
        self.type = type
    
    def describe(self):
        print(f"The {self.name} serves cuisine {self.type} type.")
    
    def open(self):
        print(f"The restaurant opens 9am in the morning!")
        
my_restaurant = Restaurant('Korean Chicken', 'Korean food')
your_restaurant = Restaurant('Bún ốc tôi yêu', 'Bún ốc, riêu')
his_restaurant = Restaurant('Phở gà phố cổ', 'Phở lẫn giòn sần sật')

my_restaurant.describe()
your_restaurant.describe()
his_restaurant.describe()
