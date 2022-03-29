import matplotlib.pyplot as plt

def square(list):
    return[i**2 for i in list]

def root(list):
    return[i**0.5 for i in list]

input_values = range(0, 1001, 100)
squares = root(input_values)
input_values_x = range(0, 1000)
input_values_y = [i / 2 for i in input_values_x]

# Print all in-build styles:
# print(plt.style.available)

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(input_values, squares, c = (0, 0.1, 0.8), linewidth = 3, 
        zorder = 1)
ax.scatter(input_values_x, input_values_y, c = input_values_y, 
           cmap = plt.cm.ocean, s = 1)
ax.scatter(input_values, squares, c = squares, cmap = plt.cm.Blues, 
           s = 200, zorder = 5)

# Set the range for each axis.
ax.axis([0, 1000, 0, 1000])

# Set the chart title and label axes.
ax.set_title("Square Numbers", fontsize = 24, color = "blue")
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square of Value", fontsize = 14)

# Set size of tick labels.
ax.tick_params(axis = "both", which = "major", labelsize = 14)  


# plt.show()
plt.savefig('simple-line-graph.png', bbox_inches='tight')