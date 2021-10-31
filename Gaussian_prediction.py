from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, ConstantKernel as C, RationalQuadratic as RQ, WhiteKernel, \
    ExpSineSquared as Exp, DotProduct
import numpy as np
from series_splitting import series_splitting_index
from gaussian_data import gauss_data
from plotting import *
from errors import standard_error
from config import *


def max_difference_search(arr):

    max_difference = arr[0]

    for i in range(0, len(arr) - 1):
        current_difference = abs(arr[i] - arr[i + 1])
        if current_difference > max_difference:
            max_difference = current_difference

    return max_difference


def gaussian_process_prediction(series, data1, data2):

    # Gaussian process set
    kernel = C() * Exp(length_scale=24, periodicity=0.1)
    # kernel = DotProduct() + WhiteKernel()
    # kernel = RBF(length_scale=1) + WhiteKernel(noise_level=0)
    gp = GaussianProcessRegressor(kernel=kernel, n_restarts_optimizer=10)

    idx = series_splitting_index(series['time'])  # Series borders
    predicted_states = np.empty((idx[-1], 2), dtype=float)
    standard_err = np.empty((len(idx), 2), dtype=float)

    # predicted_states_temp_size = max_difference_search(idx)

    for i in range(0, len(idx) - 1):  # Number of series
        temp_series = series.iloc[idx[i]:idx[i + 1], :]  # Teaching set for current series
        temp_series = temp_series.reset_index(drop=True)
        data_set, training_set, test_set, current_series_time = gauss_data(temp_series, data1, data2)  # Data preparation

        n = len(temp_series)  # temp series length

        gp.fit(training_set, test_set)  # Prediction methods
        prediction = gp.predict(training_set)
        prediction = np.asarray(prediction)

        predicted_states_temp = np.empty((len(prediction) + len(training_set), 2), dtype=float)
        predicted_states_temp[::2] = training_set
        predicted_states_temp[1::2] = prediction

        standard_err[i, 0] = standard_error(data_set[:, 0], predicted_states_temp[:, 0])  # STD
        standard_err[i, 1] = standard_error(data_set[:, 1], predicted_states_temp[:, 1])
        # gpp_plot(current_series_time, data_set, current_series_time, predicted_states_temp, i, standard_err, movement_type)

        predicted_states[idx[i]:idx[i + 1]] = predicted_states_temp[0:n]

    return predicted_states, standard_err, idx
