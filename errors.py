

def standard_error(experiment_data, predicted_data):
    standard_err = 0
    for i in range(0, len(predicted_data)):
        standard_err = (experiment_data[i] - predicted_data[i])**2 + standard_err

    standard_err = (standard_err / len(predicted_data))**0.5

    return standard_err

