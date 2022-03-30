import csv
import matplotlib.pyplot as plt
from datetime import datetime as dt

sitka = 'data/sitka_weather_2018_simple.csv'
death_valley = 'data/death_valley_2018_simple.csv'

with open(death_valley) as f:
    dv_reader = csv.reader(f)
    dv_header_row = next(dv_reader)

    # Get dates, and high and low temperatures from this file.
    dv_dates, dv_highs, dv_lows = [], [], []
    for row in dv_reader:
        try:
            dv_current_date = dt.strptime(row[dv_header_row.index('DATE')], '%d/%m/%Y')
            dv_high = int(row[dv_header_row.index('TMAX')])
            dv_low = int(row[dv_header_row.index('TMIN')])
            dv_name = str(row[dv_header_row.index('NAME')])
        except ValueError:
            print(f"Missing data for {dv_current_date}")
        else:
            dv_highs.append(dv_high)
            dv_lows.append(dv_low)
            dv_dates.append(dv_current_date)

with open(sitka) as f:
    s_reader = csv.reader(f)
    s_header_row = next(s_reader)
    # Print headers values.
    # print(s_header_row)

    #for index, column_header in enumerate(s_header_row):
        #print(index, column_header)

    # Extracting high temps from reader
    s_dates, s_lows, s_highs = [], [], []
    for row in s_reader:
        s_high = int(row[5])
        s_low = int(row[6])
        s_date = dt.strptime(row[2], '%d/%m/%Y')
        s_name = str(row[s_header_row.index('NAME')])

        s_highs.append(s_high)
        s_lows.append(s_low)
        s_dates.append(s_date)

plt.style.use('seaborn')
fig, ax = plt.subplots()
# Plot sitka
ax.plot(s_dates, s_highs, c = 'red', zorder = 1, alpha = 0.5)
ax.plot(s_dates, s_lows, c = 'blue', zorder = 1, alpha = 0.5)
plt.fill_between(s_dates, s_highs, s_lows, facecolor = 'blue', 
                 alpha = 0.1)
# plot death valley
ax.plot(dv_dates, dv_highs, c = 'red', zorder = 1, alpha = 0.5)
ax.plot(dv_dates, dv_lows, c = 'blue', zorder = 1, alpha = 0.5)
plt.fill_between(dv_dates, dv_highs, dv_lows, facecolor = 'red', 
                 alpha = 0.1)

# Format plot.
plt.title(f"Daily high and low temperatures\n{dv_name} and {s_name}", 
          fontsize = 24)
plt.xlabel('', fontsize = 16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize = 16)
plt.tick_params(axis = 'both', which = 'major', labelsize = 16)
plt.savefig('sitka_death_valley.png')
plt.show()