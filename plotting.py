import matplotlib.pyplot as plt
from config import *
from numpy import asarray

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


def gpp_plot(exp_data, data, series_borders, predict_states_val_num, std_err, max_abs_err, mae_err, eval_parameter):
    time = data.loc[:, 'time']
    for i in range(0, len(series_borders) - 1):  # Number of series
        test_time_start = series_borders[i + 1] - int(predict_states_val_num[i])  # start idx of predicted states

        train_data = asarray(exp_data.loc[series_borders[i]:series_borders[i + 1] - 1, eval_parameter])
        predicted_data = asarray(data.loc[test_time_start - 1:series_borders[i + 1] - 1, eval_parameter])

        fig = plt.figure(num=1, figsize=(30, 20), dpi=300, facecolor='w', edgecolor='k')
        ax = fig.add_subplot()
        fig.suptitle(g_param1, y=1.2, fontsize=30)
        ax.set_title('series #' + str(i) + ', STD = ' + str(round(std_err[i], 2)) + ', MAX = ' +
                     str(round(max_abs_err[i], 2)) + ', MAE = ' + str(round(mae_err[i], 2)), fontsize=20)
        ax.plot(time[series_borders[i]:series_borders[i + 1]], train_data,
                'b-', markersize=5, label=u'Observation')
        ax.plot(time[test_time_start - 1:series_borders[i + 1]],
                predicted_data, 'r-', linewidth=1, label=u'Prediction')
        # plt.axvline(x=time[test_time_start - 1])
        ax.legend(loc='upper right', fontsize=15)
        ax.grid()
        plt.savefig('/Users/stepanletyagin/Desktop/BMSTU/6_semestr/Coursework/python_code/plots/'
                    + movement_type + '/' + eval_parameter + '/GPP_plot_' + str(i) + '.jpg')
        plt.cla()
        plt.clf()
        plt.close(fig)


def gpp_dot_plot(exp_data, predicted_data, movement_type):
    fig = plt.figure(num=1, figsize=(30, 20), dpi=300, facecolor='w', edgecolor='k')
    ax = fig.add_subplot()
    ax.set_title(movement_type, fontsize=30)
    ax.plot(predicted_data.loc[:, g_param1], predicted_data.loc[:, g_param2], 'r.', linewidth=1, label=u'Prediction')
    ax.plot(exp_data.loc[:, g_param1], exp_data.loc[:, g_param2], 'b.', markersize=5, label=u'Observation')
    ax.legend(loc='upper right', fontsize=10)
    plt.grid()
    fig.savefig('/Users/stepanletyagin/Desktop/BMSTU/6_semestr/Coursework/python_code/plots/'
                + movement_type + '/GPP_dot_plot.jpg')

def gpp_plot_distr(data, train_set_l, val_set_l, time, eval_parameter, i):
    fig = plt.figure(num=1, figsize=(30, 20), dpi=300, facecolor='w', edgecolor='k')
    ax = fig.add_subplot()
    fig.suptitle(g_param1, y=1.2, fontsize=30)

    ax.plot(time[0:train_set_l], data[0:train_set_l], 'b-', markersize=5, label=u'training data')
    ax.plot(time[val_set_l - 1:len(data)], data[val_set_l - 1:len(data)], 'g-', markersize=5, label=u'testing data')
    ax.legend(loc='upper right', fontsize=15)
    ax.grid()
    plt.savefig('/Users/stepanletyagin/Desktop/BMSTU/6_semestr/Coursework/python_code/plots/'
                + movement_type + '/' + eval_parameter + '/data_distribution' + '/GPP_plot_' + str(i) + '.jpg')
    plt.cla()
    plt.clf()
    plt.close(fig)
