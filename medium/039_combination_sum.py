"""
Given a set of candidate numbers (candidates) (without duplicates)
and a target number (target), find all unique combinations
in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates
unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]

Example 2:
Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""


class Solution:
    """
    Runtime: 92 ms, faster than 56.86% of Python3.
    Memory Usage: 13.3 MB, less than 41.83% of Python3.
    """
    def combinationSum(self, candidates: list, target: int) -> list:
        def dfs(ans, current, current_sum, i):
            if current_sum == target:
                ans.append(current)
                return
            if current_sum > target:
                return
            for j in range(i, len(candidates)):
                dfs(ans, current + [candidates[j]], current_sum + candidates[j], j)

        ans = []
        dfs(ans, [], 0, 0)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum([2, 3, 6, 7], 7))
