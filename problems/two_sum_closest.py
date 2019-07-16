"""
Given a list of numbers and a target number
return the pair of indices which of which sum is closest to
the target.

Developed this to study https://leetcode.com/problems/3sum-closest/
"""
import math


def two_sum_closest(nums, target):
    nums.sort()
    left, right = 0, len(nums) - 1
    min_diff = math.inf
    pair = (-1, -1)
    while left < right:
        two_sum = nums[left] + nums[right]
        abs_diff = abs(target - two_sum)
        if abs_diff < min_diff:
            min_diff = abs_diff
            pair = (left, right)
        if two_sum > target:
            right -= 1
        elif two_sum == target:
            return (left, right)
        else:  # two_sum < target:
            left += 1
    return pair


if __name__ == "__main__":
    assert two_sum_closest([1, 2, 3], 10) == (1, 2)
    assert two_sum_closest([1, 2, 3], -10) == (0, 1)
    assert two_sum_closest([1, 2, 3], 4) == (0, 2)
    assert two_sum_closest([1, 2, 3], 3) == (0, 1)
    assert two_sum_closest([1, 5, 6, 8, 14], 12) == (1, 3)
