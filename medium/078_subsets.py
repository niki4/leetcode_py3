"""
Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Constraints:
    1 <= nums.length <= 10
    -10 <= nums[i] <= 10
    All the numbers of nums are unique.
"""
import itertools
from typing import List


class Solution:
    """
    Itertools provides a convenient method to get combination of elements with given size.

    Runtime: 36 ms, faster than 58.03% of Python3
    Memory Usage: 14.5 MB, less than 54.22% of Python3
    """

    def subsets(self, nums: List[int]) -> List[List[int]]:
        return [
            list(comb)
            for size in range(len(nums) + 1)
            for comb in itertools.combinations(nums, size)
        ]


if __name__ == '__main__':
    tc = (
        ([1, 2, 3], [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]),
        ([0], [[], [0]]),
    )
    solutions = [Solution()]
    for s in solutions:
        for inp_nums, exp_comb in tc:
            res = sorted(s.subsets(inp_nums))
            assert res == sorted(exp_comb)
