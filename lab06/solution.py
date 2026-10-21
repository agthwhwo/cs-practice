def count_items(values):
    result = dict()
    for value in values:
        result[value] = result.get(value,0) + 1
    return result

def unique_sorted(values):
    return sorted(set(values))

def common(first,second):
    return sorted(set(first) &  set(second))


def only_in_first(first,second):
    return sorted(set(first) - set(second))