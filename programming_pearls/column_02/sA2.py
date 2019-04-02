"""
Missing integer in non-sorted array

Use memory and binary-search to solve it still in O(log N)
even though the array is not sorted.
"""


def find_missing_brute(a, rmin, rmax):
    a.sort()
    g = rmin
    for x in a:
        if g != x:
            return g
        g += 1
    if x != rmax:
        return rmax
    return None


def find_missing(a, rmin, rmax):
    while rmin <= rmax:
        rmidl = (rmax + rmin) // 2
        rmidr = rmidl + 1

        lows = [x for x in a if rmin <= x <= rmidl]
        highs = [x for x in a if rmidr <= x <= rmax]

        if len(lows) == 0:
            return rmin
        
        if len(highs) == 0:
            return rmax

        if highs[0] - lows[-1] > 1:
            return lows[-1] + 1

        if rmidl - rmin + 1 > len(lows):
            rmax = rmidl
            a = lows
        
        elif rmax - rmidr + 1 > len(highs):
            rmin = rmidr
            a = highs
        
        else:
            return None
    
    return rmin, rmax


print(find_missing([1, 2, 3], 1, 3))
