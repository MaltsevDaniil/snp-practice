def coincidence(lst=(), rng=()):
    res = []
    if lst == res or rng == res:
        return res
    for i in lst:
        if isinstance(i, int | float) and rng[0] <= i <= rng[-1]:
            res.append(i)
    return res
