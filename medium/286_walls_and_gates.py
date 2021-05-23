"""
You are given an m x n grid rooms initialized with these three possible values.
    -1      A wall or an obstacle.
    0       A gate.
    INF     Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that
            the  distance to a gate is less than 2147483647.

Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it
should be filled with INF.

Example 1: https://assets.leetcode.com/uploads/2021/01/03/grid.jpg
Input: rooms = [
    [2147483647,-1,0,2147483647],
    [2147483647,2147483647,2147483647,-1],
    [2147483647,-1,2147483647,-1],
    [0,-1,2147483647,2147483647]]
Output: [
    [3,-1,0,1],
    [2,2,1,-1],
    [1,-1,2,-1],
    [0,-1,3,4]]

Constraints:
    m == rooms.length
    n == rooms[i].length
    1 <= m, n <= 250
    rooms[i][j] is -1, 0, or 231 - 1.
"""
from typing import List


class Solution:
    """
    BFS (Breadth-first search)

    Runtime: 240 ms, faster than 96.14% of Python3
    Memory Usage: 18 MB, less than 32.27% of Python3

    Time complexity: O(m*n). We take m×n steps to reach all rooms.
    Space complexity: O(m*n). The space complexity depends on the queue's size.
                     We insert at most m×n points into the queue.
    """

    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        gate = 0  # start point
        empty_room = 2147483647  # cell that can be visited

        queue = list()
        height = len(rooms)
        width = len(rooms[0])

        for row in range(height):
            for col in range(width):
                if rooms[row][col] == gate:
                    queue.append((row, col))

        for row, col in queue:
            dist = rooms[row][col] + 1
            for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):  # directions: up, down, left, right
                r = row + dx
                c = col + dy
                # if within borders and cell can be visited, mark as visited with its distance
                if 0 <= r < height and 0 <= c < width and rooms[r][c] == empty_room:
                    rooms[r][c] = dist
                    queue.append((r, c))


if __name__ == '__main__':
    def get_tc():
        return (
            ([[2147483647, -1, 0, 2147483647],
              [2147483647, 2147483647, 2147483647, -1],
              [2147483647, -1, 2147483647, -1],
              [0, -1, 2147483647, 2147483647]],
             [[3, -1, 0, 1],
              [2, 2, 1, -1],
              [1, -1, 2, -1],
              [0, -1, 3, 4]]),
            ([[-1]], [[-1]]),
            ([[2147483647]], [[2147483647]]),
            ([[0]], [[0]]),
        )


    solutions = [Solution()]
    for sol in solutions:
        for inp_rooms, exp_result in get_tc():
            sol.wallsAndGates(inp_rooms)
            assert inp_rooms == exp_result
