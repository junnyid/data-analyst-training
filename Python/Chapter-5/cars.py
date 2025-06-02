# IF STATEMENTS
#if statement allows to examine the current state of a programm and respond appropriately to that state

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
        