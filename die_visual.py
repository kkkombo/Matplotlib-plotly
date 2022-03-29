from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

die_1 = Die()
die_2 = Die()

# Create a score table for Die results.
die_results = []

# Throwing dies.
for throw in range(0, 1000):
    throw_1 = die_1.roll()
    throw_2 = die_2.roll()
    die_results.append(throw_1 + throw_2)

# Analyse the results.
frequencies = {}
max_result = die_1.num_sides + die_2.num_sides
print(max_result)
for value in range(2, max_result + 1):
    frequency = die_results.count(value)
    frequencies[value] = frequency
print(frequencies)

# Check all throws.
all_sum = 0
for value in frequencies.values():
    all_sum += value
print(all_sum)

# Visualize the results.
x_values = list(range(2, max_result + 1))
data = [Bar(x = x_values, y = list(frequencies.values()))]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling two D6 1000 times', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6.html')