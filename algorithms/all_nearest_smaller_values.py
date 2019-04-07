from data_structures.stack import Stack


def nsv(a, ix):
    """Get nearest smaller (index, value) of a[ix] towards left."""
    iy = ix - 1
    while iy >= 0:
        if a[iy] < a[ix]:
            return (iy, a[iy])
        iy -= 1
    return (None, None)  # return (-1, None)


def nsv_backward(a, ix):
    """Get nearest smaller (index, value) of a[ix] towards right."""
    iy = ix + 1
    while iy < len(a):
        if a[iy] < a[ix]:
            return (iy, a[iy])
        iy += 1
    return (None, None)  # return (-1, None)


def all_nearest_smaller_values_brute(a, is_forward=True, exceed_index=False):
    """Brute-force computation of all nearest smaller values of array a."""
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
    """White board computation of all nearest smaller values of array a."""
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


def all_nearest_smaller_values_v2(a):
    """Compute all nearest smaller values of array a using a Stack."""
    r = []
    s = Stack()
    for ix, x in enumerate(a):
        while not s.is_empty() and s.peek()[1] >= x:
            s.pop()
        if s.is_empty():
            r.append((None, None))  # (-1, None)
        else:
            r.append(s.peek())
        s.push((ix, x))
    return r


# Some simple tests that does not use Stack version.
if __name__ == "__main__":
    print(all_nearest_smaller_values_brute([2, 5, 7, 3, 3, 5, 4, 6, 1]))
    print(all_nearest_smaller_values([2, 5, 7, 3, 3, 5, 4, 6, 1]))
    print(all_nearest_smaller_values_v2([2, 5, 7, 3, 3, 5, 4, 6, 1]))
    print(
        all_nearest_smaller_values_brute([2, 5, 7, 3, 3, 5, 4, 6, 1], exceed_index=True)
    )
    print(
        all_nearest_smaller_values_brute([2, 5, 7, 3, 3, 5, 4, 6, 1], is_forward=False)
    )
    print(
        all_nearest_smaller_values_brute(
            [2, 5, 7, 3, 3, 5, 4, 6, 1], is_forward=False, exceed_index=True
        )
    )
    print(all_nearest_smaller_values_brute([]))
