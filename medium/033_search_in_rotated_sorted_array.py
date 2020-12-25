"""
You are given an integer array nums sorted in ascending order, and an integer target.

Suppose that nums is rotated at some pivot unknown to you beforehand (
i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

If target is found in the array return its index, otherwise, return -1.

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
"""
from typing import List


class Solution:
    """
    Bruteforce solution.

    Runtime: 36 ms, faster than 88.86% of Python3
    Memory Usage: 14.6 MB, less than 50.70% of Python3

    Time complexity: O(n)
    """

    def search(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except ValueError:
            return -1


class Solution2:
    """
    Bruteforce solution. The same idea as in first solution - scan all items and compare with target.

    Runtime: 40 ms, faster than 68.40% of Python3
    Memory Usage: 14.7 MB, less than 13.30% of Python3

    Time complexity: O(n)
    """

    def search(self, nums: List[int], target: int) -> int:
        for i, n in enumerate(nums):
            if n == target:
                return i
        return -1


class Solution3:
    """
    Algorithm idea: Define if there rotate in the list, if it's - remember rotate pivot (shift size). Normalize the list
     then apply Binary search. If target found, return its index taking into the account the shift size.

     Runtime: 36 ms, faster than 88.86% of Python3
     Memory Usage: 14.5 MB, less than 50.70% of Python3

     Time complexity: binary search takes O(log n) and O(k+n) takes slicing.
     Space complexity: We shadow original nums slice (if there rotation) with a normalized copy, it takes O(n)
    """

    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        rotate_pivot = 0

        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                rotate_pivot = i
        if rotate_pivot:
            nums = nums[rotate_pivot:] + nums[:rotate_pivot]

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return (mid + rotate_pivot) % len(nums)
            elif nums[mid] < target:
                left = mid + 1
            else:  # nums[mid] > target
                right = mid - 1
        return -1


class Solution4:
    """
    One-pass Binary Search (with defining subarrays):
        say if some pivot point (mid) has lowest value, on the left side from it toward begin will be
        one sorted subarray, and starting from that pivot point toward end will be another sorted subarray.

    Runtime: 40 ms, faster than 68.40% of Python3
    Memory Usage: 14.6 MB, less than 50.70% of Python3

    Time complexity: O(log n)
    Space complexity: O(1)
    """

    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > nums[right]:  # Left side of mid is sorted
                if nums[left] <= target < nums[mid]:  # Target in the left side
                    right = mid - 1
                else:  # target in the right side
                    left = mid + 1
            else:  # Right side is sorted
                if nums[mid] < target <= nums[right]:  # Target in the right side
                    left = mid + 1
                else:  # target in the left side
                    right = mid - 1
        return -1


if __name__ == '__main__':
    solutions = [Solution(), Solution2(), Solution3(), Solution4()]
    tc = (
        ([4, 5, 6, 7, 0, 1, 2], 0, 4),
        ([4, 5, 6, 7, 0, 1, 2], 4, 0),
        ([4, 5, 6, 7, 0, 1, 2], 6, 2),
        ([4, 5, 6, 7, 0, 1, 2], 3, -1),
        ([1, 2, 3, 4, 5], 2, 1),
        ([1], 0, -1),
        ([], 0, -1),
    )
    for s in solutions:
        for inp, trg, exp in tc:
            res = s.search(inp, trg)
            assert res == exp, f'{s.__class__.__name__}: want {exp}, got {res}'
