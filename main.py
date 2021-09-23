from config import *
from importfile import importdata
from assigning_values import assign_val
from resampling import time_resampling
from states import create_states
from plotting import *


data_union = importdata(file)

values = assign_val(data_union, movement_type)

# dot_plot(values.loc['angle_knee'], values.loc['angle_hip'], movement_type)

series = time_resampling(values)

states = create_states(series, x_points, y_points, x_min, x_max, y_min, y_max)

line_plot(series['time'], series['angle_knee'], movement_type, 'time', 'knee angle')

# print(series)
