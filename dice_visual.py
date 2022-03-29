from plotly.graph_objs import Bar, Layout
from plotly import offline

from dice import Dice

dice_1 = Dice()
dice_2 = Dice(num_sides = 10)

# Create a score table for Die results.
dice_results = []

# Throwing dies.
for throw in range(0, 10000):
    throw_1 = dice_1.roll()
    throw_2 = dice_2.roll()
    dice_results.append(throw_1 + throw_2)

# Analyse the results.
frequencies = {}
max_result = dice_1.num_sides + dice_2.num_sides
print(max_result)
for value in range(2, max_result + 1):
    frequency = dice_results.count(value)
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
my_layout = Layout(title='Results of rolling D6 and D10 10000 times', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d10.html')