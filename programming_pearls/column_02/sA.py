"""Missing Integer Problem."""

n_max = 8
a = [0, 1, 2, 3, 5, 6, 7, 8]


def find_missing(a, n_max):
    def count_in_range(a, mn, mx):
        return sum([1 for x in a if mn <= x <= mx])
    lo = 0
    hi = n_max

    while lo <= hi:
        mi = (lo + hi) // 2
        cnt1 = count_in_range(a, 0, mi)
        cnt2 = count_in_range(a, mi + 1, hi)
        print(lo, hi, mi, a[mi], cnt1, cnt2)
        if cnt1 <= cnt2:
            hi = mi
        else:
            lo = mi + 1


find_missing(a, n_max)
