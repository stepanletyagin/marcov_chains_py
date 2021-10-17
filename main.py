from config import *
from importfile import importdata
from assigning_values import assign_val
from resampling import time_resampling
from Gaussian_prediction import gaussian_process_prediction
from gaussian_data import gauss_data
from output import df_to_excel
import time
import numpy as np
from states import create_states
from plotting import *
import pandas as pd

start_time = time.time()  # Time

data_union = importdata(file)
values = assign_val(data_union, movement_type)
# dot_plot(values.loc['angle_knee'], values.loc['angle_hip'], movement_type)


series = time_resampling(values)
df_to_excel(series)

# hist(series['angle_knee'], series['angle_hip'])

t_set, t_time = gauss_data(series)
predicted_values = gaussian_process_prediction(t_set, t_time)
gpp_dot_plot(t_set, predicted_values)

# states = create_states(series, x_points, y_points, x_min, x_max, y_min, y_max)
# line_plot(series['time'], series['angle_knee'], movement_type, 'time', 'knee angle')

print("--- %s seconds ---" % (time.time() - start_time))
