# python main.py < input.txt | diff output.txt -

import sys

n_cases = int(sys.stdin.readline())
for _ in range(n_cases):
    n_targets = int(sys.stdin.readline())
    positions = [int(s) for s in sys.stdin.readline().split(' ')]
    target_range = max(positions) - min(positions)
    min_travel_distance = 2 * target_range
    print(min_travel_distance)
