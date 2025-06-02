#Adding New Key-Value Pairs
#Dictionaries: dynamic structures
alien_0 = {'color': 'green', 'point': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#an Empty dictionary
alien_1 = {}

alien_1['color'] = 'green'
alien_1['points'] = 5

print(alien_1)

#modifying values in a dictionary
alien_2 = {'color': 'green'}
print(f"The alien is {alien_2['color']}.")

alien_2['color'] = 'yellow'
print(f"The alien is now {alien_2['color']}.")
