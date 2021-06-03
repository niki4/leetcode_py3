"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate
a queen and an empty space, respectively.

Example 1:
https://assets.leetcode.com/uploads/2020/11/13/queens.jpg
    Input: n = 4
    Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
    Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
Example 2:
    Input: n = 1
    Output: [["Q"]]

Constraints:
    1 <= n <= 9
"""
from typing import List


class Solution:
    """
    Runtime: 104 ms, faster than 42.03% of Python3
    Memory Usage: 14.7 MB, less than 53.49% of Python3

    Time complexity: O(N!), where N is the number of queens (which is the same as the width and height of the board).
    Space complexity: O(N^2), we use 3 sets used to store board state, as well as the recursion call stack.
    """

    def solveNQueens(self, n: int) -> List[List[str]]:
        board_solutions = []

        def backtrack(row, diagonals, anti_diagonals, columns, solution):
            if row == n:  # we reached end of board, all N queens are placed, found solution
                board_solutions.append(list(solution))  # make a copy to avoid side effects
                return

            for col in range(n):
                curr_diagonal = row - col
                curr_anti_diagonal = row + col
                if (  # queen cannot be placed here
                        curr_diagonal in diagonals or
                        curr_anti_diagonal in anti_diagonals or
                        col in columns
                ):
                    continue

                # place queen
                diagonals.add(curr_diagonal)
                anti_diagonals.add(curr_anti_diagonal)
                columns.add(col)
                solution.append("".join("Q" if i == col else "." for i in range(n)))

                # go to next row (to put another candidate, etc.)
                backtrack(row + 1, diagonals, anti_diagonals, columns, solution)

                # remove queen (candidate backtracking) to try with the other one (if left some)
                diagonals.remove(curr_diagonal)
                anti_diagonals.remove(curr_anti_diagonal)
                columns.remove(col)
                solution.pop()

        backtrack(0, set(), set(), set(), list())
        return board_solutions


if __name__ == '__main__':
    solutions = [Solution()]
    tc = (
        (4, [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]),
        (1, [["Q"]]),
    )
    for sol in solutions:
        for inp_n, exp_output in tc:
            assert sol.solveNQueens(inp_n) == exp_output
