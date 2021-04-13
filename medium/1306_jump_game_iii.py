"""
Given an array of non-negative integers arr, you are initially positioned at start index of the array. When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach to any index with value 0.

Notice that you can not jump outside of the array at any time.

Example 1:
Input: arr = [4,2,3,0,3,1,2], start = 5
Output: true
Explanation:
    All possible ways to reach at index 3 with value 0 are:
    index 5 -> index 4 -> index 1 -> index 3
    index 5 -> index 6 -> index 4 -> index 1 -> index 3

Example 2:
Input: arr = [4,2,3,0,3,1,2], start = 0
Output: true
Explanation:
    One possible way to reach at index 3 with value 0 is:
    index 0 -> index 4 -> index 1 -> index 3

Example 3:
Input: arr = [3,0,2,1,2], start = 2
Output: false
Explanation: There is no way to reach at index 1 with value 0.

Constraints:
    1 <= arr.length <= 5 * 104
    0 <= arr[i] < arr.length
    0 <= start < arr.length
"""
from typing import List


class Solution:
    """
    DFS (Depth-First Search)

    Runtime: 284 ms, faster than 89.27% of Python3
    Memory Usage: 73.1 MB, less than 27.54% of Python3

    Time complexity: O(N), since we will visit every index only once.
    Space complexity: O(N) since it needs at most O(N) stacks for recursions.
    """

    def canReach(self, arr: List[int], start: int) -> bool:
        def dfs(idx: int, visited: List[int]) -> bool:
            if not (0 <= idx < len(arr) and visited[idx] >= 0):
                return False
            if arr[idx] == 0:
                return True
            visited[idx] = -visited[idx]  # mark idx as visited
            return dfs(idx + arr[idx], visited) or dfs(idx - arr[idx], visited)

        return dfs(start, arr[:])


if __name__ == '__main__':
    solutions = (
        Solution(),
    )
    tc = (
        ([4, 2, 3, 0, 3, 1, 2], 5, True),
        ([4, 2, 3, 0, 3, 1, 2], 0, True),
        ([3, 0, 2, 1, 2], 2, False),
    )
    for sol in solutions:
        for inp_nums, inp_start, exp_res in tc:
            res = sol.canReach(inp_nums, inp_start)
            assert res is exp_res, f"For input {inp_nums} -> Expected {exp_res}, got {res}"
