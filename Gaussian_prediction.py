from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, ConstantKernel as C, RationalQuadratic as RQ, WhiteKernel, \
    ExpSineSquared as Exp, DotProduct
from gaussian_data import gauss_data
import numpy as np
from config import *


def Gaussian_Process_Prediction(time, t_set, size):

    kernel = C() * Exp(length_scale=24, periodicity=1)
    gp = GaussianProcessRegressor(kernel=kernel, n_restarts_optimizer=4)

    # time, t_set = gauss_data(series)  # teaching set for n series

    gp.fit(time, t_set)  # teaching method
    pr_time = np.atleast_2d(np.linspace(0, size, 10739)).T  # prediction time

    pred, sigma = gp.predict(pr_time, return_std=True)

    return pred, sigma, pr_time
