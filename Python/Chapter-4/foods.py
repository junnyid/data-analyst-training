my_foods = ['pizza', 'falafel', ' carrot cake']
friend_foods = my_foods[:]      #copying a list
#friend_foods = my_foods    => this doesn't work: when append cannoli, ice cream=> they will appear both of lists


my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)