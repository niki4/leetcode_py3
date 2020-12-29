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


class Solution2:
    """
    Binary search.
    Here we converge left and right borders toward the lowest element.

    Runtime: 44 ms, faster than 96.51% of Python3
    Memory Usage: 15 MB, less than 30.85% of Python3

    Time complexity: O(log n)
    Space complexity: O(1)
    """

    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        if nums[left] < nums[right]:  # already sorted in asc order
            return nums[left]

        while left < right:
            mid = (left + right) // 2  # or "left + (right - left) // 2" to avoid potential overflow
            if nums[left] == nums[mid] == nums[right]:  # skip duplicates
                left += 1
                right -= 1
            elif nums[mid] <= nums[right]:  # regular binary search
                right = mid
            else:
                left = mid + 1
        return nums[left]


class Solution3:
    """
    Binary search.
    Right border is the local maximum for right border (mid to right asc subarr)
    and local minimum to left border (left to mid asc subarr). In case mid and right points has the same value, we
    just skip the duplicated item by moving right border by one (toward left). Once borders are converged, we found min.

    Runtime: 44 ms, faster than 96.51% of Python3
    Memory Usage: 14.9 MB, less than 50.05% of Python3

    Time complexity: O(log n)
    Space complexity: O(1)
    """

    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:  # nums[mid] == nums[right]
                right -= 1
        return nums[left]


if __name__ == '__main__':
    solutions = [Solution(), Solution2()]
    tc = (
        ([1, 3, 5], 1),
        ([3, 3, 1, 3], 1),
        ([2, 2, 2, 0, 1], 0),
        ([4, 5, 6, 7, 0, 1, 2], 0),
        ([10, 1, 10, 10, 10], 1),
    )
    for s in solutions:
        for inp, exp in tc:
            res = s.findMin(inp)
            assert res == exp, f"{s.__class__.__name__}: for inp {inp} exp {exp}, got {res}"
