"""
Assume the following rules are for the tic-tac-toe game on an n x n board between two players:
    1. A move is guaranteed to be valid and is placed on an empty block.
    2. Once a winning condition is reached, no more moves are allowed.
    3. A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.

Implement the TicTacToe class:
    TicTacToe(int n) Initializes the object the size of the board n.
    int move(int row, int col, int player) Indicates that player with id player plays at the cell (row, col) of
    the board. The move is guaranteed to be a valid move.

Follow up:
    Could you do better than O(n2) per move() operation?

Example 1:
Input
["TicTacToe", "move", "move", "move", "move", "move", "move", "move"]
[[3], [0, 0, 1], [0, 2, 2], [2, 2, 1], [1, 1, 2], [2, 0, 1], [1, 0, 2], [2, 1, 1]]
Output
[null, 0, 0, 0, 0, 0, 0, 1]

Constraints:
    2 <= n <= 100
    player is 1 or 2.
    1 <= row, col <= n
    (row, col) are unique for each different call to move.
    At most n2 calls will be made to move.

"""


class TicTacToe:
    """
    Bruteforce approach

    Runtime: 1204 ms, faster than 5.07% of Python3
    Memory Usage: 17 MB, less than 20.90% of Python3

    Time complexity: O(n**2) because we have to check the whole matrix after each move
    Space complexity: O(n**2) because we need to store n*n board
    """

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.board = [[-1] * n for _ in range(n)]

    def is_win(self, p_id: int) -> bool:
        """ Returns True if there win situation for current player, False otherwise """
        n = len(self.board)
        for i in range(n):
            if (all(p == p_id for p in self.board[i]) or  # row
                    all(self.board[j][i] == p_id for j in range(n))):  # col
                return True

        if (all(self.board[i][i] == p_id for i in range(n)) or  # top left - bottom right diagonal
                all(self.board[i][n - i - 1] == p_id for i in range(n))):  # top right - bottom left diagonal
            return True

        return False

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        self.board[row][col] = player
        return player if self.is_win(player) else 0


if __name__ == '__main__':
    ticTacToe = TicTacToe(3)
    # Assume that player 1 is "X" and player 2 is "O" in the board.

    assert ticTacToe.move(0, 0, 1) == 0  # return 0 (no one wins)
    # |X| | |
    # | | | |    // Player 1 makes a move at (0, 0).
    # | | | |

    assert ticTacToe.move(0, 2, 2) == 0  # return 0 (no one wins)
    # |X| |O|
    # | | | |    // Player 2 makes a move at (0, 2).
    # | | | |

    assert ticTacToe.move(2, 2, 1) == 0  # return 0 (no one wins)
    # |X| |O|
    # | | | |    // Player 1 makes a move at (2, 2).
    # | | |X|

    assert ticTacToe.move(1, 1, 2) == 0  # return 0 (no one wins)
    # |X| |O|
    # | |O| |    // Player 2 makes a move at (1, 1).
    # | | |X|

    assert ticTacToe.move(2, 0, 1) == 0  # return 0 (no one wins)
    # |X| |O|
    # | |O| |    // Player 1 makes a move at (2, 0).
    # |X| |X|

    assert ticTacToe.move(1, 0, 2) == 0  # return 0 (no one wins)
    # |X| |O|
    # |O|O| |    // Player 2 makes a move at (1, 0).
    # |X| |X|

    assert ticTacToe.move(2, 1, 1) == 1  # return 1 (player 1 wins)
    # |X| |O|
    # |O|O| |    // Player 1 makes a move at (2, 1).
    # |X|X|X|
