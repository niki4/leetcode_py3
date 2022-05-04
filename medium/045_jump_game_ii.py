"""
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Your goal is to reach the last index in the minimum number of jumps.
You can assume that you can always reach the last index.

Example 1:
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [2,3,0,1,4]
Output: 2

Constraints:
    1 <= nums.length <= 104
    0 <= nums[i] <= 1000
"""

from typing import List


class Solution:
    """
    Algorithm idea: moving pointer from end toward begin, at each step find the
    longest possible jump that allows us reach our pointer.
    """
    def jump(self, nums: List[int]) -> int:
        last_pos = len(nums)-1
        jumps = 0

        while last_pos > 0:
            tmp = last_pos
            for i in range(last_pos, -1, -1):
                if i + nums[i] >= last_pos:  # can reach last_pos from curr_pos
                    tmp = i
            last_pos = tmp  # move ptr to source of longest possible jump
            jumps += 1

        return jumps


if __name__ == '__main__':
    solutions = [
        Solution(),
    ]
    tc = (
        ([2,3,1,1,4], 2),
        ([2,3,0,1,4], 2),
    )
    for sol in solutions:
        for inp_nums, res_jumps in tc:
            assert sol.jump(inp_nums) == res_jumps
