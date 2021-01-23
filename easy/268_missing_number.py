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


class Solution4:
    """
    Algorithm: XOR (Exclusive OR) all values in etalon range first, then repeat for given array.
    In XOR, which works with bits of num, if two bits equal it produces 0, and if not eq produces 1:
    x	y	x ^ y
    0	0	0
    0	1	1
    1	0	1
    1	1	0
    So that, e.g. 0011 ^ 0101 = 0110 if two nums are differ, and if two nums are equal x ^ x = 0.
    Iterating through ethalon range, then through array with missed nums, with XOR, will remove all the dup values
    leaving us missed num as the result.

    Runtime: 140 ms, faster than 40.63% of Python3
    Memory Usage: 15.5 MB, less than 53.58% of Python3
    """

    def missingNumber(self, nums: List[int]) -> int:
        result = 0
        for val in range(len(nums) + 1):
            result ^= val
        for val in nums:
            result ^= val
        return result


if __name__ == "__main__":
    solutions = [Solution(), Solution2(), Solution3(), Solution4()]
    tc = (
        ([3, 0, 1], 2),
        ([0, 1], 2),
        ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8),
        ([0], 1),
    )
    for s in solutions:
        for inp, exp in tc:
            assert s.missingNumber(inp) == exp
