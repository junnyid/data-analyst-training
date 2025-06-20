from cProfile import label
import plotly.express as px

from unittest import result
from die import Die

# Create a D6
die = Die()

# Make some rolls, and store results in a list
results = []
for roll_num in range(100):
    result = die.roll()
    results.append(result)

# Analyze the results.
frequencies = []
poss_results = range(1, die.num_sides + 1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
title = "Results of Rolling One D6 Dice 1,000 Times"
labels = {"x": "Result", "y": "Frequency of Result"}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Further customize chart
fig.update_layout(xaxis_dtick=1)

fig.show()

print(results)
print(frequencies)
