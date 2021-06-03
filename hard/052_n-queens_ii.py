"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example 1:
https://assets.leetcode.com/uploads/2020/11/13/queens.jpg
    Input: n = 4
    Output: 2
    Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
Example 2:
    Input: n = 1
    Output: 1

Constraints:
    1 <= n <= 9
"""


class Solution:
    """
    Runtime: 84 ms, faster than 34.83% of Python3
    Memory Usage: 14.3 MB, less than 30.65% of Python3

    Time complexity: O(N!), where N is the number of queens (which is the same as the width and height of the board).
    Space complexity: O(N), we use 3 sets used to store board state, as well as the recursion call stack.
    """

    def totalNQueens(self, n: int) -> int:
        def backtrack(row, diagonals, anti_diagonals, columns):
            # base case - N queens have been placed
            if row == n:
                return 1

            solutions = 0
            for col in range(n):  # iterate over columns on the specified row
                curr_diagonal = row - col
                curr_anti_diagonal = row + col
                if (  # queen is under attack at this position
                        curr_diagonal in diagonals or
                        curr_anti_diagonal in anti_diagonals or
                        col in columns):
                    continue

                # place queen (candidate)
                diagonals.add(curr_diagonal)
                anti_diagonals.add(curr_anti_diagonal)
                columns.add(col)

                # go to next row (to put another candidate, etc.)
                solutions += backtrack(row + 1, diagonals, anti_diagonals, columns)

                # remove queen (candidate backtracking) since we have already explored all valid paths
                # using the above function call
                diagonals.remove(curr_diagonal)
                anti_diagonals.remove(curr_anti_diagonal)
                columns.remove(col)
            return solutions

        return backtrack(0, set(), set(), set())


if __name__ == '__main__':
    solutions_ = [Solution()]
    tc = (
        (4, 2),
        (1, 1),
    )
    for sol in solutions_:
        for inp_n, exp_count in tc:
            assert sol.totalNQueens(inp_n) == exp_count
