"""
Determine if a 9 x 9 Sudoku board is valid.
Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note: A Sudoku board (partially filled) could be valid but is not necessarily solvable.
"""

from typing import List


class Solution:
    """
    Runtime: 92 ms, faster than 82.11% of Python3
    Memory Usage: 14.1 MB, less than 39.17% of Python3
    """

    def isValidSeq(self, seq: List[str]) -> bool:
        if len(seq) != 9:
            return False

        list_nums = [int(x) for x in seq if x != "."]
        if not list_nums:  # Only the filled cells need to be validated
            return True

        set_nums = set(list_nums)
        if len(list_nums) != len(set_nums):  # duplicated nums
            return False
        for n in set_nums:
            if n < 1 or n > 9:
                return False
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows
        for row in board:
            if not self.isValidSeq(row):
                return False

        # check columns
        for i in range(len(board)):
            col = [r[i] for r in board]
            if not self.isValidSeq(col):
                return False

        # check 3x3 squares; we have three 3x3 boxes at each 3rd row
        for i in range(0, len(board), 3):
            for col_idx in range(0, len(board[i]), 3):  # column to start from
                box = []
                for row_idx in range(i, i + 3):  # row to start from
                    box += board[row_idx][col_idx:col_idx + 3]  # items in flat list
                if not self.isValidSeq(box):
                    return False

        # All checks are passed
        return True


if __name__ == '__main__':
    sol = Solution()
    valid_board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    invalid_board = [  # there is duplicated 8 at the first column
        ["8", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    assert sol.isValidSudoku(valid_board)
    assert sol.isValidSudoku(invalid_board) is False
