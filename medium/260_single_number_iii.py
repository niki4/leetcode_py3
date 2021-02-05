"""
Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly
twice. Find the two elements that appear only once. You can return the answer in any order.

Follow up:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?

Constraints:

2 <= nums.length <= 3 * 104
-231 <= nums[i] <= 231 - 1
Each integer in nums will appear twice, only two integers will appear once.
"""

from collections import Counter
from typing import List


class Solution:
    """
    Using counter to calculate amount of each element, then filter for those that appears only once.

    Runtime: 60 ms, faster than 67.65% of Python3
    Memory Usage: 16.1 MB, less than 32.17% of Python3

    Time complexity: (2*n) which turns to O(n) because 2 is constant
    Space complexity: O(n) for storing element in Counter
    """

    def singleNumber(self, nums: List[int]) -> List[int]:
        ctr = Counter(nums)
        res = list()
        for k in ctr:
            if ctr[k] == 1:
                res.append(k)
                if len(res) == 2:
                    return res


if __name__ == '__main__':
    solutions = [Solution()]
    tc = (
        ([1, 2, 1, 3, 2, 5], [3, 5]),
        ([-1, 0], [-1, 0]),
        ([0, 1], [0, 1]),
    )
    for s in solutions:
        for inp, exp in tc:
            assert s.singleNumber(inp) == exp
