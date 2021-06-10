"""
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.

Example 1:
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

Example 2:
Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

Constraints:
    1 <= nums.length <= 1000
    -10^6 <= nums[i] <= 10^6
"""
from itertools import accumulate
from typing import List


class Solution:
    """
    Runtime: 36 ms, faster than 85.31% of Python3
    Memory Usage: 14.1 MB, less than 96.97% of Python3

    Time complexity: O(n)
    Space complexity: O(n)
    """

    def runningSum(self, nums: List[int]) -> List[int]:
        prev_sum = 0
        result = []
        for n in nums:
            prev_sum += n
            result.append(prev_sum)
        return result


class Solution2:
    """
    Runtime: 40 ms, faster than 63.50% of Python3
    Memory Usage: 14.5 MB, less than 10.28% of Python3

    Time complexity: O(n)
    Space complexity: O(n)
    """

    def runningSum(self, nums: List[int]) -> List[int]:
        return list(accumulate(nums))


class Solution3:
    """
    Runtime: 88 ms, faster than 5.32% of Python3
    Memory Usage: 14.5 MB, less than 10.28% of Python3

    Time complexity: O(n)
    Space complexity: O(1). Note we update nums list in place (so changes are seen outside of the function).
    """

    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] = sum(nums[i - 1:i + 1])
        return nums


if __name__ == '__main__':
    solutions = [Solution(), Solution2(), Solution3()]
    tc = (
        ([1, 2, 3, 4], [1, 3, 6, 10]),
        ([1, 1, 1, 1, 1], [1, 2, 3, 4, 5]),
        ([3, 1, 2, 10, 1], [3, 4, 6, 16, 17]),
    )
    for sol in solutions:
        for inp_nums, exp_nums in tc:
            assert sol.runningSum(inp_nums) == exp_nums
