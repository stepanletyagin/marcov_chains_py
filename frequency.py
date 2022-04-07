import numpy as np
from series_splitting import series_splitting_index
from plotting import dot_plot
from tensor_operations import space_tensor_size
from config import *


def create_freq_matrix(series):
    idx = series_splitting_index(series['time'])  # series borders

    series_freq_array = np.zeros((len(idx) - 1, 1)).astype(np.object)  # array of freq for all series

    freq_matrix_len = g_y_points * g_x_points
    delta_x = (x_max - x_min) / g_x_points  # Hypercube side
    delta_y = (y_max - y_min) / g_y_points

    for n in range(0, len(idx) - 1):  # Number of series
        temp_freq_matrix = np.zeros((freq_matrix_len, freq_matrix_len))  # temp frequencies array of states
        temp_freq_matrix = temp_freq_matrix.astype(np.object)

        temp_series = series.iloc[idx[n]:idx[n + 1], :]  # temp series for creating states
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
                        if k == 0:  # Разобраться с первым элементом серии
                            seq_idx_cur = i * g_x_points + j  # Sequence num of elem in matrix (x_points - num of col)
                        else:
                            seq_idx_last = seq_idx_cur
                            seq_idx_cur = i * g_x_points + j
                            temp_freq_matrix[seq_idx_last][seq_idx_cur] += 1
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

        series_freq_array[n, 0] = temp_freq_matrix

    return series_freq_array


def create_freq_tensor(series):
    series_freq_array = np.zeros((len(series), 1)).astype(np.object)    # array of freq for all series

    freq_tensor_len = space_tensor_size(len(series[0, 0][:]))
    delta_x = (x_max - x_min) / g_x_points                              # Hypercube side
    delta_y = (y_max - y_min) / g_y_points

    for n in range(0, len(series)):                                     # Number of series
        temp_freq_tensor = np.zeros(freq_tensor_len, dtype='uint8')     # temp frequencies array of states

        temp_series = series[n, 0]                                      # temp series for creating states
        # temp_series_l = len(temp_series)

        x_min_temp = x_min  # Current state x_min
        x_max_temp = x_min + delta_x  # Current state x_max
        y_min_temp = y_max - delta_y  # Current state y_min
        y_max_temp = y_max  # Current state y_max
        print(n)
        # dot_plot(data1, data2, n)

    return series_freq_array
