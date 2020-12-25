"""
Given a sorted (in ascending order) integer array nums of n elements and a target value,
write a function to search target in nums. If target exists, then return its index, otherwise return -1.

Note:
You may assume that all elements in nums are unique.
n will be in the range [1, 10000].
The value of each element in nums will be in the range [-9999, 9999].
"""
from typing import List
from bisect import bisect_left


class Solution:
    """
    Not a binary search, but good to know alternative approaches to solve the task.

    Runtime: 228 ms, faster than 90.09% of Python3
    Memory Usage: 15.6 MB, less than 20.05% of Python3
    Time complexity: O(n)
    Space complexity: O(1)
    """

    def search(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except ValueError:
            return -1


class Solution2:
    """
    Binary search using standard library module 'bisect'

    Runtime: 240 ms, faster than 39.88% of Python3
    Memory Usage: 15.6 MB, less than 20.05% of Python3
    Time complexity: O(log n)

    """

    def search(self, nums: List[int], target: int) -> int:
        idx = bisect_left(nums, target)
        return idx if (idx < len(nums) and nums[idx] == target) else -1


class Solution3:
    """
    Runtime: 240 ms, faster than 39.88% of Python3
    Memory Usage: 15.6 MB, less than 43.37% of Python3
    Time complexity: O(log n), we split and discard one half at each iteration.
    Space complexity: O(1)
    """

    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2  # or (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1


if __name__ == '__main__':
    solutions = [Solution(), Solution2(), Solution3()]
    tc = (
        ([-1, 0, 3, 5, 9, 12], 9, 4),
        ([-1, 0, 3, 5, 9, 12], 2, -1),
    )
    for s in solutions:
        for inp, trg, exp in tc:
            assert s.search(inp, trg) == exp
