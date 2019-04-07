def nsv(a, ix):
    iy = ix - 1
    while iy >= 0:
        if a[iy] < a[ix]:
            return (iy, a[iy])
        iy -= 1
    return (None, None)  # return (-1, None)


def nsv_backward(a, ix):
    iy = ix + 1
    while iy < len(a):
        if a[iy] < a[ix]:
            return (iy, a[iy])
        iy += 1
    return (None, None)  # return (-1, None)


def all_nearest_smaller_values_brute(a, is_forward=True, exceed_index=False):
    r = []
    for ix, x in enumerate(a):
        if is_forward:
            iy, y = nsv(a, ix)
        else:
            iy, y = nsv_backward(a, ix)
        if exceed_index and iy is None:
            iy = -1 if is_forward else len(a)
        r.append((iy, y))
    return r


def all_nearest_smaller_values(a):
    r, s = [], []
    for ix, x in enumerate(a):
        while s and s[-1][1] >= x:
            s.pop()
        if not s:
            r.append((None, None))  # (-1, None)
        else:
            r.append(s[-1])
        s.append((ix, x))
    return r


print(all_nearest_smaller_values_brute([2, 5, 7, 3, 3, 5, 4, 6, 1]))
print(all_nearest_smaller_values([2, 5, 7, 3, 3, 5, 4, 6, 1]))
print(all_nearest_smaller_values_brute([2, 5, 7, 3, 3, 5, 4, 6, 1], exceed_index=True))
print(all_nearest_smaller_values_brute([2, 5, 7, 3, 3, 5, 4, 6, 1], is_forward=False))
print(
    all_nearest_smaller_values_brute(
        [2, 5, 7, 3, 3, 5, 4, 6, 1], is_forward=False, exceed_index=True
    )
)
print(all_nearest_smaller_values_brute([]))
