from config import *

"""
Функция принимает на вход кол-во глобальных параметров (кол-во переменных в пространстве лагов)
и вычисляет размерность тензора

На выходе массив из одинаковых значений, каждое из которых - кол-во сегментов по каждой переменной.
"""


# def space_tensor_size(lag_space_size):
#     size = 1
#     for n in range(0, int(lag_space_size / 2)):                 # Size of each dimension
#         size = g_x_points * g_y_points * size
#
#     size_tuple = tuple([size for i in range(lag_space_size)])   # array of dimensions size for creating freq tensor
#
#     return size_tuple


def space_tensor_size(lag_space_size):

    size_tuple = tuple([g_x_points if i % 2 == 0 else g_y_points for i in range(lag_space_size)])
    return size_tuple
