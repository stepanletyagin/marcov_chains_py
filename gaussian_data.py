import numpy as np
import pandas as pd
from output import df_to_excel
from config import *


def gauss_data(series):
    series_l = len(series)

    angle_knee = series.loc[0:series_l, 'angle_knee']
    angle_hip = series.loc[0:series_l, 'angle_hip']
    time = series.loc[0:series_l, 'time']

    t_set = np.asarray([angle_knee, angle_hip]).T
    # t_set = np.asarray(angle_knee).T
    # time = np.atleast_2d(np.arange(0, len(series) * tau, tau)).T
    t_time = np.asarray(time).T

    return t_set, t_time

