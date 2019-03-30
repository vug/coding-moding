import logging

# import random

# n = 10
# m = 20
# all_nums = list(range(m))
# random.shuffle(all_nums)
# nums = all_nums[:n]
# nums.sort()

nums = [1, 2, 3, 5, 7, 8, 10, 14, 15, 17]
logging.basicConfig(level=logging.DEBUG)
logging.debug(nums)


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


# print(binary_search([1, 2, 3, 5, 7, 8, 10, 14, 15, 17], 2))
# print(binary_search([1, 2, 3, 5, 7, 8, 10, 14, 15, 17], 4))
print(binary_search([1, 2, 3], 1))

# TODO: https://github.com/vug/coding-moding/projects/5
