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


def gpp_plot(t_time, t_set, pr_vals, pr_time):
    fig = plt.figure(num=1, figsize=(30, 20), dpi=300, facecolor='w', edgecolor='k')
    plt.plot(t_time, t_set[:, 0], 'r.', markersize=5, label=u'Observation')
    plt.plot(pr_time, pr_vals[:, 0], 'b-', linewidth=1, label=u'Prediction')
    # plt.fill_between(x[:, 0], y[:, 0] - 1.96 * sigma, y[:, 0] + 1.96 * sigma, alpha=0.2, color='k',
    #                  label=u'95% confidence interval')
    plt.legend(loc='upper right', fontsize=10)
    plt.xlim(0, 60)
    plt.ylim(-50, 100)
    plt.grid()
    # plt.show()
    fig.savefig('GPP_plot.jpg')
