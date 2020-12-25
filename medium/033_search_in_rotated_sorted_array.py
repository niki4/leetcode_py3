"""
You are given an integer array nums sorted in ascending order, and an integer target.

Suppose that nums is rotated at some pivot unknown to you beforehand (
i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

If target is found in the array return its index, otherwise, return -1.

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
"""
from typing import List


class Solution:
    """
    Bruteforce solution.

    Runtime: 36 ms, faster than 88.86% of Python3
    Memory Usage: 14.6 MB, less than 50.70% of Python3

    Time complexity: O(n)
    """

    def search(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except ValueError:
            return -1


class Solution2:
    """
    Bruteforce solution. The same idea as in first solution - scan all items and compare with target.

    Runtime: 40 ms, faster than 68.40% of Python3
    Memory Usage: 14.7 MB, less than 13.30% of Python3

    Time complexity: O(n)
    """

    def search(self, nums: List[int], target: int) -> int:
        for i, n in enumerate(nums):
            if n == target:
                return i
        return -1


if __name__ == '__main__':
    solutions = [Solution(), Solution2()]
    tc = (
        ([4, 5, 6, 7, 0, 1, 2], 0, 4),
        ([4, 5, 6, 7, 0, 1, 2], 3, -1),
        ([1], 0, -1),
    )
    for s in solutions:
        for inp, trg, exp in tc:
            assert s.search(inp, trg) == exp
