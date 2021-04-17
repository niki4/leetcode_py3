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
import bisect
from typing import List


class Solution:
    """
    Bottom-Up DP

    Runtime: 4092 ms, faster than 15.07% of Python3
    Memory Usage: 14.7 MB, less than 17.73% of Python3

    Time complexity: O(n^2)
    Space complexity: O(n)

    Change dp over time for test sample:
    In: sol.lengthOfLIS( [0,1,0,3,2,3])
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
    Out: 4

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


class Solution2:
    """
    Bottom-Up DP + Binary Search

    Runtime: 84 ms, faster than 82.25% of Python3
    Memory Usage: 14.5 MB, less than 91.77% of Python3

    Time complexity: O(n logN)
    Space complexity: O(n)

    The idea is to replace element in dp list each time we found a better one (lower than last one in dp list).
        Say, we have subarr [2, 5], next element from nums 3 would be placed between 2 and 5 to keep the list sorted.
        Its index 1, so we just put 3 at index 1 replacing 5 and new subarr [2, 3].
        Next element from nums would be 7 which is greater than last one in dp list, so we just push it to the dp list
        and new subarr [2, 3, 7]. And so on.
    """

    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        dp = [nums[0]]
        for i in range(1, len(nums)):
            left, right = 0, len(dp) - 1
            while left < right:
                mid = (left + right) // 2
                if dp[mid] < nums[i]:
                    left = mid + 1
                else:
                    right = mid

            if dp[left] < nums[i]:
                dp.append(nums[i])
            else:
                dp[left] = nums[i]
        return len(dp)


class Solution3:
    """
    Bottom-Up DP + Binary Search

    The same idea as in Solution2, but using Python's bisect library

    Runtime: 68 ms, faster than 93.71% of Python3
    Memory Usage: 14.5 MB, less than 74.90% of Python3

    Time complexity: O(n logN)
    Space complexity: O(n)
    """

    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        for i in range(len(nums)):
            if not dp or nums[i] > dp[-1]:
                dp.append(nums[i])
            else:
                # bisect_left - Returns the index where to insert nums[i] in list dp, assuming dp is sorted.
                pos = bisect.bisect_left(dp, nums[i])
                dp[pos] = nums[i]
        return len(dp)


if __name__ == '__main__':
    solutions = [Solution(), Solution2(), Solution3()]
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
