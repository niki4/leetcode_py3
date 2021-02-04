"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1

"""
from typing import List


class Solution:
    """
    Runtime: 3324 ms, faster than 5.00% of Python3.
    Memory Usage: 14.8 MB, less than 5.05% of Python3.
    """

    def singleNumber(self, nums: 'List[int]') -> int:
        for x in set(nums):
            if nums.count(x) == 1:
                return x


class Solution2:
    """
    Runtime: 52 ms, faster than 44.56% of Python3.
    Memory Usage: 15.1 MB, less than 5.05% of Python3.
    """

    def singleNumber(self, nums: List[int]) -> int:
        if not nums:
            return 0

        counter = dict()

        for i in nums:
            if i not in counter:
                counter[i] = 1
            else:
                counter[i] += 1

        return min(counter, key=counter.get)  # return key that holds min counter value


if __name__ == '__main__':
    solutions = [Solution(), Solution2()]
    tc = (
        ([1, 1, 2], 2),
        ([2, 2, 1], 1),
        ([4, 1, 2, 1, 2], 4),
        ([1], 1),
    )
    for s in solutions:
        for inp, exp in tc:
            assert s.singleNumber(inp) == exp
