"""
A matrix is Toeplitz if every diagonal from top-left
to bottom-right has the same element.

Now given an M x N matrix, return True if and only if the matrix is Toeplitz.

Example 1:  Input:
matrix = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]
Output: True
Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.

Example 2:  Input:
matrix = [
  [1,2],
  [2,2]
]
Output: False
Explanation:
The diagonal "[1, 2]" has different elements.
"""

class Solution:
    """
    Runtime: 44 ms, faster than 86.90% of Python3.
    Memory Usage: 13.2 MB, less than 55.87% of Python3.

    "Group by Category":
    We ask what feature makes two coordinates (r1, c1) and (r2, c2) belong to the same diagonal?

    It turns out two coordinates are on the same diagonal if and only if r1 - c1 == r2 - c2.

    This leads to the following idea: remember the value of that diagonal as groups[r-c].
    If we see a mismatch, the matrix is not Toeplitz; otherwise it is.

    Time Complexity: O(M*N)
        (Recall in the problem statement that M, NM,N are the number of rows and columns in matrix.)
    Space Complexity: O(M+N)
    """
    def isToeplitzMatrix(self, matrix: list) -> bool:
        groups = dict()
        for r_idx, row in enumerate(matrix):
            for c_idx, val in enumerate(row):
                if r_idx-c_idx not in groups:
                    groups[r_idx-c_idx] = val
                elif groups[r_idx-c_idx] != val:
                    return False
        return True

class Solution2:
    """
    Runtime: 44 ms, faster than 86.90% of Python3.
    Memory Usage: 13.1 MB, less than 83.91% of Python3.

    Algorithm idea: compare with top-left neighbor.
    Every element belongs to some diagonal, and it's previous element (if it exists)
    is it's top-left neighbor. Thus, for the square (r, c), we only need to check
    r == 0 OR c == 0 OR matrix[r-1][c-1] == matrix[r][c].

    Time Complexity: O(M*N), as defined in the problem statement.
    Space Complexity: O(1)
    """
    def isToeplitzMatrix(self, matrix: list) -> bool:
        return all(r == 0 or c == 0 or matrix[r-1][c-1] == val
        for r, row in enumerate(matrix)
        for c, val in enumerate(row))

if __name__ == "__main__":
    s = Solution()
    s2 = Solution2()
    matrix1 = [
        [1,2,3,4],
        [5,1,2,3],
        [9,5,1,2],
    ]
    matrix2 = [
        [1,2],
        [2,2]
    ]
    matrix3 = [
        [83],[64],[57]
        ]
    assert s.isToeplitzMatrix(matrix1) == True
    assert s.isToeplitzMatrix(matrix2) == False
    assert s.isToeplitzMatrix(matrix3) == True
    assert s2.isToeplitzMatrix(matrix1) == True
    assert s2.isToeplitzMatrix(matrix2) == False
    assert s2.isToeplitzMatrix(matrix3) == True
