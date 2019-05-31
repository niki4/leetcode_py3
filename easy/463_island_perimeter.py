"""
You are given a map in form of a two-dimensional integer
grid where 1 represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally).
The grid is completely surrounded by water, and there is exactly
one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected
to the water around the island). One cell is a square with side length 1.
The grid is rectangular, width and height don't exceed 100.
Determine the perimeter of the island.

Example:
Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image below:
"""

class Solution:
    """
    Runtime: 260 ms, faster than 51.27% of Python3.
    Memory Usage: 13.5 MB, less than 54.12% of Python3.

    The algorithm is pretty simple:
    each spotted piece of island square has at maximum 4 sides, if it has any junction (neighbor),
    it will consume one side. Perimeter is sum of all sides that are not linked to any other.
    """

    def has_top_junction(self, grid: list, pos_i: int, pos_j: int) -> bool:
        if pos_i == 0:
            return False
        return grid[pos_i-1][pos_j] == 1

    def has_bottom_junction(self, grid: list, pos_i: int, pos_j: int) -> bool:
        if pos_i == len(grid)-1:
            return False
        return grid[pos_i+1][pos_j] == 1

    def has_left_junction(self, grid: list, pos_i: int, pos_j: int) -> bool:
        if pos_j == 0:
            return False
        return grid[pos_i][pos_j-1] == 1

    def has_right_junction(self, grid: list, pos_i: int, pos_j: int) -> bool:
        if pos_j == len(grid[pos_i])-1:
            return False
        return grid[pos_i][pos_j+1] == 1

    def islandPerimeter(self, grid: list) -> int:
        perimeter = int()

        for i in range(len(grid)):
            row = grid[i]
            for j in range(len(row)):
                if row[j] == 1:
                    cost = 4
                    if self.has_left_junction(grid, i, j):   cost -= 1
                    if self.has_right_junction(grid, i, j):  cost -= 1
                    if self.has_top_junction(grid, i, j):    cost -= 1
                    if self.has_bottom_junction(grid, i, j): cost -= 1
                    perimeter += cost

        return perimeter


if __name__ == "__main__":
    s = Solution()
    src = [
        [0,1,0,0],
        [1,1,1,0],
        [0,1,0,0],
        [1,1,0,0]]
    assert s.islandPerimeter(src) == 16
