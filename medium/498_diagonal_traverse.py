"""
Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix
in diagonal order as shown in the below image.
https://assets.leetcode.com/uploads/2018/10/12/diagonal_traverse.png

Example:
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output:  [1,2,4,7,5,3,6,8,9]
"""
from collections import defaultdict
from typing import List


class Solution:
    """
    Runtime: 196 ms, faster than 46.02% of Python3
    Memory Usage: 17.2 MB, less than 5.05% of Python3
    """

    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        m = len(matrix)
        if not m: return result

        dd = defaultdict(list)  # set [] if no key exist
        # step 1: numbers are grouped by the diagonals.
        # nums in the same diagonal have same value of row+col sum
        for i in range(m):  # for each array...
            n = len(matrix[i])
            for j in range(n):  # ...traverse all elements
                dd[i + j].append(matrix[i][j])
        # step 2: place diagonals in the result list,
        # reverse elements for even diagonals (0th, 2nd, 4th, etc)
        for k in sorted(dd.keys()):
            result += dd[k] if k % 2 else dd[k][::-1]
        return result


class Solution2:
    """
    Slightly optimized version of first solution

    Runtime: 196 ms, faster than 46.02% of Python3
    Memory Usage: 17 MB, less than 5.93% of Python3
    """

    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        m = len(matrix)
        if not m: return result
        n = len(matrix[0])

        dd = defaultdict(list)
        for i in range(m):
            n = len(matrix[i])
            for j in range(n):
                dd[i + j].append(matrix[i][j])

        diagonal_count = m + n
        for k in range(diagonal_count + 1):
            result += dd[k] if k % 2 else dd[k][::-1]
        return result


if __name__ == '__main__':
    solutions = [Solution(), Solution2()]
    inp = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    out = [1, 2, 4, 7, 5, 3, 6, 8, 9]
    for s in solutions:
        result = s.findDiagonalOrder(inp)
        assert result == out, f'{s.__class__}: expected {out}, got {result}'
