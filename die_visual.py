from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

die = Die()

# Create a score table for Die results.
die_results = []

# Throwing dies.
for throw in range(0, 1000):
    throw = die.roll()
    die_results.append(throw)

# Analyse the results.
frequencies = {}
for value in range(1, die.num_sides+1):
    frequency = die_results.count(value)
    frequencies[value] = frequency
print(frequencies)

# Check all throws.
all_sum = 0
for value in frequencies.values():
    all_sum += value
print(all_sum)

# Visualize the results.
x_values = list(range(1, die.num_sides + 1))
data = [Bar(x = x_values, y = list(frequencies.values()))]

x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling one D6 1000 times', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')