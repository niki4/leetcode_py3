"""
Alice and Bob take turns playing a game, with Alice starting first.

Initially, there is a number N on the chalkboard.
On each player's turn, that player makes a move consisting of:

Choosing any x with 0 < x < N and N % x == 0.
Replacing the number N on the chalkboard with N - x.
Also, if a player cannot make a move, they lose the game.

Return True if and only if Alice wins the game,
assuming both players play optimally.

Example 1:
Input: 2
Output: true
Explanation: Alice chooses 1, and Bob has no more moves.

Example 2:
Input: 3
Output: false
Explanation: Alice chooses 1, Bob chooses 1, and Alice has no more moves.


Note:
1 <= N <= 1000
"""

class Solution:
    """
    Runtime: 36 ms, faster than 89.70% of Python3.
    Memory Usage: 13.1 MB, less than 67.43% of Python3.

    Even nums always lead to win Alice. Accordingly, odd nums leads to loose.
    """
    def divisorGame(self, N: int) -> bool:
        return N % 2 == 0


if __name__ == "__main__":
    s = Solution()
    assert s.divisorGame(2) == True  # for N=2 possible option is only 1 (0<x<N) and Alice takes this before Bob
    assert s.divisorGame(3) == False # Base case on reducing odd N is 1 (so literally 0<x<1), so Bob's turn will be the last
