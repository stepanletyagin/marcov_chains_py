import numpy as np
from series_splitting import series_splitting_index


def create_states(series, x_points, y_points, x_min, x_max, y_min, y_max):
    states = np.zeros((y_points, x_points))  # Cell array of states
    states = states.astype(np.object)

    delta_x = (x_max - x_min) / x_points  # Hypercube side
    delta_y = (y_max - y_min) / y_points

    brd_idx = series_splitting_index(series['time'])  # Series borders
    for n in range(0, len(brd_idx) - 1):
        x_min_temp = x_min  # Current state x_min
        x_max_temp = x_min + delta_x  # Current state x_max
        y_min_temp = y_max - delta_y  # Current state y_min
        y_max_temp = y_max  # Current state y_max
        # print(n)
        data1 = series.loc[brd_idx[n]:brd_idx[n + 1] - 1, 'angle_knee']
        data2 = series.loc[brd_idx[n]:brd_idx[n + 1] - 1, 'angle_hip']
        data1 = data1.reset_index(drop=True)
        data2 = data2.reset_index(drop=True)
        for k in range(0, len(data1)):
            for i in range(0, x_points):
                flag = False
                for j in range(0, y_points):
                    if (data1[k] > x_min_temp) and (data1[k] < x_max_temp) and (data2[k] > y_min_temp) and (
                            data2[k] < y_max_temp):
                        temp_vec = np.array([[data1[k]], [data2[k]]])
                        if np.all(states[i][j] == 0):
                            states[i][j] = temp_vec
                            flag = True
                            break
                        else:
                            states[i][j] = np.c_[states[i][j], temp_vec]
                            flag = True
                            break
                    x_min_temp = x_max_temp  # Changing the x limit
                    x_max_temp = x_max_temp + delta_x

                if flag == True:
                    break
                y_max_temp = y_min_temp  # Changing the row
                y_min_temp = y_min_temp - delta_y
                x_min_temp = x_min
                x_max_temp = x_min + delta_x

            x_min_temp = x_min  # Current state x_min
            x_max_temp = x_min + delta_x  # Current state x_max

            y_min_temp = y_max - delta_y  # Current state y_min
            y_max_temp = y_max  # Current state y_max

    return states
