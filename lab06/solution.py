def count_times(values):
    result = dict()
    for value in values:
        result[value] = result.get(value,0) + 1
    return result

def unique_sorted(values):
    return sorted(set(values))

