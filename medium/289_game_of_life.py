"""
According to the Wikipedia's article: "The Game of Life, also known simply as Life,
is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0).
Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the
following four rules (taken from the above Wikipedia article):

1. Any live cell with fewer than two live neighbors dies, as if caused by under-population.
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies, as if by over-population.
4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its
current state. The next state is created by applying the above rules simultaneously
to every cell in the current state, where births and deaths occur simultaneously.

NB!    Do not return anything, modify board in-place instead.
"""

class Solution(object):
    """
    Runtime: 36 ms, faster than 93.24% of Python3.
    Memory Usage: 13 MB, less than 94.84% of Python3.

    Runtime complexity: O(N**2)
    Space complexity: O(1) as we store the middle result without use extra space, then
    using the result to create a new (final) result using conversion as below:

    living cells nearby | change | new value
    <2                    1->0     2
    2,3                   1->1     1
    >3                    1->0     2
    3                     0->1     3
    """
    def gameOfLife(self, board):
        if not board or not board[0]:
            return
        m, n = len(board), len(board[0])
        for i, row in enumerate(board):
            for j in range(len(row)):
                count = 0
                for a in range(max(0, i - 1), min(i + 2, m)):
                    for b in range(max(0, j - 1), min(j + 2, n)):
                        if (a, b) != (i, j) and 1 <= board[a][b] <= 2:
                            count += 1
                if board[i][j] == 0:
                    if count == 3:
                        board[i][j] = 3
                else:
                    if count < 2 or count > 3:
                        board[i][j] = 2
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 0
                elif board[i][j] == 3:
                    board[i][j] = 1


if __name__ == "__main__":
    s = Solution()
    src = [
        [0,1,0],
        [0,0,1],
        [1,1,1],
        [0,0,0]
    ]
    exp = [
        [0,0,0],
        [1,0,1],
        [0,1,1],
        [0,1,0]
    ]
    s.gameOfLife(src)
    assert src == exp
