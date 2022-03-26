"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
    Input: nums = [1,2,3,4]
    Output: [24,12,8,6]

Example 2:
    Input: nums = [-1,1,0,-3,3]
    Output: [0,0,9,0,0]

Constraints:
    2 <= nums.length <= 105
    -30 <= nums[i] <= 30
    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
"""

from typing import List


class Solution:
    """
    Time complexity: O(n)
    Space complexity: O(1) - output array does not count as extra space as per problem description.
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        for i in range(1, len(nums)):
            result[i] = nums[i-1] * result[i-1]  # left prod
        # e.g., for 'nums' [1, 2, 3, 4] we get 'result' [1, 1, 2, 6]
        # here last 3 items calculated as 1*1=1, 2*1=2, 3*2=6

        right_prod = 1
        for i in range(len(nums)-1, -1, -1):
            # while calc product from right side, we define product without current
            result[i] *= right_prod
            right_prod *= nums[i]
        # 'result' [24,12,8,6]

        return result


if __name__ == '__main__':
    solutions = [
        Solution(),
    ]
    tc = (
        ([1,2,3,4], [24,12,8,6]),
        ([-1,1,0,-3,3], [0,0,9,0,0]),
    )
    for solution in solutions:
        for inp_nums, exp_output in tc:
            assert solution.productExceptSelf(inp_nums) == exp_output
