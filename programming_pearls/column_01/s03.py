# $ cat numbers_small.txt | python s03.py > numbers_small_sorted.txt
# $ cat numbers_big.txt | python s03.py > numbers_big_sorted.txt
import array
import math
import sys


class BitVector(object):
    def __init__(self, size, bytes_per_word=4):
        self.bits_per_word = bytes_per_word * 8
        self.shift = int(math.log2(self.bits_per_word))  # 5
        self.mask = self.bits_per_word - 1  # 0x1F == 31
        self.all_ones = 2 ** self.bits_per_word - 1
        self.a = array.array("I", (0 for _ in range(size // 4)))

    def set(self, i):
        self.a[i >> self.shift] |= 1 << (i & self.mask)

    def clr(self, i):
        self.a[i >> self.shift] &= self.all_ones - (1 << (i & self.mask))

    def test(self, i):
        return self.a[i >> self.shift] & 1 << (i & self.mask) > 0

    # # Below implementations takes same amount of time and are more readable
    # def set1(self, i):
    #     ix = i // self.bits_per_word
    #     w = 1 << i % self.bits_per_word
    #     self.a[ix] |= w

    # def test1(self, i):
    #     ix = i // self.bits_per_word
    #     w = 1 << i % self.bits_per_word
    #     return self.a[ix] & w > 0


if __name__ == "__main__":
    a = BitVector(10_000_000)

    for n, line in enumerate(sys.stdin):
        a.set1(int(line))
    for x in range(n + 1):
        if a.test1(x):
            sys.stdout.write(f"{x}\n")

    # # Below implementation takes same amount of time
    # with open("numbers_big.txt", "rt") as f:
    #     lines = f.readlines()

    # [a.set(int(line)) for line in lines]

    # with open("numbers_big_sorted2.txt", "wt") as f:
    #     [
    #         f.write(f"{i}\n")
    #         for i in range(len(lines))
    #         if a.test(i)
    #     ]
