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

    Time complexity: O((M+N)(log(M+N)) log log(M+N)^2)
    Space complexity: O(1)
    """

    def uniquePaths(self, m: int, n: int) -> int:
        return int(
            factorial(m + n - 2) / factorial(m - 1) / factorial(n - 1))


class Solution2:
    """
    Runtime: 32 ms, faster than 96.37% of Python3.
    Memory Usage: 13.3 MB, less than 22.42% of Python3.

    Dynamic Programming.
    Time/Space complexity: O(m * n)

    On each step use prev result to calculate possible steps. E.g., for 3x7 grid:
    In [77]: sol.uniquePaths(3, 7)
        j:1	 	1 + 1    d[1]: 2
        j:2	 	2 + 1    d[2]: 3
        j:3	 	3 + 1    d[3]: 4
        j:4	 	4 + 1    d[4]: 5
        j:5	 	5 + 1    d[5]: 6
        j:6	 	6 + 1    d[6]: 7
        ------
        j:1	 	1 + 2    d[1]: 3
        j:2	 	3 + 3    d[2]: 6
        j:3	 	6 + 4    d[3]: 10
        j:4	 	10 + 5    d[4]: 15
        j:5	 	15 + 6    d[5]: 21
        j:6	 	21 + 7    d[6]: 28
        ------
        Out[77]: 28
    """

    def uniquePaths(self, m: int, n: int) -> int:
        d = [1] * n
        for _ in range(1, m):
            for j in range(1, n):
                d[j] = d[j - 1] + d[j]
        return d[-1] if m and n else 0


class Solution3:
    """
    Short recursive solution. But got TLE from LC.

    The idea is that from any position (starting from top left corner) we can move either down (m - 1) or right (n - 1).
    So for any given position we can recursively calculate possible steps from there.
    The downwards is that we repeatedly re-calculate steps for each position.

    Time complexity: O(m^n)
    """

    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)


class Solution4:
    """
    Optimized Solution3 - using DP with memoization.

    Runtime: 36 ms, faster than 15.98% of Python3
    Memory Usage: 14.3 MB, less than 38.60% of Python3

    Time complexity: O(m * n)
    Space complexity: O(m * n) for memo and recursion stack
    """

    def uniquePaths(self, m: int, n: int) -> int:
        memo = dict()

        def helper(m_, n_):
            if (m_, n_) in memo:
                return memo[(m_, n_)]

            if m_ == 1 or n_ == 1:
                return 1

            res = helper(m_ - 1, n_) + helper(m_, n_ - 1)
            memo[(m_, n_)] = res
            return res

        result = helper(m, n)
        return result


if __name__ == "__main__":
    solutions = [Solution(), Solution2(), Solution3(), Solution4()]
    tc = (
        (7, 3, 28),
        (3, 7, 28),
        (3, 2, 3),
        (3, 3, 6),
        (1, 2, 1)
    )
    for sol in solutions:
        for inp_m, inp_n, exp_res in tc:
            assert sol.uniquePaths(inp_m, inp_n) == exp_res
