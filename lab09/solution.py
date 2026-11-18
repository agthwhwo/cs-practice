import numpy as np


def make_hours():
    return np.arange(0,22,3).tolist()


def vector_report(values):
    arr = np.array(values)
    return {
        "third": arr[2].tolist(),
        "last": arr[-1].tolist(),
        "middle": arr[2:6].tolist(),
        "every_second": arr[::2].tolist(),
        "reversed": arr[::-1].tolist(),
    }
    
    
def change_vector(values):
    arr = np.array(values)
    new_arr = arr.copy().astype(float)
    new_arr[2:5] = 99
    new_arr[::2] = -1
    return new_arr.tolist()


print(change_vector([0, 3, 6, 9, 12, 15, 18, 21]))
    
    