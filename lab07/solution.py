import numpy as np

def reshape_rows(values,width):
    result = np.asarray(values,dtype = float)
    if width <= 0 or result.size % width != 0:
        return []

    return result.reshape(-1,width).tolist()
