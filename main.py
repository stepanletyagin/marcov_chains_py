from config import *
from importfile import importdata
from assigning_values import assign_val
from resampling import time_resampling
from Gaussian_prediction import gaussian_process_prediction
from gaussian_data import gauss_data
from errors import standard_error
from output import df_to_excel
import time
from states import create_states
from plotting import *


start_time = time.time()  # Time of compilation

data_union = importdata(file)
values = assign_val(data_union, movement_type)
# dot_plot(values.loc['angle_knee'], values.loc['angle_hip'], movement_type)


series = time_resampling(values)
# df_to_excel(series)
# hist(series['angle_knee'], series['angle_hip'])

data_set, training_set, test_set, series_time = gauss_data(series, param1, param2)
predicted_values, standard_err, series_borders = gaussian_process_prediction(series, param1, param2)

gpp_series_plot(data_set[:, 0], predicted_values[:, 0], series_time, series_borders,
                standard_err[:, 0], movement_type, param1)
gpp_series_plot(data_set[:, 1], predicted_values[:, 1], series_time, series_borders,
                standard_err[:, 1], movement_type, param2)
gpp_dot_plot(data_set, predicted_values, movement_type)

standard_err_knee = standard_error(data_set[:, 0], predicted_values[:, 0])
standard_err_hip = standard_error(data_set[:, 1], predicted_values[:, 1])
print("--- %s standard_err_knee ---" % standard_err_knee)
print("--- %s standard_err_hip ---" % standard_err_hip)

# states = create_states(series, x_points, y_points, x_min, x_max, y_min, y_max)
# line_plot(series['time'], series['angle_knee'], movement_type, 'time', 'knee angle')

print("--- %s seconds ---" % (time.time() - start_time))
