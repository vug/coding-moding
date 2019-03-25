"""
Similar to C version:
Read input lines from a pipe, write output lines into a pipe.

$ cat numbers_small.txt | python s01b.py > numbers_small_sorted.txt
"""
import sys

numbers = []
for line in sys.stdin:
    numbers.append(int(line))

numbers.sort()

for n in numbers:
    sys.stdout.write(f"{n}\n")
