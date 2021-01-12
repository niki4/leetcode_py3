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
from typing import List


class Solution:
    """
    Greedy approach.

    Runtime: 60 ms, faster than 91.14% of Python3
    Memory Usage: 14.9 MB, less than 56.56% of Python3
    Runtime complexity: O(n)
    Space complexity: O(1)

    Algorithm idea: we keep track on local max (curr_sum) if its growing sequence or reset it if current num is larger.
    Also on each iteration we compare global max with the local one and update it accordingly.
    """

    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        curr_sum = max_sum = nums[0]
        for num in nums[1:]:  # also can use iteration for range (by idx) instead slice (by num)
            curr_sum = max(num, curr_sum + num)
            max_sum = max(max_sum, curr_sum)

        return max_sum


class Solution2:
    """
    Kadane's algorithm / Dynamic Programming
    https://en.wikipedia.org/wiki/Maximum_subarray_problem#Kadane's_algorithm

    Algorithm idea: one could modify the array to track the current local maximum sum at this given point.
    Next step is to update the global maximum sum, knowing the local one.

    current element = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        restart if curr_sum < 0
    current max sum = [-2, 1(!), -2, 4(!), 3, 5, 6, 1, 5]
    max sum seen so far = [-2, 1, 1, 4, 4, 5, 6, 6, 6(the answer)]

    Runtime: 68 ms, faster than 50.22% of Python3
    Memory Usage: 15.2 MB, less than 13.75% of Python3
    Runtime complexity: O(n)
    Space complexity: O(1)
    """

    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0] if nums else 0
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
            max_sum = max(max_sum, nums[i])
        return max_sum


if __name__ == '__main__':
    solutions = [Solution()]
    tc = (
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
        ([1], 1),
        ([0], 0),
        ([-1], -1),
        ([-100000], -100000),
    )
    for sol in solutions:
        for inp, exp in tc:
            assert sol.maxSubArray(inp) == exp
