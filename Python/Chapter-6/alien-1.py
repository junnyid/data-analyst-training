# Python's dictionaries allow you to connect pieces of related information
# A simple dictionary
alien_0 = {"color": "green", "points": 5}

new_points = alien_0["points"]
print(f"You just earned {new_points} points!")
print(alien_0["color"])
print(alien_0["points"])

# A dictionary is a collection of key-value pairs. Key connect to value

# remove key-value pairs
del alien_0["points"]
print(alien_0)
