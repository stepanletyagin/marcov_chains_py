from sklearn.gaussian_process.kernels import RBF, ConstantKernel as C, RationalQuadratic as RQ, WhiteKernel, \
    ExpSineSquared as Exp, DotProduct


file = 'data.mat'
movement_type = 'Walking'

g_param1 = 'angle_knee'
g_param2 = 'angle_hip'

x_points = 98
y_points = 91
x_min = 0
x_max = 80
y_min = -50
y_max = 31

eps = 0.000001
tau = 1/10  # Interpolation step

test_sample = 0.8
g_window = 3

# Gaussian process set
# kernel_1 = C() * Exp(length_scale=0.1, periodicity=0.1)
# kernel_2 = RBF(length_scale=1.0)
# kernel_3 = WhiteKernel(noise_level=0.09) + 1.41 ** 2 * Exp(length_scale=1, periodicity=40)
# kernel_4 = DotProduct() + WhiteKernel()
# kernel_5 = RBF(length_scale=1) + WhiteKernel(noise_level=0)
# kernel_6 = 1**2 * Exp(length_scale=1, periodicity=5)
#
# k0 = WhiteKernel(noise_level=0.3**2, noise_level_bounds=(0.1**2, 0.5**2))
# k1 = C(constant_value=2) * \
#   Exp(length_scale=1.0, periodicity=40, periodicity_bounds=(35, 45))
# kernel_7 = k0 + k1
#
# kernel_8 = C(1.0, constant_value_bounds="fixed") * RBF(1.0, length_scale_bounds="fixed")
# kernel_9 = C(1.0, constant_value_bounds="fixed") * RQ(alpha=0.1, length_scale=1)
# kernel_10 = C(1.0, constant_value_bounds="fixed") * Exp(1.0, 5.0, periodicity_bounds=(1e-2, 1e1))

kernel_1 = C(constant_value=1e-10, constant_value_bounds=(1e-10, 10)) * RQ(length_scale=500,
                length_scale_bounds=(1e-4, 10), alpha=50.0, alpha_bounds=(1e-4, 10)) + WhiteKernel(noise_level=0.3**2)
kernel_2 = C(constant_value=1e-10) * Exp(length_scale=1, periodicity=1) + WhiteKernel(noise_level=0.3**2)
kernel_3 = C(constant_value=1e-10) * RBF(length_scale=1) + WhiteKernel(noise_level=0.3**2)
kernel_4 = C(constant_value=1e-10) * RBF(length_scale=1) + WhiteKernel(noise_level=0.3**2)
kernel_5 = C(constant_value=1e-10) * RBF(length_scale=1) + WhiteKernel(noise_level=0.3**2)

kernel_7 = C(constant_value=1e-10) * RBF(length_scale=1) + WhiteKernel(noise_level=0.3**2)

kernel_list = [kernel_1, kernel_2, kernel_3, kernel_4, kernel_5, kernel_7]

param_grid = {"kernel": kernel_list,
              "alpha": [0, 1e0],
              "optimizer": ["fmin_l_bfgs_b"],
              "n_restarts_optimizer": [1],
              "normalize_y": [True],
              "copy_X_train": [True],
              "random_state": [0]}
