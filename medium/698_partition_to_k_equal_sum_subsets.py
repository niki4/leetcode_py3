"""
Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into
k non-empty subsets whose sums are all equal.

Example 1:
Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.

Note:
    1 <= k <= len(nums) <= 16.
    0 < nums[i] < 10000.
"""
from typing import List


class Solution:
    """
    Dynamic Programming / DFS with backtracking

    Runtime: 48 ms, faster than 77.03% of Python3
    Memory Usage: 14.1 MB, less than 98.53% of Python3

    Time complexity: O(k ^ n)
    Every element in the nums array must be placed in one destined bucket. And for each element in nums array, it has k
    choices, so we time k n times, i.e., k * k * k * ... * k. However, pruning unsolvable combination by checking an
    empty subset (avoid putting the same useless content into next k - 1 buckets) will improve the performance.
    """

    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        bucket, k_sum = [0] * k, sum(nums) // k
        nums.sort(reverse=True)  # starting from larger nums first speed up algorithm

        def dfs(idx):
            if idx == len(nums):
                return len(set(bucket)) == 1
            for i in range(k):
                bucket[i] += nums[idx]
                if bucket[i] <= k_sum and dfs(idx + 1):
                    return True
                bucket[i] -= nums[idx]
                """
                The key is, bucket[i] == 0 means for all k > i, sum[k] == 0; because this algorithm always fill the 
                previous buckets before trying the next.
                So if putting nums[i] in this empty bucket can't solve the game, putting nums[i] on other empty 
                buckets can't solve the game either.
                """
                if bucket[i] == 0:
                    break
            return False

        return dfs(0)


if __name__ == '__main__':
    sol = Solution()
    res = sol.canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4)
    assert res is True, f"Expected {True}, got {res}"
