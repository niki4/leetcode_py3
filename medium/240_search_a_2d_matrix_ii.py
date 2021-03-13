"""
Write an efficient algorithm that searches for a target value in an m x n integer matrix.

The matrix has the following properties:
    Integers in each row are sorted in ascending from left to right.
    Integers in each column are sorted in ascending from top to bottom.

Constraints:
    m == matrix.length
    n == matrix[i].length
    1 <= n, m <= 300
    -109 <= matix[i][j] <= 109
    All the integers in each row are sorted in ascending order.
    All the integers in each column are sorted in ascending order.
    -109 <= target <= 109
"""
from typing import List


class Solution:
    """
    Runtime: 184 ms, faster than 23.60% of Python3
    Memory Usage: 20.6 MB, less than 31.15% of Python3

    Time complexity: O(R logN) where R is number of rows and N is number of elements in the row. At worst case we will
    have to visit all elements thus complexity O(N logN).
    Space complexity: O(1)
    """

    def binary_search(self, row, left, right, target):
        while left <= right:
            mid = (left + right) // 2
            if row[mid] == target:
                return True
            if target < row[mid]:  # go left
                right = mid - 1
            else:  # go right
                left = mid + 1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if (
                    row[0] <= target <= row[-1]) and (
                    self.binary_search(row, 0, len(row) - 1, target)):
                return True
        return False


if __name__ == '__main__':
    matrix_ = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30],
    ]
    sol = Solution()
    assert sol.searchMatrix(matrix_, 5) is True
    assert sol.searchMatrix(matrix_, 20) is False
