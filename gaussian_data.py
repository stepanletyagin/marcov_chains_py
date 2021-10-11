import numpy as np
from config import *


def gauss_data(series):
    series_l = len(series)

    angle_knee = series.loc[0:series_l, 'angle_knee']
    angle_hip = series.loc[0:series_l, 'angle_hip']

    t_set = np.asarray([angle_knee, angle_hip]).T
    time = np.atleast_2d(np.arange(0, len(series) * tau, tau)).T

    return time, t_set

