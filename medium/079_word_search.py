"""
Given an m x n board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where "adjacent" cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 3:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
"""
from typing import List


class Solution:
    """
    Algorithm: combination of DFS with Backtracking

    Runtime: 364 ms, faster than 55.16% of Python3
    Memory Usage: 15.7 MB, less than 53.07% of Python3

    Time Complexity: O(N * 3^L) where N is the number of cells in the board and L
    is the length of the word to be matched.
    Space Complexity:O(L) where L is the length of the word to be matched.
    """

    def __init__(self):
        self.grid = list()
        self.r_len = 0
        self.c_len = 0

    def exist(self, board: List[List[str]], word: str) -> bool:
        # board[:] makes a new (copy of the) list;
        # if we apply backtracking as here it's not necessary, but still good practice to avoid side-effects.
        # See Solution2 which has no such side-effect (albeit in cost of additional memory used to store local copy)
        self.grid = board
        self.r_len = len(self.grid)
        self.c_len = len(self.grid[0])

        for row in range(self.r_len):
            for col in range(self.c_len):
                if self._check_word(row, col, word):
                    return True
        # all cells verified, no match
        return False

    def _check_word(self, row: int, col: int, suffix: str):
        if not suffix:  # found match of the word
            return True

        if (row < 0 or
                col < 0 or
                row >= self.r_len or
                col >= self.c_len or
                self.grid[row][col] != suffix[0]):
            return False

        self.grid[row][col] = "*"  # mark as visited to skip next time

        ret = False
        for r_offset, c_offset in ((1, 0), (-1, 0), (0, 1), (0, -1)):  # down, up, right, left
            ret = self._check_word(row + r_offset, col + c_offset, suffix[1:])
            if ret:
                break  # break instead of return directly to do some cleanup afterwards

        # backtrack (revert change) before next iteration (starting point)
        self.grid[row][col] = suffix[0]
        # tried all directions from given point and didn't find any match
        return ret


class Solution2:
    """
    Runtime: 376 ms, faster than 46.77% of Python3
    Memory Usage: 15.8 MB, less than 40.53% of Python3
    """

    def __init__(self):
        self.grid = list()
        self.r_len = 0
        self.c_len = 0

    def exist(self, board: List[List[str]], word: str) -> bool:
        # board[:] makes a new (copy of the) list,
        # so self.grid changes won't affect source "board"
        self.grid = board[:]
        self.r_len = len(self.grid)
        self.c_len = len(self.grid[0])

        for row in range(self.r_len):
            for col in range(self.c_len):
                if self._check_word(row, col, word):
                    return True
        # all cells verified, no match
        return False

    def _is_valid_char(self, row: int, col: int, ch: str):
        if (row < 0 or
                col < 0 or
                row >= self.r_len or
                col >= self.c_len or
                self.grid[row][col] != ch):
            return False
        return True

    def _check_word(self, row: int, col: int, suffix: str):
        """ combination of DFS with Backtrack """
        if suffix == "":  # found match of the word
            return True

        if not self._is_valid_char(row, col, suffix[0]):  # adds overhead on calls, extracted in sake of readability
            return False

        self.grid[row][col] = "*"  # mark as visited to skip next time

        for r_offset, c_offset in ((1, 0), (-1, 0), (0, 1), (0, -1)):  # down, up, right, left
            if self._check_word(row + r_offset, col + c_offset, suffix[1:]):
                return True  # sudden-death return, no cleanup.

        # backtrack (revert change) before next iteration (starting point)
        self.grid[row][col] = suffix[0]
        # tried all directions from given point and didn't find any match
        return False


if __name__ == '__main__':
    solutions = [Solution, Solution2]
    tc = (
        ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED", True),
        ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE", True),
        ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB", False),
    )
    for s in solutions:
        for inp_board, inp_word, exp in tc:
            assert s().exist(inp_board, inp_word) is exp
