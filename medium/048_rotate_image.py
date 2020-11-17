"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.

Constraints:
matrix.length == n
matrix[i].length == n
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000
"""
from typing import List


class Solution:
    """
    Runtime: 32 ms, faster than 81.41% of Python3
    Memory Usage: 14.3 MB, less than 8.66% of Python3
    """

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        flipped = zip(*matrix)  # generates pairs like (1, 4, 7)
        for i, v in enumerate(flipped):
            matrix[i] = list(reversed(v))


class Solution2:
    """
    Transpose and then reverse

    Runtime: 36 ms, faster than 55.34% of Python3
    Memory Usage: 14 MB, less than 86.72% of Python3

    Time complexity: O(N**2)
    Space complexity: O(1)
    """

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # matrix.reverse() before transpose; or after - matrix[i].reverse()
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            matrix[i].reverse()


if __name__ == "__main__":
    def get_tc():
        return [
            ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[7, 4, 1], [8, 5, 2], [9, 6, 3]]),
            ([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]],
             [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]),
            ([[1]], [[1]]),
            ([[1, 2], [3, 4]], [[3, 1], [4, 2]]),
        ]


    solutions = [Solution(), Solution2()]
    for sol in solutions:
        for matrix, expected in get_tc():
            sol.rotate(matrix)
            assert matrix == expected, f'got: {matrix}\nwant: {expected}'
