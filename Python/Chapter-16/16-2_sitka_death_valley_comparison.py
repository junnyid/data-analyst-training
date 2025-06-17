from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt
from matplotlib.rcsetup import ValidateInStrings
from scipy.datasets import face

def get_weather_data(path, dates, highs, lows, date_index, high_index, low_index):
    #Get the highs and lows from a data file.
    lines = path.read_text().splitlines()
    reader = csv.reader(lines)
    header_row = next(reader)

    #Extract dates, highs and lows temperatures.
    for row in reader:
        current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
        try:
            high = int(row[high_index])
            low = int(row[low_index])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
            
#Get weather data for Sitka
path = Path('Python/Chapter-16/weather_data/sitka_weather_2021_simple.csv')
dates, highs, lows = [], [], []
get_weather_data(path, dates, highs, lows, date_index=2, high_index=4, low_index=5)

#Plot weather data for Sitka
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

#Get weather data for Death Valley
path = Path('Python/Chapter-16/weather_data/death_valley_2021_simple.csv')
dates, highs, lows = [], [], []
get_weather_data(path, dates, highs, lows, date_index=2, high_index=3, low_index=4)

#Add Death Valley weather data to current plot
ax.plot(dates, highs, color='red', alpha=0.25)
ax.plot(dates, lows, color='blue', alpha=0.25)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.05)


#Format plot
title = "Daily High and Low Temparatures, 2021 \nSitka, AK and Death Valley, CA"
ax.set_title(title, fontsize=20)
ax.set_xlabel('', fontsize=14)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=14)
ax.tick_params(labelsize=14)
ax.set_ylim(10, 140)

plt.show()
