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


class Solution2:
    """
    Shorter version of first solution

    Runtime: 56 ms, faster than 86.65% of Python3
    Memory Usage: 16.4 MB, less than 7.62% of Python3
    """

    def singleNumber(self, nums: List[int]) -> List[int]:
        ctr = Counter(nums)
        return [n for n in ctr if ctr[n] == 1]


class Solution3:
    """
    Algorithm idea:
    1. Using XOR discard all duplicates from nums list so we get bitmask (diff) of two unique elements
    2. Using that bitmask we can use "x & (-x)" binary operation to isolate the rightmost 1-bit (and set all the others
    bits to zero), which is different between x and y. Let's say this is 1-bit for x, and 0-bit for y.
    3. Now let's use XOR as before, but for the new bitmask x_bitmask, which will contain only the numbers which have
    1-bit in the position of bitmask & (-bitmask). This way, this new bitmask will contain only number x x_bitmask = x,
    because of two reasons:
        1) y has 0-bit in the position bitmask & (-bitmask) and hence will not enter this new bitmask.
        2) All numbers but x will not be visible in this new bitmask because they appear two times.
    4. Once we identified X, we can identify Y by applying XOR to the bitmask (y = bitmask^x)

    Runtime: 48 ms, faster than 98.84% of Python3
    Memory Usage: 15.8 MB, less than 58.60% of Python3

    Time complexity: O(N) to iterate over the input array.
    Space complexity: O(1), it's a constant space solution.
    """

    def singleNumber(self, nums: List[int]) -> List[int]:
        # difference between two numbers (x and y) which were seen only once
        bitmask = 0
        for num in nums:
            bitmask ^= num

        # rightmost 1-bit diff between x and y
        diff = bitmask & (-bitmask)

        x = 0
        for num in nums:
            # bitmask which will contain only x
            if num & diff:
                x ^= num

        return [x, bitmask ^ x]


if __name__ == '__main__':
    solutions = [Solution(), Solution2(), Solution3()]
    tc = (
        ([1, 2, 1, 3, 2, 5], [3, 5]),
        ([-1, 0], [-1, 0]),
        ([0, 1], [0, 1]),
    )
    for s in solutions:
        for inp, exp in tc:
            res = s.singleNumber(inp)
            assert sorted(res) == sorted(exp), f"{s.__class__.__name__}: for input {inp} expected {exp}, got {res}"
