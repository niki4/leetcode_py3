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

    def singleNumber(self, nums: List[int]) -> int:
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


class Solution3:
    """
    XOR (exclusive OR) approach

    Runtime: 148 ms, faster than 32.59% of Python3
    Memory Usage: 16.6 MB, less than 86.53% of Python3

    This works on binary level so this pattern could also be applied to non-num characters.
    Applying XOR all duplicated values (which has the same binary representation) will turn to 0 leaving us unique val.

    XOR table:
    x   y       res
    0   0   =   0
    0   1   =   1
    1   0   =   1
    1   1   =   0

    Time complexity: O(n)
    Space complexity: O(1)
    """

    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res ^= n
        return res


if __name__ == '__main__':
    solutions = [Solution(), Solution2(), Solution3()]
    tc = (
        ([1, 1, 2], 2),
        ([2, 2, 1], 1),
        ([4, 1, 2, 1, 2], 4),
        ([1], 1),
    )
    for s in solutions:
        for inp, exp in tc:
            assert s.singleNumber(inp) == exp
