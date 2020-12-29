"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times.

For example, the array nums = [0,1,2,4,5,6,7] might become:
[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in
the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums, return the minimum element of this array.

Example 1:
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

Constraints:
n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
All the integers of nums are unique.
nums is sorted and rotated between 1 and n times.
"""
from typing import List


class Solution:
    """
    Bruteforce solution (we guaranteed in Constraints that there's at least one element, so no check for nums).

    Runtime: 40 ms, faster than 62.35% of Python3
    Memory Usage: 14.6 MB, less than 39.04% of Python3

    Time complexity: O(n)
    Space complexity: O(1)
    """

    def findMin(self, nums: List[int]) -> int:
        return min(nums)


if __name__ == '__main__':
    tc = (
        ([3, 4, 5, 1, 2], 1),
        ([4, 5, 6, 7, 0, 1, 2], 0),
        ([11, 13, 15, 17], 11),
    )
    solutions = [Solution()]
    for s in solutions:
        for inp, exp in tc:
            assert s.findMin(inp) == exp
