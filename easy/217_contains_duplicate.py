"""
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array,
and it should return false if every element is distinct.
"""
from typing import List


class Solution:
    """
    Runtime: 104 ms, faster than 98.40% of Python3
    Memory Usage: 19.7 MB, less than 26.75% of Python3

    Time complexity: O(n) for scanning over nums during set creation, O(1) for comparison
    Space complexity: O(n) for storing set
    """

    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


class Solution2:
    """
    Runtime: 104 ms, faster than 98.40% of Python3
    Memory Usage: 21 MB, less than 26.75% of Python3

    Time complexity: O(n) for scanning over nums, O(1) for key lookup in dict
    Space complexity: O(n) for storing dict (basically, solution uses hash table just like solution with set above).
    """

    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = dict()
        for n in nums:
            if n in seen:
                return True
            seen[n] = True
        return False


if __name__ == '__main__':
    tc = [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
    ]
    solutions = [Solution(), Solution2()]
    for sol in solutions:
        for nums, expected in tc:
            assert sol.containsDuplicate(nums) == expected
