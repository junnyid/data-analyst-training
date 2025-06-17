from cProfile import label
from email import header
from pathlib import Path

import csv
from datetime import datetime
from turtle import color

import matplotlib.pyplot as plt

from pyparsing import line

#path = Path('Python/Chapter-16/weather_data/sitka_weather_07-2021_simple.csv')
path = Path('Python/Chapter-16/weather_data/sitka_weather_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

#Extract dates and high temperatures
dates, highs = [], []

#Extract high temperature
#highs = []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    high = int(row[4])
    dates.append(current_date)
    highs.append(high)
print(highs)

for index, column_header in enumerate(header_row):
    print(index, column_header)

print(header_row)

#Plot the high temperature
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
#ax.plot(highs, color='red')
ax.plot(dates, highs, color='red')

#Format plot
#ax.set_title("Daily High Temperatures, July 2021", fontsize=24)
ax.set_title("Daily High Temperature, 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()