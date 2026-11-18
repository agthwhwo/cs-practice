import numpy as np


def make_hours():
    return np.arange(0,22,3).tolist()


def vector_report(values):
    arr = np.asarray(values)
    return {
        "third": arr[2].tolist(),
        "last": arr[-1].tolist(),
        "middle": arr[2:6].tolist(),
        "every_second": arr[::2].tolist(),
        "reversed": arr[::-1].tolist(),
    }
    
    
def change_vector(values):
    arr = np.asarray(values)
    new_arr = arr.copy()
    new_arr[2:5] = 99
    new_arr[::2] = -1
    return new_arr.tolist()



def cap_above(values, limit):
    arr = np.asarray(values)
    new_arr = arr.copy()
    new_arr[new_arr > limit] = limit
    return new_arr.tolist()

    
    
def celsius_to_fahrenheit(values):
    arr = np.asarray(values)
    return (arr * 9 / 5 + 32).tolist()