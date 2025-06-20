from cProfile import label
import plotly.express as px

from unittest import result
from die import Die

# Create two D6
die_1 = Die()
die_2 = Die()

# Make some rolls, and store results in a list
results = [die_1.roll() + die_2.roll() for roll_num in range(1000)]

# Analyze the results.
possible_results = range(2, die_1.num_sides + die_2.num_sides + 1)
frequencies = [results.count(value) for value in possible_results]

# Visualize the results.
title = "Results of Rolling Two D6 Dice 1,000 Times"
labels = {"x": "Result", "y": "Frequency of Result"}
fig = px.bar(x=possible_results, y=frequencies, title=title, labels=labels)

# Further customize chart
fig.update_layout(xaxis_dtick=1)

fig.show()
