"""
Module for some algorithm and data structure implementation tests.
It is placed at project root level so that all intra-package imports in imported
modules run correctly.
"""
from itertools import product

from algorithms.all_nearest_smaller_values import (
    all_nearest_smaller_values,
    all_nearest_smaller_values_v2,
    all_nearest_smaller_values_brute,
)


cases = []
for r in range(5):
    cases.extend(product([1, 3, 5, 7], repeat=r))
for c in cases:
    assert all_nearest_smaller_values_brute(c) == all_nearest_smaller_values(c)
    assert all_nearest_smaller_values_brute(c) == all_nearest_smaller_values_v2(c)
