def max_odd(array):
    subarr = []
    for i in array:
        if isinstance(i, int | float) and i % 2 != 0:
            subarr.append(i)
    if len(subarr) == 0:
        return None
    return int(max(subarr))


