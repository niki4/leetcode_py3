"""
Given an array nums and a target value k, find the maximum length of a subarray that sums to k.
If there isn't one, return 0 instead.

Note:
The sum of the entire nums array is guaranteed to fit within the 32-bit signed integer range.

Example 1:

Input: nums = [1, -1, 5, -2, 3], k = 3
Output: 4
Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.
Example 2:

Input: nums = [-2, -1, 2, 1], k = 1
Output: 2
Explanation: The subarray [-1, 2] sums to 1 and is the longest.

Follow Up:
Can you do it in O(n) time?
"""
from typing import List


class Solution:
    """
    TLE

    Time complexity: O(n**3) because of two nested loops and sum calculation for slice
    """

    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        max_len_k = 0
        i = 0
        while i < len(nums):
            j = len(nums)
            if max_len_k >= j - i:
                return max_len_k

            while i < j:
                if sum(nums[i:j]) == k:
                    max_len_k = max(max_len_k, j - i)
                    break
                j -= 1
            i += 1
        return max_len_k


class Solution2:
    """
    Also TLE

    Time complexity: O(n**2 + n)
    """

    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0

        nums_sum = sum(nums)
        if nums_sum == k:
            return len(nums)

        max_len = 0
        for i in range(len(nums)):
            tmp = nums_sum
            for j in range(len(nums) - 1, i - 1, -1):
                if tmp == k:
                    max_len = max(max_len, j + 1 - i)
                tmp -= nums[j]
            nums_sum -= nums[i]
        return max_len


if __name__ == '__main__':
    solutions = [Solution(), Solution2()]
    tc = (
        ([1, -1, 5, -2, 3], 3, 4),
        ([-2, -1, 2, 1], 1, 2),
        ([1], 0, 0),
        ([1, 1, 0], 1, 2)
    )
    for s in solutions:
        for inp_nums, inp_k, exp in tc:
            res = s.maxSubArrayLen(inp_nums, inp_k)
            assert res == exp, f"{s.__class__.__name__}: expected {exp}, got {res}"
