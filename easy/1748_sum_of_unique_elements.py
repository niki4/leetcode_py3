"""
You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.

Return the sum of all the unique elements of nums.



Example 1:

Input: nums = [1,2,3,2]
Output: 4
Explanation: The unique elements are [1,3], and the sum is 4.
"""

import collections
from typing import List


class Solution:
    """
    Runtime: 44 ms, faster than 6.40% of Python3
    Memory Usage: 14.3 MB, less than 42.72% of Python3
    """

    def sumOfUnique(self, nums: List[int]) -> int:
        ctr = collections.Counter(nums)
        return sum(k for k in ctr if ctr[k] == 1)


class Solution2:
    """
    Num range is constant as it was set in Constraints, so we can pre-allocate array where
    index represent the num (1-100) and value is the count of the num from source array.

    Runtime: 44 ms, faster than 6.44% of Python3
    Memory Usage: 14.1 MB, less than 90.38% of Python3
    """

    def sumOfUnique(self, nums: List[int]) -> int:
        num_ctr = [0] * (100 + 1)
        for n in nums:
            num_ctr[n] += 1
        return sum(i for (i, n) in enumerate(num_ctr) if n == 1)


if __name__ == '__main__':
    solutions = [Solution()]
    tc = (
        ([1, 2, 3, 2], 4),
        ([1, 1, 1, 1, 1], 0),
        ([1, 2, 3, 4, 5], 15),
    )
    for sol in solutions:
        for inp_nums, exp_sum in tc:
            assert sol.sumOfUnique(inp_nums) == exp_sum
