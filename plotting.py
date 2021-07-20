import matplotlib.pyplot as plt


def dot_plot(data1, data2, movement_type):
    fig, ax = plt.subplots(figsize=(30, 20))
    ax.set_title(movement_type, fontsize=50)
    ax.set_xlabel("knee", fontsize=40)
    ax.set_ylabel("hip", fontsize=40)
    plt.plot(data1, data2, 'bo')
    plt.grid()
    plt.show()
    fig.savefig('dot_plot.jpg')


def line_plot(data1, data2, movement_type, ax1, ax2):
    fig, ax = plt.subplots(figsize=(30, 20))
    ax.set_title(movement_type, fontsize=50)
    ax.set_xlabel(ax1, fontsize=40)
    ax.set_ylabel(ax2, fontsize=40)
    plt.plot(data1, data2)
    plt.grid()
    plt.show()
    fig.savefig('line_plot.jpg')