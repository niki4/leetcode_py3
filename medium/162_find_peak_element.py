"""
A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its index.
If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Example 2:
Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2,
or index number 5 where the peak element is 6.

Constraints:
1 <= nums.length <= 1000
-231 <= nums[i] <= 231 - 1
nums[i] != nums[i + 1] for all valid i.

Follow up: Could you implement a solution with logarithmic complexity?
"""
from typing import List


class Solution:
    """
    Bruteforce solution.
    Algorithm idea: Peak's next element is lower (descent). Also there's special case when there only ascent, so the
    peak will be the last element in this case.

    Time complexity: O(n)
    """

    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                return i - 1
            elif nums[i] > nums[i - 1] and i == len(nums) - 1:
                return i


if __name__ == '__main__':
    solutions = [Solution()]
    tc = (
        ([1, 2, 3, 1], [2]),
        ([1, 2, 1, 3, 5, 6, 4], [1, 5])
    )
    for s in solutions:
        for inp, exp in tc:
            assert s.findPeakElement(inp) in exp
