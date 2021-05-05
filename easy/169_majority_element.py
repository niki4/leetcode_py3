"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element
always exists in the array.

Constraints:
    n == nums.length
    1 <= n <= 5 * 104
    -231 <= nums[i] <= 231 - 1

Follow-up: Could you solve the problem in linear time and in O(1) space?
"""

import collections
from typing import List


class Solution:
    """
    Runtime: 164 ms, faster than 69.01% of Python3
    Memory Usage: 15.4 MB, less than 95.44% of Python

    Time complexity: O(n)
    Space complexity: O(n) for counter
    """

    def majorityElement(self, nums: List[int]) -> int:
        ctr = collections.Counter(nums)
        return sorted(ctr, key=ctr.get, reverse=True)[0]


if __name__ == '__main__':
    solutions = [Solution()]
    tc = (
        ([3, 2, 3], 3),
        ([2, 2, 1, 1, 1, 2, 2], 2),
    )
    for sol in solutions:
        for inp_nums, exp_majority in tc:
            assert sol.majorityElement(inp_nums) == exp_majority
