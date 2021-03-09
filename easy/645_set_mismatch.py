"""
You have a set of integers s, which originally contains all the numbers from 1 to n.
Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set,
which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.

Example 1:
Input: nums = [1,2,2,4]
Output: [2,3]

Example 2:
Input: nums = [1,1]
Output: [1,2]

Constraints:
    2 <= nums.length <= 104
    1 <= nums[i] <= 104
"""

import collections
from typing import List


class Solution:
    """
    Runtime: 196 ms, faster than 68.21% of Python3
    Memory Usage: 15.9 MB, less than 42.22% of Python3
    """

    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums_ctr = dict()
        for n in nums:
            if n in nums_ctr:
                nums_ctr[n] += 1
            else:
                nums_ctr[n] = 1
        missed, duplicated = 0, 0

        for n in range(1, len(nums) + 1):
            if n not in nums_ctr:
                missed = n
            elif nums_ctr[n] >= 2:
                duplicated = n

        return [duplicated, missed]


class Solution2:
    """
    The idea is to combine both the source and expected lists of nums then find the min (missed) and max (duplicated)
     count number.

    Runtime: 200 ms, faster than 62.09% of Python3
    Memory Usage: 15.9 MB, less than 42.22% of Python3
    """

    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums_ctr = collections.Counter(nums)
        nums_ctr.update(range(1, len(nums) + 1))
        ns = sorted(nums_ctr, key=nums_ctr.get)
        return [ns[-1], ns[0]] if ns else []


if __name__ == '__main__':
    solutions = [Solution(), Solution2()]
    tc = (
        ([1, 2, 2, 4], [2, 3]),
        ([1, 1], [1, 2]),
        ([2, 2], [2, 1]),
        ([3, 2, 2], [2, 1]),
        ([3, 2, 3, 4, 6, 5], [3, 1]),
    )
    for sol in solutions:
        for inp, exp in tc:
            assert sol.findErrorNums(inp) == exp
