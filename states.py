import numpy as np
from series_splitting import series_splitting_index
from plotting import dot_plot
from config import *


def create_states(series):
    idx = series_splitting_index(series['time'])  # series borders

    series_states_array = np.zeros((len(idx) - 1, 1)).astype(np.object)   # array of states for all series

    delta_x = (x_max - x_min) / g_x_points  # Hypercube side
    delta_y = (y_max - y_min) / g_y_points

    for n in range(0, len(idx) - 1):  # Number of series
        temp_states = np.zeros((g_y_points, g_x_points))  # temp cell array of states
        temp_states = temp_states.astype(np.object)

        temp_series = series.iloc[idx[n]:idx[n + 1], :]     # temp series for creating states
        temp_series = temp_series.reset_index(drop=True)
        # temp_series_l = len(temp_series)

        x_min_temp = x_min  # Current state x_min
        x_max_temp = x_min + delta_x  # Current state x_max
        y_min_temp = y_max - delta_y  # Current state y_min
        y_max_temp = y_max  # Current state y_max
        print(n)
        data1 = series.loc[idx[n]:idx[n + 1] - 1, g_param1]
        data2 = series.loc[idx[n]:idx[n + 1] - 1, g_param2]
        data1 = data1.reset_index(drop=True)
        data2 = data2.reset_index(drop=True)
        # dot_plot(data1, data2, n)
        for k in range(0, len(data1)):
            for i in range(0, g_x_points):
                flag = False
                for j in range(0, g_y_points):
                    if (data1[k] > x_min_temp) and (data1[k] < x_max_temp) and (data2[k] > y_min_temp) and (
                            data2[k] < y_max_temp):
                        temp_vec = np.array([[data1[k]], [data2[k]]])
                        if np.all(temp_states[i][j] == 0):
                            temp_states[i][j] = temp_vec
                            flag = True
                            break
                        else:
                            temp_states[i][j] = np.c_[temp_states[i][j], temp_vec]
                            flag = True
                            break
                    x_min_temp = x_max_temp  # Changing the x limit
                    x_max_temp = x_max_temp + delta_x

                if flag == True:
                    break
                y_max_temp = y_min_temp  # Changing the row
                y_min_temp = y_min_temp - delta_y
                x_min_temp = x_min
                x_max_temp = x_min + delta_x

            x_min_temp = x_min  # Current state x_min
            x_max_temp = x_min + delta_x  # Current state x_max

            y_min_temp = y_max - delta_y  # Current state y_min
            y_max_temp = y_max  # Current state y_max

        series_states_array[n, 0] = temp_states

    return series_states_array


# def create_states(series, x_points, y_points, x_min, x_max, y_min, y_max):
#     states = np.zeros((y_points, x_points))  # Cell array of states
#     states = states.astype(np.object)
#
#     delta_x = (x_max - x_min) / x_points  # Hypercube side
#     delta_y = (y_max - y_min) / y_points
#
#     brd_idx = series_splitting_index(series['time'])  # Series borders
#     for n in range(0, len(brd_idx) - 1):
#         x_min_temp = x_min  # Current state x_min
#         x_max_temp = x_min + delta_x  # Current state x_max
#         y_min_temp = y_max - delta_y  # Current state y_min
#         y_max_temp = y_max  # Current state y_max
#         # print(n)
#         data1 = series.loc[brd_idx[n]:brd_idx[n + 1] - 1, 'angle_knee']
#         data2 = series.loc[brd_idx[n]:brd_idx[n + 1] - 1, 'angle_hip']
#         data1 = data1.reset_index(drop=True)
#         data2 = data2.reset_index(drop=True)
#         for k in range(0, len(data1)):
#             for i in range(0, x_points):
#                 flag = False
#                 for j in range(0, y_points):
#                     if (data1[k] > x_min_temp) and (data1[k] < x_max_temp) and (data2[k] > y_min_temp) and (
#                             data2[k] < y_max_temp):
#                         temp_vec = np.array([[data1[k]], [data2[k]]])
#                         if np.all(states[i][j] == 0):
#                             states[i][j] = temp_vec
#                             flag = True
#                             break
#                         else:
#                             states[i][j] = np.c_[states[i][j], temp_vec]
#                             flag = True
#                             break
#                     x_min_temp = x_max_temp  # Changing the x limit
#                     x_max_temp = x_max_temp + delta_x
#
#                 if flag == True:
#                     break
#                 y_max_temp = y_min_temp  # Changing the row
#                 y_min_temp = y_min_temp - delta_y
#                 x_min_temp = x_min
#                 x_max_temp = x_min + delta_x
#
#             x_min_temp = x_min  # Current state x_min
#             x_max_temp = x_min + delta_x  # Current state x_max
#
#             y_min_temp = y_max - delta_y  # Current state y_min
#             y_max_temp = y_max  # Current state y_max
#
#     return states
