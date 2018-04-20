"""
Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Follow up:

If you have figured out the O(n) solution, try coding another solution using
the divide and conquer approach, which is more subtle.
"""
from math import floor

# TODO: Complete the solution
class Solution:
    def maxSubArray(self, nums):
        """
        :param nums: List[int]
        :return: int
        """
        # max_subarray = []

        half_part = floor(len(nums) / 2)

        while half_part > 1:

            if sum(nums[:half_part]) < sum(nums[half_part:]):
                max_subarray = nums[half_part:]
            else:
                max_subarray = nums[:half_part]

            self.maxSubArray(max_subarray)

        # return max_subarray


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # expected: 6  ([4,-1,2,1] has the largest sum = 6)
