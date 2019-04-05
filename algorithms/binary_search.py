import bisect
import logging

logging.basicConfig(level=logging.INFO)


def binary_search_rec(indexable, value):  # or sequence
    """Recursive Binary Search."""

    def helper(low, high, value):
        logging.debug(f"low: {low}, high: {high}")
        if low > high:
            return None
        mid = (low + high) // 2  # low + (high - low) // 2
        mid_val = indexable[mid]
        logging.debug(f"mid: {mid}, mid_val: {mid_val}")
        if mid_val == value:
            logging.debug(f"found at {mid}")
            return mid
        elif mid_val < value:
            low = mid + 1
        else:
            high = mid - 1
        return helper(low, high, value)

    return helper(0, len(indexable) - 1, value)


def binary_search(a, x):
    """Iterative Binary Search."""
    lo = 0
    hi = len(a) - 1
    while lo <= hi:
        md = (lo + hi) // 2
        if x == a[md]:
            return md
        elif x < a[md]:
            hi = md - 1
        elif x > a[md]:
            lo = md + 1
    return None


def binary_search_closest(a, x):
    """Get closest value and its index to x in a."""
    if len(a) == 0:
        raise ValueError("Input list can not be empty.")
    lo = 0
    hi = len(a) - 1
    while lo <= hi:
        md = (lo + hi) // 2
        if x == a[md]:
            return md
        elif x < a[md]:
            hi = md - 1
        elif x > a[md]:
            lo = md + 1
    return max([(ix, a[ix]) for ix in [lo, hi] if 0 <= ix < len(a)])


assert binary_search_closest([3], 10) == (0, 3)
assert binary_search_closest([3], -10) == (0, 3)
assert binary_search_closest([1, 2, 3], 10) == (2, 3)
assert binary_search_closest([1, 2, 3], -10) == (0, 1)
try:
    binary_search_closest([], 10)
except ValueError as e:
    print(e)


def binary_search_func(f, n, lo, hi):
    """Integer binary search, but with functions instead of list."""
    while lo <= hi:
        md = (lo + hi) // 2
        if n == f(md):
            return md
        elif n < f(md):
            hi = md - 1
        elif n > f(md):
            lo = md + 1
    return None


assert binary_search_func(lambda x: x * x * x, 8, 0, 10) == 2
assert binary_search_func(lambda x: x * x * x, 27, 0, 10) == 3
assert binary_search_func(lambda x: x * x * x, 5, 0, 10) is None


def binary_search_closest_func(f, x, lo, hi, eps=0.01, num_tries=1000):
    """Search the function input in given range that is closest to x."""
    while lo <= hi:
        md = (lo + hi) / 2
        if abs(x - f(md)) < eps:
            return md
        elif x < f(md):
            hi = md - eps
        elif x > f(md):
            lo = md + eps
    return (md, f(md))


def cube(x):
    return x * x * x


assert abs(binary_search_closest_func(cube, 8, 0.0, 10.0)[0] - 2) < 0.01
assert abs(binary_search_closest_func(cube, 5, 0.0, 10.0)[0] - 1.7) < 0.01
assert abs(binary_search_closest_func(cube, 1_000_000, 0.0, 10.0)[0] - 10) < 0.01


def binary_search_python(a, x):
    """Implement binary search using standard Python library."""
    ix = bisect.bisect_left(a, x)
    if ix < len(a) and a[ix] == x:
        return ix
    return None


assert binary_search_python([1, 2, 3], 1) == 0
assert binary_search_python([1, 2, 3], 3) == 2
assert binary_search_python([1, 2, 3], 4) is None
