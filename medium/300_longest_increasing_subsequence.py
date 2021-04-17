"""
Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order
 of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:
Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:
Input: nums = [7,7,7,7,7,7,7]
Output: 1

Constraints:
    1 <= nums.length <= 2500
    -104 <= nums[i] <= 104

Follow up:
    Could you come up with the O(n2) solution?
    Could you improve it to O(n log(n)) time complexity?
"""
from typing import List


class Solution:
    """
    Bottom-Up DP

    Runtime: 4092 ms, faster than 15.07% of Python3
    Memory Usage: 14.7 MB, less than 17.73% of Python3

    Time complexity: O(n^2)
    Space complexity: O(n)

    Change dp over time for test sample:
    In [120]: sol.lengthOfLIS( [0,1,0,3,2,3])
        max(dp[1] = 1, dp[0] + 1 = 2)	dp[1] = 2
        max(dp[3] = 1, dp[0] + 1 = 2)	dp[3] = 2
        max(dp[3] = 2, dp[1] + 1 = 3)	dp[3] = 3
        max(dp[3] = 3, dp[2] + 1 = 2)	dp[3] = 3
        max(dp[4] = 1, dp[0] + 1 = 2)	dp[4] = 2
        max(dp[4] = 2, dp[1] + 1 = 3)	dp[4] = 3
        max(dp[4] = 3, dp[2] + 1 = 2)	dp[4] = 3
        max(dp[5] = 1, dp[0] + 1 = 2)	dp[5] = 2
        max(dp[5] = 2, dp[1] + 1 = 3)	dp[5] = 3
        max(dp[5] = 3, dp[2] + 1 = 2)	dp[5] = 3
        max(dp[5] = 3, dp[4] + 1 = 4)	dp[5] = 4
    Out[120]: 4

    """

    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    # print(f"max(dp[{i}] = {dp[i]}, dp[{j}] + 1 = {dp[j] + 1})", end="\t")
                    dp[i] = max(dp[i], dp[j] + 1)
                    # print(f"dp[{i}] = {dp[i]}")
        return max(dp)


if __name__ == '__main__':
    solutions = [Solution()]
    tc = (
        ([10, 9, 2, 5, 3, 7, 101, 18], 4),
        ([0, 1, 0, 3, 2, 3], 4),
        ([7, 7, 7, 7, 7, 7, 7], 1),
        ([1, 3, 6, 7, 9, 4, 10, 5, 6], 6)
    )
    for sol in solutions:
        for inp_nums, exp_lis_len in tc:
            res = sol.lengthOfLIS(inp_nums)
            assert res == exp_lis_len, f"for input {inp_nums} expected result {exp_lis_len}, got {res}"
