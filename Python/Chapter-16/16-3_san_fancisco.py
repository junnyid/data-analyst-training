from email import header
from pathlib import Path
from datetime import datetime
import csv
from turtle import title
import matplotlib.pyplot as plt

path = Path("Python/Chapter-16/weather_data/san_francisco_weather_data.csv")
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Extract dates, highs ans lows temperatures.
dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], "%Y-%m-%d")
    high = float(row[3])
    low = float(row[4])
    dates.append(current_date)
    highs.append(high)
    lows.append(low)
# Plot the high and low temperatures.
plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()
ax.plot(dates, highs, color="red", alpha=0.5)
ax.plot(dates, lows, color="blue", alpha=0.5)
# Format plot
title = "Daily High and Low Temperatures, 2025\nSan Francisco"
ax.set_title(title, fontsize=20)
ax.set_xlabel("", fontsize=14)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=14)
ax.tick_params(labelsize=14)

plt.show()

for index, column_header in enumerate(header_row):
    print(index, column_header)
