"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""
import itertools
from typing import List


class Solution:
    """
    Runtime: 32 ms, faster than 97.49% of Python3
    Memory Usage: 14.3 MB, less than 73.39% of Python3
    """

    def permute(self, nums: List[int]) -> List[List[int]]:
        # LC also accept "list(itertools.permutations(nums))", but it returns list of tuples rather than list of lists
        return [list(perm) for perm in itertools.permutations(nums)]


if __name__ == '__main__':
    solutions = [Solution()]
    tc = (
        ([1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
        ([0, 1], [[0, 1], [1, 0]]),
        ([1], [[1]]),
    )
    for s in solutions:
        for inp_nums, exp_perm in tc:
            res = s.permute(inp_nums)
            assert res == exp_perm
