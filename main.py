from config import *
from importfile import importdata
from assigning_values import assign_val
from series_splitting import series_splitting_index
from resampling import time_resampling
from plotting import *


data_union = importdata(file)

values = assign_val(data_union, movement_type)

# dot_plot(values.loc['angle_knee'], values.loc['angle_hip'], movement_type)

series = time_resampling(values)

line_plot(series['time'], series['angle_knee'], movement_type, 'time', 'knee angle')

# print(series)
