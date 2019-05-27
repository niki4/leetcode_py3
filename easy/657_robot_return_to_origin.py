"""
There is a robot starting at position (0, 0), the origin, on a 2D plane.
Given a sequence of its moves, judge if this robot ends up at (0, 0) after
it completes its moves.

The move sequence is represented by a string, and the character moves[i]
represents its ith move. Valid moves are R (right), L (left), U (up),
and D (down). If the robot returns to the origin after it finishes all
of its moves, return true. Otherwise, return false.

Note: The way that the robot is "facing" is irrelevant. "R" will always
make the robot move to the right once, "L" will always make it move
left, etc. Also, assume that the magnitude of the robot's movement is
the same for each move.

Example 1:

Input: "UD"
Output: true
Explanation: The robot moves up once, and then down once.
All moves have the same magnitude, so it ended up at the origin where
it started. Therefore, we return true.
"""

class Solution:
    """
    Runtime: 132 ms, faster than 5.63% of Python3.
    Memory Usage: 13.4 MB, less than 10.94% of Python3.

    Trivial and easy-to-understand, but slow solution.
    """
    def judgeCircle(self, moves: str) -> bool:
        horizontal_moves = []
        vertical_moves = []

        for mv in moves:
            if mv == 'U':
                if 'D' in vertical_moves:
                    vertical_moves.remove('D')
                else:
                    vertical_moves.append('U')
            elif mv == 'D':
                if 'U' in vertical_moves:
                    vertical_moves.remove('U')
                else:
                    vertical_moves.append('D')
            elif mv == 'L':
                if 'R' in horizontal_moves:
                    horizontal_moves.remove('R')
                else:
                    horizontal_moves.append('L')
            elif mv == 'R':
                if 'L' in horizontal_moves:
                    horizontal_moves.remove('L')
                else:
                    horizontal_moves.append('R')

        return (not horizontal_moves and not vertical_moves)


class Solution2:
    """
    Runtime: 68 ms, faster than 53.26% of Python3.
    Memory Usage: 13.1 MB, less than 84.93% of Python3.

    Faster solution using incr/decr counters.
    Could be improved if use single counter per horizontal/vertical moves.
    """
    def judgeCircle(self, moves: str) -> bool:
        moves_to_L = 0
        moves_to_R = 0
        moves_to_U = 0
        moves_to_D = 0

        for mv in moves:
            if mv == 'U':
                if moves_to_D:
                    moves_to_D -= 1
                else:
                    moves_to_U += 1
            elif mv == 'D':
                if moves_to_U:
                    moves_to_U -= 1
                else:
                    moves_to_D += 1
            elif mv == 'L':
                if moves_to_R:
                    moves_to_R -= 1
                else:
                    moves_to_L += 1
            elif mv == 'R':
                if moves_to_L:
                    moves_to_L -= 1
                else:
                    moves_to_R += 1

        return not any((moves_to_L, moves_to_R, moves_to_U, moves_to_D))


class Solution3:
    """
    Runtime: 60 ms, faster than 65.46% of Python3.
    Memory Usage: 13.3 MB, less than 39.12% of Python3.
    """
    def judgeCircle(self, moves: str) -> bool:
        move_counters = dict()

        for direction in moves:
            if direction in move_counters:
                move_counters[direction] += 1
            else:
                move_counters[direction] = 1

        return (
            move_counters.get('U') == move_counters.get('D') and
            move_counters.get('R') == move_counters.get('L')
        )


class Solution4:
    """
    Runtime: 40 ms, faster than 94.64% of Python3.
    Memory Usage: 13.3 MB, less than 37.84% of Python3.

    Using Python's built-in method.

    Despite the stat provided by Leetcode, this solution requires O(4*N)
    because of implicit loop over entire string at each count() call.
    """
    def judgeCircle(self, moves: str) -> bool:
        return moves.count('U') == moves.count('D') and moves.count('R') == moves.count('L')


if __name__ == "__main__":
    sol = Solution()
    sol2 = Solution2()
    sol3 = Solution2()
    sol4 = Solution2()
    assert sol.judgeCircle("UD") == True
    assert sol.judgeCircle("LL") == False
    assert sol2.judgeCircle("UD") == True
    assert sol2.judgeCircle("LL") == False
    assert sol3.judgeCircle("UD") == True
    assert sol3.judgeCircle("LL") == False
    assert sol4.judgeCircle("UD") == True
    assert sol4.judgeCircle("LL") == False
