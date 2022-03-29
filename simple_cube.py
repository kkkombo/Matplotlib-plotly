import matplotlib.pyplot as plt

def cube(list):
    return[i**3 for i in list]

input_values = range(1,5)
input_values2 = range(0, 5000)
input_values2_y = cube(input_values2)

fig, ax = plt.subplots()
# First 5 values:
# ax.plot(input_values, cube(input_values))

ax.scatter(input_values2, input_values2_y, c = input_values2_y, 
           cmap = plt.cm.Blues)

plt.show()