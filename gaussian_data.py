import numpy as np


def gauss_data(series, data1, data2):
    series_l = len(series)

    eval_param1 = series.loc[0:series_l, data1]  # Getting evaluation parameters
    eval_param2 = series.loc[0:series_l, data2]
    time = series.loc[0:series_l, 'time']

    training_set = np.asarray([eval_param1.iloc[::2], eval_param2.iloc[::2]]).T  # Even indexes for training set
    test_set = np.asarray([eval_param1.iloc[1::2], eval_param2.iloc[1::2]]).T    # Odd indexes for training set

    data_set = np.asarray([eval_param1, eval_param2]).T
    t_time = np.asarray(time).T

    return data_set, training_set, test_set, t_time
