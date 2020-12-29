"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

The array may contain duplicates.

Example 1:
Input: [1,3,5]
Output: 1

Example 2:
Input: [2,2,2,0,1]
Output: 0

Note:
This is a follow up problem to Find Minimum in Rotated Sorted Array.
Would allow duplicates affect the run-time complexity? How and why?
"""
from typing import List


class Solution:
    """
    Runtime: 52 ms, faster than 62.23% of Python3
    Memory Usage: 14.8 MB, less than 50.05% of Python3

    Time complexity: O(n)
    Space complexity: O(1)
    """

    def findMin(self, nums: List[int]) -> int:
        return min(nums)


if __name__ == '__main__':
    solutions = [Solution()]
    tc = (
        ([1, 3, 5], 1),
        ([2, 2, 2, 0, 1], 0),
    )
    for s in solutions:
        for inp, exp in tc:
            res = s.findMin(inp)
            assert res == exp, f"{s.__class__.__name__}: for inp {inp} exp {exp}, got {res}"
