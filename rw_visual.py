import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    rw = RandomWalk(5_000)
    rw.fill_walk()

    # Create a plot with RW.
    fig, ax = plt.subplots(figsize = (15, 9))
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, s = 15, c = point_numbers, cmap = plt.cm.cool)
    #ax.plot(rw.x_values, rw.y_values, linewidth = 3)
    # First point.
    # ax.scatter(0, 0, c = 'black', s = 20)
    # Last point.
    # ax.scatter(rw.x_values[-1], rw.y_values[-1], c = 'black', s = 20)

    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    # Show thee plot.
    plt.savefig('random_walk.png')
    plt.show()

    # Check if continue.
    keep_running = input("Make another walk (y/n): ")
    if keep_running.lower() == 'n':
        break