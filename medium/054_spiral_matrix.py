"""
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
1 -> 2 -> 3
          |
4 -> 5    6
|         |
7 <- 8 <- 9
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

"""

from typing import List


class Solution:
    """
    Runtime: 32 ms, faster than 49.23% of Python3
    Memory Usage: 14.4 MB, less than 10.72% of Python3
    """

    def isNextRightMoveAllowed(self, j, r_border) -> bool:
        return j < r_border

    def isNextLeftMoveAllowed(self, j, l_border) -> bool:
        return l_border < j

    def isNextUpMoveAllowed(self, i, u_border) -> bool:
        return i > u_border

    def isNextDownMoveAllowed(self, i, d_border) -> bool:
        return i < d_border

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if not matrix or not matrix[0]:
            return res

        m = len(matrix) - 1  # num of arrays (vertical)
        n = len(matrix[0]) - 1  # num of elements in each array (horizontal)
        # print('matrix', matrix, f'\nn {n}, m {m}')
        u_border = 0
        l_border = 0
        d_border = m
        r_border = n

        i, j = 0, 0  # start position from top left corner
        direction = 'right'

        while u_border <= d_border and l_border <= r_border:
            # print('res', res)
            # print(f'i {i}, j {j}, matrix[i][j] {matrix[i][j]}, direction {direction}')
            res.append(matrix[i][j])

            if direction == 'right':
                if self.isNextRightMoveAllowed(j, r_border):
                    j += 1  # move right
                else:
                    if self.isNextDownMoveAllowed(i, d_border):
                        i += 1
                    u_border += 1
                    direction = 'down'
            elif direction == 'down':
                if self.isNextDownMoveAllowed(i, d_border):
                    i += 1  # move down
                else:
                    if self.isNextLeftMoveAllowed(j, l_border):
                        j -= 1
                    r_border -= 1
                    direction = 'left'
            elif direction == 'left':
                if self.isNextLeftMoveAllowed(j, l_border):
                    j -= 1  # move left
                else:
                    if self.isNextUpMoveAllowed(i, u_border):
                        i -= 1
                    d_border -= 1
                    direction = 'up'
            elif direction == 'up':
                if self.isNextUpMoveAllowed(i, u_border):
                    i -= 1  # move up
                else:
                    if self.isNextRightMoveAllowed(j, r_border):
                        j += 1
                    l_border += 1
                    direction = 'right'
        return res


class Solution2:
    """
    Time / Space complexity: O(n)
    """
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        spiral = list()
        m, n = len(matrix), len(matrix[0])  # m - rows, n - cols
        size = m * n
        r1, c1 = 0, 0      # top left
        r2, c2 = m-1, n-1  # right bottom

        while len(spiral) < size:  # traverse elements in spiral order
            j = c1
            while j <= c2 and len(spiral) < size:  # go right
                spiral.append(matrix[r1][j])
                j += 1
            r1 += 1  # one step down / skip visited row next time

            i = r1
            while i <= r2 and len(spiral) < size:  # go down
                spiral.append(matrix[i][c2])
                i += 1
            c2 -= 1  # one step left / skip visited column next time

            j = c2
            while j >= c1 and len(spiral) < size:
                spiral.append(matrix[r2][j])
                j -= 1
            r2 -= 1  # one step up / skip visited row next time

            i = r2
            while i >= r1 and len(spiral) < size:
                spiral.append(matrix[i][c1])
                i -= 1
            c1 += 1  # one step right / skip visited column next time

        return spiral


if __name__ == '__main__':
    solutions = [
        Solution(),
        Solution2(),
        ]
    tc = [
        ([
             [1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5]),
        ([
             [1, 2, 3, 4],
             [5, 6, 7, 8],
             [9, 10, 11, 12]], [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]),
    ]

    for sol in solutions:
        for inp, expected in tc:
            result = sol.spiralOrder(inp)
            assert result == expected, f'\ninput:\t\t{inp}\nexpected:\t{expected}\ngot:\t\t{result}'
