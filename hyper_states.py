import numpy as np
import itertools
from config import *
# from series_splitting import series_splitting_index


def axis_centers_search(hyper_state_len):
    data = np.zeros((hyper_state_len, 1)).astype(np.object)
    data_list = []
    delta_x = (x_max - x_min) / g_x_points
    delta_y = (y_max - y_min) / g_y_points

    for n in range(0, hyper_state_len):
        if n % 2 == 0:
            data[n, 0] = (np.linspace(x_min + delta_x / 2, x_max - delta_x / 2, g_x_points))
        else:
            data[n, 0] = np.linspace(y_min + delta_y / 2, y_max - delta_y / 2, g_y_points)
        data_list.append(data[n, 0].tolist())
    return data_list


def hypercube_center_search(hyper_states_series, dimension_of_lag_space):
    hyper_states_centers = np.zeros((len(hyper_states_series), 1)).astype(np.object)
    axis_centers_l = axis_centers_search(dimension_of_lag_space)
    centers = np.array(list(itertools.product(*axis_centers_l)))

    for n in range(0, len(hyper_states_series)):
        hyper_states_centers[n, 0] = centers

    return hyper_states_centers
