from email import header
from pathlib import Path
from datetime import datetime
import csv
from turtle import title
import matplotlib.pyplot as plt
from numpy import place

path = Path("Python/Chapter-16/weather_data/vietnam_weather_summary.csv")
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

date_index = header_row.index("date")
high_index = header_row.index("tmax")
low_index = header_row.index("tmin")
name_index = header_row.index("name")

# Extract dates, highs ans lows temperatures.
dates, highs, lows = [], [], []
places = []
for row in reader:
    if not places:
        places = row[name_index]
    current_date = datetime.strptime(row[2], "%Y-%m-%d")
    try:
        high = float(row[high_index])
        low = float(row[low_index])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# Plot the high and low temperatures.
plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()
ax.plot(dates, highs, color="red", alpha=0.5)
ax.plot(dates, lows, color="blue", alpha=0.5)
# Format plot
title = "Daily High and Low Temperatures, 2025\nViet Nam"
ax.set_title(title, fontsize=20)
ax.set_xlabel("", fontsize=14)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (C)", fontsize=14)
ax.tick_params(labelsize=14)

plt.show()

for index, column_header in enumerate(header_row):
    print(index, column_header)
