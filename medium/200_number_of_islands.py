"""
Given a 2d grid map of '1's (land) and '0's (water),
count the number of islands. An island is surrounded
by water and is formed by connecting adjacent lands
horizontally or vertically. You may assume all four
edges of the grid are all surrounded by water.

Example 1:
Input:
    11110
    11010
    11000
    00000
Output: 1

Example 2:
Input:
    11000
    11000
    00100
    00011
Output: 3
"""


class Solution:
    """
    Runtime: 84 ms, faster than 62.09% of Python3.
    Memory Usage: 13.8 MB, less than 83.29% of Python3.

    Algorithm idea (Depth-First Search):
        1. Iteratively scan each cell
        2. If found any piece of island, recursively mark all the rest parts of this island ('*')
        3. Increase found islands count by 1, then proceed with scanning grid

    Time complexity: O(M×N) where M is the number of rows and N is the number of columns.
    Space complexity: O(M×N) in case that the grid map is filled with lands where DFS goes by M×N deep.
    """

    def numIslands(self, grid: list) -> int:
        self.grid = grid[:]
        islands_count = 0

        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                if self.grid[row][col] == '1':
                    self._dfs_mark_island_as_seen(row, col)
                    islands_count += 1
        return islands_count

    def _dfs_mark_island_as_seen(self, row: int, col: int):
        if (row < 0 or
                col < 0 or
                row >= len(self.grid) or
                col >= len(self.grid[0]) or
                self.grid[row][col] != '1'):
            return
        self.grid[row][col] = '*'
        self._dfs_mark_island_as_seen(row + 1, col)
        self._dfs_mark_island_as_seen(row - 1, col)
        self._dfs_mark_island_as_seen(row, col + 1)
        self._dfs_mark_island_as_seen(row, col - 1)


if __name__ == "__main__":
    s = Solution()
    src1 = [['1', '1', '1', '1', '0'],
            ['1', '1', '0', '1', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '0', '0', '0']]
    src2 = [['1', '1', '0', '0', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '1', '0', '0'],
            ['0', '0', '0', '1', '1']]
    assert s.numIslands(src1) == 1
    assert s.numIslands(src2) == 3
