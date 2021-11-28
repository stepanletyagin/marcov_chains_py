from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.model_selection import GridSearchCV
import numpy as np
from numpy import concatenate
from series_splitting import series_splitting_index
from gaussian_data import gauss_data_spl
from errors import standard_error
from config import *


def gaussian_process_prediction_spl(series):
    # kernel = C() * Exp(length_scale=24, periodicity=0.1)
    # kernel = DotProduct() + WhiteKernel()
    # kernel = RBF(length_scale=1) + WhiteKernel(noise_level=0)
    gp = GaussianProcessRegressor(kernel=kernel_1, n_restarts_optimizer=10)

    idx = series_splitting_index(series['time'])           # series borders
    predict_states_val_count = np.zeros((len(idx), 1))     # number of predicted "states" in each series (only for plotting)
    data_with_predicted_states = np.zeros((idx[-1], 2))    # series with predicted states
    # standard_err = np.empty((len(idx), 2), dtype=float)

    for i in range(0, len(idx) - 1):  # Number of series
        temp_series = series.iloc[idx[i]:idx[i + 1], :]
        temp_series = temp_series.reset_index(drop=True)
        temp_series_l = len(temp_series)
        train_set, val_set, test_set = gauss_data_spl(temp_series)  # data preparation

        # gp = GaussianProcessRegressor()
        # grid_search = GridSearchCV(gp, param_grid=param_grid)
        # grid_search.fit(train_time, train_set)  # Prediction methods
        # print(grid_search.best_params_)

        gp.fit(train_set, val_set)  # prediction methods
        prediction = gp.predict(test_set)

        # standard_err[i, 0] = standard_error(data_set[:, 0], prediction[:, 0])  # STD
        # standard_err[i, 1] = standard_error(data_set[:, 1], prediction[:, 1])

        # filling predicted states
        temp_series.loc[temp_series_l - len(test_set):temp_series_l - 1, g_param1] = prediction[:, 0]
        temp_series.loc[temp_series_l - len(test_set):temp_series_l - 1, g_param2] = prediction[:, 1]
        data_with_predicted_states[idx[i]:idx[i + 1]] = temp_series.loc[0:temp_series_l, g_param1:g_param2]

        predict_states_val_count[i] = len(prediction)

    return data_with_predicted_states, idx, predict_states_val_count
