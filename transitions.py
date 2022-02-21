import numpy as np
from config import *


def create_trans_matrix(freq_matrix_arr):
    trans_matrix_arr = np.zeros((len(freq_matrix_arr), 1)).astype(np.object)
    row_sum_arr = np.zeros((len(freq_matrix_arr), 1)).astype(np.object)     # Sum of prob on each row
    trans_matrix_len = x_points * y_points                                  # transition matrix size

    for i in range(len(freq_matrix_arr)):
        row_sum_arr[i][0] = (np.sum(freq_matrix_arr[i][0], axis=1))         # sum of each row of each freq matrix


    for n in range(len(freq_matrix_arr)):
        temp_trans_matrix = np.zeros((trans_matrix_len, trans_matrix_len)).astype(np.object)  # current transition mat
        temp_freq_matrix_arr = freq_matrix_arr[n, 0].astype(np.object)                        # current freq mat
        temp_row_sum_arr = row_sum_arr[n][0]                                          # current row sum of freq matrix

        for i in range(trans_matrix_len):           # creating freq matrix
            for j in range(trans_matrix_len):
                if temp_row_sum_arr[i] == 0:
                    break
                else:
                    temp_trans_matrix[i][j] = temp_freq_matrix_arr[i][j] / temp_row_sum_arr[i]
        # print(np.sum(temp_trans_matrix, axis=1))
        # print('########')
        trans_matrix_arr[n, 0] = temp_trans_matrix

    return trans_matrix_arr
