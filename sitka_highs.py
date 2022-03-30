import csv
import matplotlib.pyplot as plt
from datetime import datetime as dt

filename = 'data/sitka_weather_2018_simple.csv'

# Open the file.
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # Print headers values.
    # print(header_row)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # Extracting high temps from reader
    dates, lows, highs = [], [], []
    for row in reader:
        high = int(row[5])
        low = int(row[6])
        date = dt.strptime(row[2], '%d/%m/%Y')

        highs.append(high)
        lows.append(low)
        dates.append(date)
    # Checks.
    # print(highs)
    # print(lows)
    # print(dates)

# Plot the high temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(dates, highs, c = highs, cmap = plt.cm.Wistia, s = 10, zorder = 10)
ax.plot(dates, highs, c = 'red', zorder = 1)

# Format plot.
plt.title("Daily high temperatures - 2018", fontsize = 24)
plt.xlabel('', fontsize = 16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize = 16)
plt.tick_params(axis = 'both', which = 'major', labelsize = 16)
plt.savefig('sitka_weather_2018.png')
plt.show()