from pylab import *
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


def hist(data1, data2):
    fig = plt.figure(num=1, figsize=(30, 20), dpi=300, facecolor='w', edgecolor='k')
    plt.hist2d(data1, data2, bins=(200, 200), vmax=30)
    plt.colorbar()
    plt.xlabel('knee')
    plt.ylabel('hip')
    fig.savefig('hist_plot.jpg')


def gpp_plot(t_time, t_set, pr_time, pr_vals, series_num):
    fig = plt.figure(num=1, figsize=(30, 20), dpi=300, facecolor='w', edgecolor='k')
    ax = fig.add_subplot()
    ax.set_title('series #' + str(series_num), fontsize=50)
    ax.plot(t_time, t_set[:, 0], 'r-', markersize=5, label=u'Observation')
    ax.plot(pr_time, pr_vals[:, 0], 'b-', linewidth=1, label=u'Prediction')
    ax.legend(loc='upper right', fontsize=15)
    ax.grid()
    plt.savefig('/Users/stepanletyagin/Desktop/BMSTU/6_semestr/Coursework/python_code/plots/GPP_plot_' + str(series_num) + '.jpg')
    plt.cla()
    plt.clf()
    plt.close(fig)


def gpp_dot_plot(t_set, pr_vals):
    fig = plt.figure(num=1, figsize=(30, 20), dpi=300, facecolor='w', edgecolor='k')
    plt.plot(t_set[:, 0], t_set[:, 1], 'r.', markersize=5, label=u'Observation')
    plt.plot(pr_vals[:, 0], pr_vals[:, 1], 'b.', linewidth=1, label=u'Prediction')
    # plt.fill_between(x[:, 0], y[:, 0] - 1.96 * sigma, y[:, 0] + 1.96 * sigma, alpha=0.2, color='k',
    #                  label=u'95% confidence interval')
    plt.legend(loc='upper right', fontsize=10)
    plt.xlim(0, 60)
    plt.ylim(-50, 100)
    plt.grid()
    # plt.show()
    fig.savefig('/Users/stepanletyagin/Desktop/BMSTU/6_semestr/Coursework/python_code/plots/GPP_dot_plot.jpg')
