from config import *
from importfile import importdata
from assigning_values import assign_val
from resampling import time_resampling
from Gaussian_prediction import gaussian_process_prediction_spl
from gaussian_data import gauss_data_spl
from errors import standard_error
from output import df_to_excel
import time
from states import create_states
from plotting import *


start_time = time.time()  # time of compilation

data_union = importdata(file)
values = assign_val(data_union, movement_type)
# dot_plot(values.loc['angle_knee'], values.loc['angle_hip'], movement_type)


series = time_resampling(values)
# df_to_excel(series)
# hist(series['angle_knee'], series['angle_hip'])

predicted_values, series_borders, predict_states_val_count, STD, MAX, MAE = gaussian_process_prediction_spl(series)
gpp_plot(series, predicted_values, series_borders, predict_states_val_count, STD[:, 0], MAX[:, 0], MAE[:, 0], g_param1)
gpp_plot(series, predicted_values, series_borders, predict_states_val_count, STD[:, 1], MAX[:, 1], MAE[:, 1], g_param2)
# gpp_dot_plot(series.loc[:, g_param1:g_param2], predicted_values, movement_type)

print("--- %s seconds ---" % (time.time() - start_time))

# states = create_states(series, x_points, y_points, x_min, x_max, y_min, y_max)
# line_plot(series['time'], series['angle_knee'], movement_type, 'time', 'knee angle')