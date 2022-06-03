"""
Given an m x n binary matrix filled with 0's and 1's, find the largest square
containing only 1's and return its area.

Example 1:
Input: matrix = [
    ["1","0","1","0","0"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    ["1","0","0","1","0"]]
Output: 4

Example 2:
Input: matrix = [
    ["0","1"],
    ["1","0"]]
Output: 1

Example 3:
Input: matrix = [["0"]]
Output: 0

Constraints:
    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 300
    matrix[i][j] is '0' or '1'.
"""

from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0]) if matrix else 0
        dp = [[0 for _ in range(cols+1)] for _ in range(rows+1)]
        max_sq_len = 0

        for i in range(1, rows+1):
            for j in range(1, cols+1):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min([   # bottom right
                        dp[i-1][j-1],  # top left
                        dp[i-1][j],    # top right
                        dp[i][j-1],    # bottom left
                    ]) + 1
                    max_sq_len = max(max_sq_len, dp[i][j])

        return max_sq_len ** 2


if __name__ == '__main__':
    solutions = [
        Solution(),
    ]
    tc = (
        ([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]], 4),
        ([["0","1"],["1","0"]], 1),
        ([["0"]], 0),
    )
    for sol in solutions:
        for inp_matrix, out_res in tc:
            res = sol.maximalSquare(inp_matrix)
            assert res == out_res, f'{res} != {out_res}'
