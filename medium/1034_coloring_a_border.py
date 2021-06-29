"""
Given a 2-dimensional grid of integers, each value in the grid represents the color of the grid square at that location.

Two squares belong to the same connected component if and only if they have the same color and are next to each other
in any of the 4 directions.

The border of a connected component is all the squares in the connected component that are either 4-directionally
adjacent to a square not in the component, or on the boundary of the grid (the first or last row or column).

Given a square at location (r0, c0) in the grid and a color, color the border of the connected component of that square
with the given color, and return the final grid.

Example 1:
Input: grid = [[1,1],[1,2]], r0 = 0, c0 = 0, color = 3
Output: [[3, 3], [3, 2]]

Example 2:
Input: grid = [[1,2,2],[2,3,2]], r0 = 0, c0 = 1, color = 3
Output: [[1, 3, 3], [2, 3, 3]]

Example 3:
Input: grid = [[1,1,1],[1,1,1],[1,1,1]], r0 = 1, c0 = 1, color = 2
Output: [[2, 2, 2], [2, 1, 2], [2, 2, 2]]
"""
import collections
from typing import List


class Solution:
    """
    Breadth-first search (BFS)

    Runtime: 128 ms, faster than 72.93% of Python3
    Memory Usage: 14.5 MB, less than 40.60% of Python3
    """

    def colorBorder(self, grid: List[List[int]], r0: int, c0: int, color: int) -> List[List[int]]:
        m, n, init_color = len(grid), len(grid[0]), grid[r0][c0]
        bfs, component = collections.deque([(r0, c0)]), {(r0, c0)}
        while bfs:
            row, col = bfs.popleft()
            for i, j in (row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1):
                if (i, j) not in component:
                    if 0 <= i < m and 0 <= j < n and grid[i][j] == init_color:
                        component.add((i, j))
                        bfs.append((i, j))
                    else:
                        grid[row][col] = color  # border of the component just before the (i, j)
        return grid


class Solution2:
    """
    Depth-first search (DFS)

    Runtime: 120 ms, faster than 97.74% of Python3
    Memory Usage: 14.5 MB, less than 68.42% of Python3
    """

    def colorBorder(self, grid: List[List[int]], r0: int, c0: int, color: int) -> List[List[int]]:
        def dfs(row, col):
            if (row, col) in component:
                return True
            if not (0 <= row < m and 0 <= col < n and grid[row][col] == init_color):
                return False
            component.add((row, col))
            # connected component border cell may have at most 3 neighbor of the same original color (component)
            if dfs(row + 1, col) + dfs(row - 1, col) + dfs(row, col + 1) + dfs(row, col - 1) < 4:
                grid[row][col] = color
            return True

        m, n, init_color, component = len(grid), len(grid[0]), grid[r0][c0], set()
        dfs(r0, c0)
        return grid


if __name__ == '__main__':
    def get_tc():
        return (([[1, 1], [1, 2]], 0, 0, 3, [[3, 3], [3, 2]]),
                ([[1, 2, 2], [2, 3, 2]], 0, 1, 3, [[1, 3, 3], [2, 3, 3]]),
                ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 1, 1, 2, [[2, 2, 2], [2, 1, 2], [2, 2, 2]]),)


    solutions = [Solution(), Solution2()]

    for sol in solutions:
        for inp_grid, r_0, c_0, inp_color, exp_grid in get_tc():
            result = sol.colorBorder(inp_grid, r_0, c_0, inp_color)
            assert result == exp_grid, f"{sol.__class__.__name__}: expected {exp_grid}, got {result}"
