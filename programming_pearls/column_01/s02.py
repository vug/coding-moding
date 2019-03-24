import array
import math

# import numpy as np

BITS_PER_WORD = 32
SHIFT = int(math.log2(BITS_PER_WORD))  # 5
MASK = BITS_PER_WORD - 1  # 0x1F == 31
ALL_ONES = 2 ** 32 - 1


def set1(a, i):
    ix = i // BITS_PER_WORD
    w = 1 << i % BITS_PER_WORD
    a[ix] |= w


def set(a, i):
    a[i >> SHIFT] |= 1 << (i & MASK)


def clr1(a, i):
    ix = i // BITS_PER_WORD
    w = 1 << i % BITS_PER_WORD
    a[ix] &= ALL_ONES - w  # RHS is bitwise NOT operation


def clr(a, i):
    a[i >> SHIFT] &= ALL_ONES - (1 << (i & MASK))


def test(a, i):
    return a[i >> SHIFT] & 1 << (i & MASK) > 0


a = array.array("I", (0 for _ in range(10_000_000 // 4)))
print(a.buffer_info(), a.itemsize)
# a = np.zeros(10_000_000 // 4, dtype=np.dtype("uint32"))
# print(a.itemsize, a.nbytes, a.nbytes / a.itemsize)

set(a, 3)
set(a, 5)
set(a, 11)
set(a, 31)
set(a, 33)
set(a, 60)
set(a, 62)

print("".join([str(x) for x in list(range(10))[::-1]] * 10)[-64:])
print(f"{a[1]:032b}" + f"{a[0]:032b}")

clr(a, 60)
clr(a, 32)
clr(a, 31)

print("".join([str(x) for x in list(range(10))[::-1]] * 10)[-64:])
print(f"{a[1]:032b}" + f"{a[0]:032b}")


print(31, test(a, 31))
print(33, test(a, 33))
