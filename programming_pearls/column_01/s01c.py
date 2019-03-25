"""
Similar to C version:
Read input lines from a pipe, write output lines into a pipe.

$ cat numbers_small.txt | python s01c.py > numbers_small_sorted.txt
"""
import sys
import numpy as np

a = np.zeros(10_000_000, dtype=int)
for n, line in enumerate(sys.stdin):
    a[n] = int(line)

a[:n].sort(kind='quicksort')  # {mergesort, heapsort}

for x in a[:n]:
    sys.stdout.write(f"{x}\n")
