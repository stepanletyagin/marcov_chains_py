from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, ConstantKernel as C, RationalQuadratic as RQ, WhiteKernel, \
    ExpSineSquared as Exp, DotProduct
import numpy as np
from series_splitting import series_splitting_index
from plotting import *
from config import *


def gaussian_process_prediction(t_set, t_time):

    # Gaussian process set
    # kernel = C() * Exp(length_scale=24, periodicity=0.1)
    kernel = DotProduct() + WhiteKernel()
    # kernel = RBF(length_scale=1) + WhiteKernel(noise_level=eps)
    gp = GaussianProcessRegressor(kernel=kernel, n_restarts_optimizer=4)

    idx = series_splitting_index(t_time)  # Series borders
    predicted_states = np.empty((idx[-1], 2), dtype=float)
    # experimental_states = np.empty((int(idx[-1] / 2), 2), dtype=float)
    # predicted_states = np.empty((int(idx[-1] / 2), 2), dtype=float)

    for i in range(0, len(idx) - 1):  # Number of series
        temp_series = t_set[idx[i]:idx[i + 1], :]  # Teaching set for current series

        n = len(temp_series)
        training_df = temp_series[0:int(n * 0.5)]
        result_df = temp_series[int(n * 0.5):int(n)]
        # test_df = temp_series[int(idx[i + 1] * 0.9):]

        gp.fit(training_df, result_df)
        prediction = np.asarray(gp.predict(temp_series))
        predicted_states[idx[i]:idx[i + 1]] = prediction

        gpp_plot(t_time[idx[i]:idx[i + 1]], temp_series, t_time[idx[i]:idx[i + 1]], prediction, i)

    return predicted_states
