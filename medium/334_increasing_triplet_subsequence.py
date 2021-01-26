"""
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that
i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

Example 1:
Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.

Example 2:
Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.
"""
from typing import List


class Solution:
    """
    Bruteforce solution. TLE

    Time complexity: O(n**3)
    Space complexity: O(1)
    """

    def increasingTriplet(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] < nums[j] < nums[k]:
                        return True
        return False


class Solution2:
    """
    Linear scan. Keep track of prev nums (min) while you go.

    Runtime: 56 ms, faster than 59.12% of Python3
    Memory Usage: 14.9 MB, less than 51.64% of Python3

    Time complexity: O(n)
    Space complexity: O(1)
    """

    def increasingTriplet(self, nums: List[int]) -> bool:
        first_num, second_num = float('inf'), float('inf')
        for n in nums:
            if n <= first_num:
                first_num = n
            elif n <= second_num:
                second_num = n
            else:
                return True
        return False


if __name__ == '__main__':
    solutions = [Solution(), Solution2()]
    tc = (
        ([1, 2, 3, 4, 5], True),
        ([5, 4, 3, 2, 1], False),
        ([2, 1, 5, 0, 4, 6], True),  # 0, 4, 6
        ([20, 100, 10, 12, 5, 13], True),  # 10, 12, 13
        ([2, 1, 5, 0, 3], False),
    )
    for s in solutions:
        for inp, exp in tc:
            res = s.increasingTriplet(inp)
            assert res == exp, f'{s.__class__.__name__}: for input {inp} expected {exp}, got {res}'
