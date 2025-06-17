from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path('Python/Chapter-16/weather_data/sitka_weather_2021_full.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

#Extract dates, highs ans lows temperatures.
dates, prcps = [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    prcp = float(row[5])
    dates.append(current_date)
    prcps.append(prcp)
        
#Plot the high and low temperatures.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.bar(dates, prcps, color='blue')

#Format plot
title = "Daily Rainfall Amounts, 2021"
ax.set_title(title, fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
