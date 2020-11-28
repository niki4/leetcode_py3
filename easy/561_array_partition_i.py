"""
Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn)
such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.

Example 1:
Input: nums = [1,4,3,2]
Output: 4
Explanation: All possible pairings (ignoring the ordering of elements) are:
1. (1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3
2. (1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3
3. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4
So the maximum possible sum is 4.


Constraints:
1 <= n <= 104
nums.length == 2 * n
-104 <= nums[i] <= 104
"""
from typing import List


class Solution:
    """
    Runtime: 292 ms, faster than 8.11% of Python3
    Memory Usage: 16.8 MB, less than 75.29% of Python3

    Presorted array guarantees we deal with closest values pairs.
    Time complexity: O(NlogN) for sorting and O(N) to iterate array.
    Space complexity: O(N) because of builtin sorting algo, which is Timsort in Python.
    """

    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        max_sum = 0
        for i in range(1, len(nums), 2):
            pair = (nums[i - 1], nums[i])
            max_sum += min(pair)
        return max_sum


class Solution2:
    """
    Runtime: 260 ms, faster than 60.12% of Python3
    Memory Usage: 16.9 MB, less than 37.74% of Python3

    Shorter version of the first solution.
    Since the array is sorted we can be sure the lowest element is first in pair,
    so just take and sum each even element (0th, 2nd, 4th, etc).
    """

    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])


if __name__ == '__main__':
    solutions = [Solution(), Solution2()]
    tc = [
        ([1, 4, 3, 2], 4),
        ([6, 2, 6, 5, 1, 2], 9)
    ]
    for s in solutions:
        for inp_nums, expected in tc:
            assert s.arrayPairSum(inp_nums) == expected
