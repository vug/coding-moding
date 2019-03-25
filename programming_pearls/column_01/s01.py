"""
Get filename via the first argument.

$ python s01.py numbers_small.txt
"""
import sys

fname = sys.argv[1]
with open(fname, "rt") as f:
    lines = f.readlines()  # list[str]

numbers = [int(s) for s in lines]
numbers.sort()

with open(f"{fname.split('.')[0]}_sorted.txt", "wt") as f:
    f.writelines([f"{s}\n" for s in numbers])
