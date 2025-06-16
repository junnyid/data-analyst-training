from cProfile import label
from tkinter import font
from matplotlib import axes
import matplotlib.pyplot as plt

x_values = list(range(5001))
cubes = [x**2 for x in x_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(x_values, cubes, c=cubes, cmap=plt.cm.Reds, s=5)

ax.set_title("Cubes", fontsize = 24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

ax.tick_params(axis='both', labelsize=14)
ax.axis([0, 5100, 0, 5100**2])

plt.show()
