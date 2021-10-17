from config import *
from series_splitting import series_splitting_index
import numpy as np
from scipy.interpolate import interp1d
import pandas as pd


def time_resampling(values):
    values = values.T
    idx = series_splitting_index(values['time'])  # values.iloc['time']
    series_inter = pd.DataFrame(columns=values.columns)
    temp_series_inter = pd.DataFrame(columns=values.columns)

    for i in range(0, len(idx) - 1):    # Number of series
        temp_series = values.iloc[idx[i]:idx[i + 1], :]
        temp_series = temp_series.drop_duplicates()
        temp_series = temp_series.reset_index(drop=True)
        interp_time = np.arange(min(temp_series['time']), max(temp_series['time']), tau)

        columns = list(temp_series)
        if len(interp_time) % 2 == 0:
            for k in columns:
                f = interp1d(temp_series['time'], temp_series[k])
                temp_series_inter[k] = f(interp_time)
        else:
            for k in columns:
                f = interp1d(temp_series['time'], temp_series[k])  # Because fit and GPR works only for same dimensions
                temp_series_inter[k] = f(interp_time[:-1])

                # The python interp1d doesn't have query points in itself,
                # but instead creates a function which you then use to get your new data points

        series_inter = pd.concat([series_inter, temp_series_inter], ignore_index=True)
        temp_series_inter = temp_series_inter.iloc[0:0]     # Clear temp DataFrame

    return series_inter
