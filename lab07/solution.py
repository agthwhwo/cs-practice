import numpy as np

def reshape_rows(values,width):
    result = np.asarray(values,dtype = float)
    if width <= 0 or result.size % width != 0:
        return list()
    else:
        return result.reshape(-1,width).tolist()


def block(matrix,rows,columns):
    result = np.asarray(matrix,dtype = float)
    if result.size != 0:
        return result[np.ix_(rows,columns)].tolist()
    else:
        return list()


def column_means(matrix):
    result = np.asarray(matrix,dtype = float)
    if result.size != 0:
        return np.round(result.mean(axis=0),6).tolist()
    else:
        return []
