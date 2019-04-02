"""
Missing integer in a sorted array.

Given an array of numbers and a range,
return one of the missing integers, if there is one
and return None if there none.
"""


def find_missing_brute(a, rmin, rmax):
    g = rmin
    for x in a:
        if g != x:
            return g
        g += 1
    if x != rmax:
        return rmax
    return None


def find_missing(a, rmin, rmax):
    """indices of a: [lo, ..., mil, mir, ..., hi]."""
    lo = 0
    hi = len(a) - 1

    while lo <= hi:
        mil = (lo + hi) // 2
        mir = mil + 1

        if a[lo] > rmin:
            return rmin

        elif a[hi] < rmax:
            return rmax

        elif a[mir] - a[mil] > 1:
            return a[mil] + 1

        elif mir > hi:  # len(a) == 1
            return None

        elif a[mil] - a[lo] > mil - lo:
            hi = mil
            rmax = a[mil]

        elif a[hi] - a[mir] > hi - mir:
            lo = mir
            rmin = a[mir]

        else:
            return None  # or mistake :-)


func = find_missing
assert func([0, 1, 2, 3], 0, 3) is None
assert func([1, 2, 3], 0, 3) == 0
assert func([1, 2, 3], 1, 3) is None
assert func([2, 3, 4, 6], 2, 6) == 5
assert func([2, 3, 4, 5], 2, 6) == 6
assert func([2, 3, 4, 5], 2, 8) is not None
