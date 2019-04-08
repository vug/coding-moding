"""
https://github.com/vug/coding-moding/wiki/Largest-Rectangle-in-Skyline-%28or-Histogram%29
"""


def largest_rectangle_brute3(a):
    areas = []
    for k in range(len(a)):
        for l in range(k + 1, len(a)):
            h = min(a[k:l])
            area = h * (l - k)
            areas.append(area)
    return max(areas)


def largest_rectangle_brute(a, debug=False):
    areas = []
    for j, h in enumerate(a):
        i = j - 1
        while i >= 0 and a[i] >= a[j]:
            i -= 1
        k = j + 1
        while k < len(a) and a[k] >= a[j]:
            k += 1
        area = h * (k - i - 1)
        if debug:
            print((j, h), (i, k), k - i - 1, area)
        areas.append(area)
    return max(areas)


def all_nearest_smaller_left_indices(a):
    r, s, ix = [], [], 0
    while ix < len(a):
        while s and a[s[-1]] >= a[ix]:
            s.pop()
        if not s:
            r.append(-1)
        else:
            r.append(s[-1])
        s.append(ix)
        ix += 1
    return r


def all_nearest_smaller_right_indices(a):
    r, s, ix = [], [], len(a) - 1
    while ix > -1:
        while s and a[s[-1]] >= a[ix]:
            s.pop()
        if not s:
            r.append(len(a))
        else:
            r.append(s[-1])
        s.append(ix)
        ix -= 1
    r.reverse()
    return r


def largest_rectangle(a, debug=False):
    i_left = all_nearest_smaller_left_indices(a)
    i_right = all_nearest_smaller_right_indices(a)
    if debug:
        print(a, i_left, i_right)
    area_max = -1
    for il, ir, h in zip(i_left, i_right, a):
        w = ir - il - 1
        area = w * h
        area_max = max(area_max, area)
    return area_max


if __name__ == "__main__":
    a = [1, 0, 2, 1, 4, 3, 3, 2, 3, 1, 2]
    print(
        a, largest_rectangle_brute3(a), largest_rectangle_brute(a), largest_rectangle(a)
    )

    from itertools import product

    cases = product([0, 1, 2, 3], repeat=4)
    for c in cases:
        if largest_rectangle_brute(c) != largest_rectangle(c):
            print(
                c,
                largest_rectangle_brute(c, debug=True),
                largest_rectangle(c, debug=True),
            )
