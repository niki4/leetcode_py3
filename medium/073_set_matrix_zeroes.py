"""
Given an m x n matrix. If an element is 0, set its entire row and column to 0. Do it in-place.

Follow up:
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
"""
from typing import List


class Solution:
    """
    Runtime: 120 ms, faster than 96.94% of Python3
    Memory Usage: 15.1 MB, less than 46.88% of Python3

    Time complexity: O(M*N) where M and N are number of rows and columns respectively
    Space complexity: O(M + N)
    """

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_idxs = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    zero_idxs.add((i, j))

        for i, j in zero_idxs:
            # set entire row to 0, in place
            matrix[i][:] = [0] * len(matrix[i])
            # set entire column to 0, in place
            for k in range(len(matrix)):
                matrix[k][j] = 0


if __name__ == '__main__':
    def get_tc():
        return (([
                     [1, 1, 1],
                     [1, 0, 1],
                     [1, 1, 1]],
                 [
                     [1, 0, 1],
                     [0, 0, 0],
                     [1, 0, 1]
                 ]),
                ([
                     [0, 1, 2, 0],
                     [3, 4, 5, 2],
                     [1, 3, 1, 5]],
                 [
                     [0, 0, 0, 0],
                     [0, 4, 5, 0],
                     [0, 3, 1, 0]]))


    solutions = [Solution()]
    for s in solutions:
        for inp_matrix, exp_matrix in get_tc():
            s.setZeroes(inp_matrix)
            assert inp_matrix == exp_matrix
