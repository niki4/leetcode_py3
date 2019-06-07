"""
A robot is located at the top-left corner of a m x n grid
(marked 'Start' in the diagram below).
https://assets.leetcode.com/uploads/2018/10/22/robot_maze.png

The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid
(marked 'Finish' in the diagram below).

Note: m and n will be at most 100.

Example 1:
Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right

Example 2:
Input: m = 7, n = 3
Output: 28
"""

from math import factorial

class Solution:
    """
    Runtime: 36 ms, faster than 88.20% of Python3.
    Memory Usage: 13.3 MB, less than 22.42% of Python3.

    Math solution: total number of possible steps to get reach the end is S = M+N-2,
    and the number of downward movements is D = M-1. Then we need to calculate
    the number of combinations of D starting from S.

    The problem itself is a special case of 'Delannoy number'
    (https://en.wikipedia.org/wiki/Delannoy_number)
    """
    def uniquePaths(self, m: int, n: int) -> int:
        return int(
            factorial(m + n - 2) / factorial(m - 1) / factorial(n - 1))

class Solution2:
    """
    Runtime: 32 ms, faster than 96.37% of Python3.
    Memory Usage: 13.3 MB, less than 22.42% of Python3.

    Dynamic Programming.
    """
    def uniquePaths(self, m: int, n: int) -> int:
        d = [1] * n
        for _ in range(1, m):
            for j in range(1, n):
                d[j] = d[j-1] + d[j]
        return d[-1] if m and n else 0


if __name__ == "__main__":
    s1 = Solution().uniquePaths
    s2 = Solution2().uniquePaths
    assert s1(7, 3) == s2(7, 3) == 28
    assert s1(3, 2) == s2(3, 2) == 3
