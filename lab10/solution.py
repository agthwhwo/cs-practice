import numpy as np


def make_table(rows, columns):
    return np.arange(rows * columns).reshape(rows,columns).Tolist()

def rectangle(matrix, row_start, row_stop, column_start, column_stop):
    arr_m = np.array(matrix)
    return arr_m[row_start:row_stop,column_start:column_stop].Tolist()