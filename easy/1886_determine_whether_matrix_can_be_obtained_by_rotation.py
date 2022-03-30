"""
Given two n x n binary matrices mat and target, return true if it is possible to make mat equal
to target by rotating mat in 90-degree increments, or false otherwise.

Example 1:
    Input: mat = [[0,1],[1,0]], target = [[1,0],[0,1]]
    Output: true
    Explanation: We can rotate mat 90 degrees clockwise to make mat equal target.

Example 2:
    Input: mat = [[0,1],[1,1]], target = [[1,0],[0,1]]
    Output: false
    Explanation: It is impossible to make mat equal to target by rotating mat.

Example 3:
    Input: mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]]
    Output: true
    Explanation: We can rotate mat 90 degrees clockwise two times to make mat equal target.

Constraints:
    n == mat.length == target.length
    n == mat[i].length == target[i].length
    1 <= n <= 10
    mat[i][j] and target[i][j] are either 0 or 1.
"""

from typing import List


class Solution:
    """
    Time complexity: O(M) where M is the number of cells in the matrix.
    Space complexity: O(M) because we created deep copy of input array to work with. We'd reuse input array if need O(1) space.
    """
    def rotate_matrix(self, matrix: List[List[int]]):
        n = len(matrix)
        matrix.reverse()

        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        mat = [row[:] for row in mat]  # make deep copy to avoid side effects

        for _ in range(4):  # there's possible to rotate by 90*4=360° in total
            self.rotate_matrix(mat)
            if mat == target:
                return True

        return False


if __name__ == '__main__':
    solutions = [
        Solution(),
    ]
    tc = (
        ([[0,1],[1,0]], [[1,0],[0,1]], True),
        ([[0,1],[1,1]], [[1,0],[0,1]], False),
        ([[0,0,0],[0,1,0],[1,1,1]], [[1,1,1],[0,1,0],[0,0,0]], True),
    )
    for solution in solutions:
        for inp_matrix, inp_target, exp_res in tc:
            res = solution.findRotation(inp_matrix, inp_target)
            assert res is exp_res, f'{res} != {exp_res}'
