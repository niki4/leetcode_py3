"""
A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9
such that each row, column, and both diagonals all have the same sum.

Given an grid of integers, how many 3 x 3 "magic square" subgrids are there?
(Each subgrid is contiguous).

Example 1:
Input: [[4,3,8,4],
        [9,5,1,9],
        [2,7,6,2]]
Output: 1
Explanation:
The following subgrid is a 3 x 3 magic square:
4 3 8
9 5 1
2 7 6

while this one is not:
3 8 4
5 1 9
7 6 2

In total, there is only one magic square inside the given grid.

Note:
1 <= grid.length <= 10
1 <= grid[0].length <= 10
0 <= grid[i][j] <= 15
"""

class Solution:
    """
    Runtime: 40 ms, faster than 74.75% of Python3.
    Memory Usage: 13.1 MB, less than 53.74% of Python3.
    """
    def is_magic_square(self, matrix: [list, tuple]) -> bool:
        target_sum = sum(matrix[0])
        l2r_diagonal = r2l_diagonal = 0

        # check 'grid filled with distinct numbers "1 to 9" only'
        nums_flattened = sorted(item for sublist in matrix for item in sublist)
        if nums_flattened != list(range(1, 10)):
            return False

        for i in range(len(matrix)):  # check diagonal sums
            j = (len(matrix)-1)-i
            l2r_diagonal += matrix[i][i]
            r2l_diagonal += matrix[i][j]
        if l2r_diagonal != target_sum or r2l_diagonal != target_sum:
            return False

        for i in range(len(matrix)):
            if sum(matrix[i]) != target_sum:  # check row sums
                return False

            if sum(matrix[j][i] for j in range(len(matrix[i]))) != target_sum:  # check column sums
                return False

        return True


    def numMagicSquaresInside(self, grid: list) -> int:
        magic_squares_counter = 0

        for i in range(len(grid)-2):
            three_rows = grid[i:i+3]
            row_len = len(three_rows[0])
            for j in range(row_len-2):
                matrix_3x3 = [row[j:j+3] for row in three_rows]
                if self.is_magic_square(matrix_3x3):
                    magic_squares_counter += 1

        return magic_squares_counter


if __name__ == "__main__":
    s = Solution()
    src = [
        [4,3,8,4],
        [9,5,1,9],
        [2,7,6,2],
        ]
    src2 = [
        [1,1,1],
        [4,5,6],
        [9,9,9],
        ]
    src3 = [
        [8,7,4,1,7,2],
        [5,8,4,2,6,9],
        [4,2,1,4,2,8],
        [6,5,9,2,7,4],
        [8,2,3,9,5,3],
        [3,9,5,6,8,1],
        ]
    src4 = [
        [5,5,5],
        [5,5,5],
        [5,5,5],
        ]
    src5 = [
        [10,3,5],
        [1,6,11],
        [7,9,2],
        ]
    assert s.numMagicSquaresInside(src) == 1
    assert s.numMagicSquaresInside(src2) == 0
    assert s.numMagicSquaresInside(src3) == 0
    assert s.numMagicSquaresInside(src4) == 0
    assert s.numMagicSquaresInside(src5) == 0
