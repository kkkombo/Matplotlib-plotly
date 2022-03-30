import csv
import matplotlib.pyplot as plt

filename = 'data/sitka_weather_07-2018_simple.csv'

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
        date = str(row[2])

        highs.append(high)
        lows.append(low)
        dates.append(date)
    print(highs)
    print(lows)
    print(dates)

# Plot the high temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(dates, highs, c = highs, cmap = plt.cm.Wistia, zorder = 10)
ax.plot(highs, c = 'red', zorder = 1)

# Format plot.
plt.title("Daily high temperatures, July 2018", fontsize = 24)
plt.xlabel('', fontsize = 16)
plt.ylabel("Temperature (F)", fontsize = 16)
plt.tick_params(axis = 'both', which = 'major', labelsize = 16)
plt.show()