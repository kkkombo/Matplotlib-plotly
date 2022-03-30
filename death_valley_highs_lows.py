import csv
import matplotlib.pyplot as plt
from datetime import datetime as dt

filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # Get dates, and high and low temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = dt.strptime(row[2], '%d/%m/%Y')
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            highs.append(high)
            lows.append(low)
            dates.append(current_date)

# Plot the high temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(dates, highs, c = highs, cmap = plt.cm.Wistia, 
           s = 10, zorder = 10)
ax.scatter(dates, lows, c = lows, cmap = plt.cm.viridis, 
           s = 10, zorder = 10)
ax.plot(dates, highs, c = 'red', zorder = 1, alpha = 0.5)
ax.plot(dates, lows, c = 'blue', zorder = 1, alpha = 0.5)
plt.fill_between(dates, highs, lows, facecolor = 'blue', alpha = 0.1)

# Format plot.
plt.title("Daily high and low temperatures - 2018\nDeath Valley", 
          fontsize = 24)
plt.xlabel('', fontsize = 16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize = 16)
plt.tick_params(axis = 'both', which = 'major', labelsize = 16)
plt.savefig('sitka_weather_2018.png')
plt.show()