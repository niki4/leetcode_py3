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


class Solution2:
    """
    Divide-And-Conquer (recursive) approach.

    Algorithm:
        Because this algorithm operates recursively, its correctness can be asserted via the correctness of its base
        and recursive cases.
    Base Case:
        For a sorted two-dimensional array, there are two ways to determine in constant time whether an arbitrary
        element target can appear in it. First, if the array has zero area, it contains no elements and therefore cannot
        contain target. Second, if target is smaller than the array's smallest element (found in the top-left corner) or
        larger than the array's largest element (found in the bottom-right corner), then it definitely is not present.
    Recursive Case:
        If the base case conditions have not been met, then the array has positive area and target could potentially be
        present. Therefore, we seek along the matrix's middle column for an index row such that
        matrix[row-1][mid] < target < matrix[row][mid]  (obviously, if we find target during this process, we
        immediately return true). The existing matrix can be partitioned into four submatrice around this index;
        the top-left and bottom-right submatrice cannot contain target (via the argument
        outlined in Base Case section), so we can prune them from the search space. Additionally, the bottom-left and
        top-right submatrice are sorted two-dimensional matrices, so we can recursively apply this algorithm to them.

    Runtime: 168 ms, faster than 40.83% of Python3
    Memory Usage: 21.2 MB, less than 6.46% of Python3

    Time complexity: O(N logN)
    Space complexity: O(logN)
    """

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        def search_rec(left, up, right, down):
            if left > right or up > down:  # no height or width
                return False

            # base case - target out of possible min/max values
            if target < matrix[up][left] or target > matrix[down][right]:
                return False

            mid = (left + right) // 2  # or "left + (right - left) // 2"

            # locate 'row' such that matrix[row-1][mid] < target < matrix[row][mid]
            row = up
            while row <= down and matrix[row][mid] <= target:
                if matrix[row][mid] == target:
                    return True
                row += 1

            return (search_rec(left, row, mid - 1, down) or  # bottom-left submatrice
                    search_rec(mid + 1, up, right, row - 1))  # top-right submatrice

        return search_rec(0, 0, len(matrix[0]) - 1, len(matrix) - 1)


if __name__ == '__main__':
    solutions = [Solution(), Solution2()]
    matrix_ = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30],
    ]
    for sol in solutions:
        assert sol.searchMatrix(matrix_, 5) is True
        assert sol.searchMatrix(matrix_, 20) is False
