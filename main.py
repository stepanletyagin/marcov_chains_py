from config import *
from importfile import importdata
from assigning_values import assign_val
from resampling import time_resampling
from Gaussian_prediction import Gaussian_Process_Prediction
from gaussian_data import gauss_data
from states import create_states
from plotting import *

import time
start_time = time.time()


data_union = importdata(file)
values = assign_val(data_union, movement_type)
# dot_plot(values.loc['angle_knee'], values.loc['angle_hip'], movement_type)

series = time_resampling(values)


t_time, t_set = gauss_data(series)
predict_vals, sigma, pr_time = Gaussian_Process_Prediction(t_time, t_set, len(series))
gpp_plot(t_time, t_set, predict_vals, pr_time)

# states = create_states(series, x_points, y_points, x_min, x_max, y_min, y_max)
# line_plot(series['time'], series['angle_knee'], movement_type, 'time', 'knee angle')

print("--- %s seconds ---" % (time.time() - start_time))

# print(series)
