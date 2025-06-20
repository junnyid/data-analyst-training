from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt
from matplotlib.rcsetup import ValidateInStrings
from scipy.datasets import face

path = Path("Python/Chapter-16/weather_data/death_valley_2021_simple.csv")
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

date_index = header_row.index("DATE")
high_index = header_row.index("TMAX")
low_index = header_row.index("TMIN")
name_index = header_row.index("NAME")

# Extract dates, highs, low temperature
dates, highs, lows = [], [], []
places = []
for row in reader:
    if not places:
        places = row[name_index]
    current_date = datetime.strptime(row[date_index], "%Y-%m-%d")
    try:
        high = int(row[high_index])
        low = int(row[low_index])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# Plot weather data for Sitka
plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()
ax.plot(dates, highs, color="red", alpha=0.5)
ax.plot(dates, lows, color="blue", alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

# Format plot
title = f"Daily High and Low Temperatures, 2021\n{places}"
ax.set_title(title, fontsize=20)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=14)
ax.tick_params(labelsize=14)

plt.show()
