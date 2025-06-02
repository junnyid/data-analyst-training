class Dog:
    """A simple attempt to model a dog."""
    
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
    
    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(f"{self.name} is now sitting.")
    
    def roll_over(self):
        """Simulate rolling over in respone to a command."""
        print(f"{self.name} rolled over!")

my_dog = Dog("Ẳng", 7)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

#Calling method
my_dog.sit()
my_dog.roll_over()

#Creating multiple instance
dwingadium_dog = Dog('Juny', 10)
your_dog = Dog('Cat', 5)

print(f"His dog's name is {dwingadium_dog.name}.")
print(f"His dog is {dwingadium_dog.age} years old.")
dwingadium_dog.roll_over()

print(f"Your dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
