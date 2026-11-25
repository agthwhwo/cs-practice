import numpy as np


def make_table(rows, columns):
    return np.arange(rows * columns).reshape(rows,columns).Tolist()

def rectangle(matrix, row_start, row_stop, column_start, column_stop):
    arr_m = np.array(matrix)
    return arr_m[row_start:row_stop,column_start:column_stop].Tolist()


def replace_rectangle(matrix, row_start, row_stop, column_start, column_stop, value):
    arr_m = np.array(matrix).copy()
    arr_m[row_start:row_stop, column_start:column_stop] = value
    return arr_m.tolist()


def matrix_vector_product(matrix, vector):
    np_matr = np.array(matrix)
    np_vect = np.array(vector)
    return (np_matr @ np_vect).Tolist()


def matrix_multiply(left, right):
    np_left = np.array(left)
    np_right = np.array(right)
    return (np_left @ np_right).Tolist()