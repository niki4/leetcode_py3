"""
This question is about implementing a basic elimination algorithm for Candy Crush.

Given an m x n integer array board representing the grid of candy where board[i][j] represents the type of candy.
A value of board[i][j] == 0 represents that the cell is empty.

The given board represents the state of the game following the player's move. Now, you need to restore the board to a
stable state by crushing candies according to the following rules:
-   If three or more candies of the same type are adjacent vertically or horizontally, crush them all at the same
        time - these positions become empty.
-   After crushing all candies simultaneously, if an empty space on the board has candies on top of itself, then
        these candies will drop until they hit a candy or bottom at the same time. No new candies will drop outside the
        top boundary.
-   After the above steps, there may exist more candies that can be crushed. If so, you need to repeat the above steps.
-   If there does not exist more candies that can be crushed (i.e., the board is stable), then return the current board.

You need to perform the above rules until the board becomes stable, then return the stable board.

Constraints:
    m == board.length
    n == board[i].length
    3 <= m, n <= 50
    1 <= board[i][j] <= 2000
"""
from typing import List


class Solution:
    """
    LC solution: leetcode.com/problems/candy-crush/discuss/109220/155-ms-Python-with-detailed-explanation-beat-100

    Runtime: 156 ms, faster than 99.01% of Python3
    Memory Usage: 14.6 MB, less than 13.65% of Python3
    """

    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        if not board or not board[0]:
            return board
        """
        Rotate the board will make the drop operation much easier. That being said, instead of 
        move all non-zero value to the end of each column, the drop operation becomes move all 
        non-zero value to the beginning of each row.
        https://discuss.leetcode.com/assets/uploads/files/1512251917616-rotate-resized.png
        """
        board = self.transpose_clockwise(board)
        m, n = len(board), len(board[0])
        while True:  # repeat crush and drop
            crushed_candy = set()

            # check every row
            for i in range(m):
                for j in range(2, n):
                    if board[i][j] and board[i][j] == board[i][j - 1] == board[i][j - 2]:
                        crushed_candy |= {(i, j), (i, j - 1), (i, j - 2)}  # |= is the union operation for set
            # check every col
            for j in range(n):
                for i in range(2, m):
                    if board[i][j] and board[i][j] == board[i - 1][j] == board[i - 2][j]:
                        crushed_candy |= {(i, j), (i - 1, j), (i - 2, j)}

            if not crushed_candy:
                break
            for x, y in crushed_candy:
                board[x][y] = 0

            for i in range(m):
                row = [v for v in board[i] if v != 0]  # filter for non-zero values
                board[i] = row + [0] * (n - len(row))  # append zeroes to end (right) after non-zero values
        for _ in range(3):  # return back to original shape
            board = self.transpose_clockwise(board)
        return board

    def transpose_clockwise(self, board):
        m, n = len(board), len(board[0])
        output = [[0] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                output[j][m - 1 - i] = board[i][j]
        return output


if __name__ == '__main__':
    solutions = [Solution]
    tc = (
        ([[110, 5, 112, 113, 114],
          [210, 211, 5, 213, 214],
          [310, 311, 3, 313, 314],
          [410, 411, 412, 5, 414],
          [5, 1, 512, 3, 3],
          [610, 4, 1, 613, 614],
          [710, 1, 2, 713, 714],
          [810, 1, 2, 1, 1],
          [1, 1, 2, 2, 2],
          [4, 1, 4, 4, 1014]],
         [[0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [110, 0, 0, 0, 114],
          [210, 0, 0, 0, 214],
          [310, 0, 0, 113, 314],
          [410, 0, 0, 213, 414],
          [610, 211, 112, 313, 614],
          [710, 311, 412, 613, 714],
          [810, 411, 512, 713, 1014]]
         ),
        ([[1, 3, 5, 5, 2],
          [3, 4, 3, 3, 1],
          [3, 2, 4, 5, 2],
          [2, 4, 4, 5, 5],
          [1, 4, 4, 1, 1]],
         [[1, 3, 0, 0, 0],
          [3, 4, 0, 5, 2],
          [3, 2, 0, 3, 1],
          [2, 4, 0, 5, 2],
          [1, 4, 3, 1, 1]]
         ),
    )
    for sol in solutions:
        for inp_board, exp_board in tc:
            assert sol().candyCrush(inp_board) == exp_board
