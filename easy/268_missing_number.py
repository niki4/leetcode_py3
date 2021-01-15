"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n,
find the one that is missing from the array.

Example 1:
Input: [3,0,1]
Output: 2

Example 2:
Input: [9,6,4,2,3,5,7,0,1]
Output: 8

Note:
Your algorithm should run in linear runtime complexity.
Could you implement it using only constant extra space complexity?
"""
from typing import List


class Solution:
    """
    Runtime: 36 ms, faster than 99.10% of Python3.
    Memory Usage: 15.4 MB, less than 5.15% of Python3.
    """

    def missingNumber(self, nums: list) -> int:
        return set(range(len(nums) + 1)).difference(nums).pop()


class Solution2:
    """
    Runtime: 40 ms, faster than 97.18%.
    Memory Usage: 14.2 MB, less than 41.46%.

    Variation on Gauss formula (closed-form expression for the sum).
    This approach expects monotonic range of nums started from 0 with single missed num.
    """

    def missingNumber(self, nums: list) -> int:
        difference = 0
        for idx, val in enumerate(nums):
            difference += (val - idx)
        return len(nums) - difference


class Solution3:
    """
    Runtime: 124 ms, faster than 89.68% of Python3
    Memory Usage: 15.5 MB, less than 17.58% of Python3
    """

    def missingNumber(self, nums: List[int]) -> int:
        return sum(range(len(nums) + 1)) - sum(nums)


if __name__ == "__main__":
    solutions = [Solution(), Solution2(), Solution3()]
    tc = (
        ([3, 0, 1], 2),
        ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8),
        ([0], 1),
    )
    for s in solutions:
        for inp, exp in tc:
            assert s.missingNumber(inp) == exp
