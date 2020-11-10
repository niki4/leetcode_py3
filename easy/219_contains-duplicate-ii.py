"""
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array
such that nums[i] = nums[j] and the absolute difference between i and j is at most k.
https://en.wikipedia.org/wiki/Absolute_difference

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
"""

from typing import List


class Solution:
    """
    Runtime: 80 ms, faster than 95.46% of Python3
    Memory Usage: 21.6 MB, less than 8.61% of Python3
    """

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = dict()
        for i, v in enumerate(nums):
            if v in seen and i - seen[v] <= k:
                return True
            seen[v] = i  # track index of value
        return False
