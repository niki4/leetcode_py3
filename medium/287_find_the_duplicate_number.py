"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.
"""
from typing import List


class Solution:
    """
    Using hash to track elements

    Runtime: 60 ms, faster than 91.09% of Python3
    Memory Usage: 18.3 MB, less than 16.38% of Python3

    Time and Space complexity: O(n)
    """

    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        for n in nums:
            if n in seen:
                return n
            seen.add(n)


class Solution2:
    """
    Some sort of bitwise magic

    Runtime: 80 ms, faster than 27.16% of Python3
    Memory Usage: 16.6 MB, less than 78.03% of Python3

     O(n) time and O(1) space
    """

    def findDuplicate(self, nums: List[int]) -> int:
        bit_mask = 1
        for n in nums:
            if bit_mask >> n & 1:
                return n
            bit_mask |= 1 << n


if __name__ == '__main__':
    solutions = [Solution(), Solution2()]
    tc = (
        ([1, 3, 4, 2, 2], 2),
        ([3, 1, 3, 4, 2], 3),
        ([1, 1], 1),
        ([1, 1, 2], 1),
        ([2, 2, 2, 2, 2], 2),
    )
    for s in solutions:
        for inp, exp in tc:
            res = s.findDuplicate(inp)
            assert res == exp, f"{s.__class__.__name__}: for input {inp} expected {exp}, got {res}"
