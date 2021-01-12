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
    Kadane's algorithm / Dynamic Programming
    https://en.wikipedia.org/wiki/Maximum_subarray_problem#Kadane's_algorithm
    
    Runtime: 44 ms, faster than 93.79% of Python3.
    Memory Usage: 13.6 MB, less than 5.50% of Python3.
    Runtime complexity: O(n)
    """
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        curr_sum = max_sum = nums[0]
        for num in nums[1:]:
            curr_sum = max(num, curr_sum + num)
            max_sum = max(max_sum, curr_sum)
            
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
