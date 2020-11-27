"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it.
https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif
"""
from typing import List


class Solution:
    """
    Runtime: 36 ms, faster than 86.90% of Python3.
    Memory Usage: 13.1 MB, less than 75.66% of Python3.

    Algorithm idea:
        1. The length of row equal to its sequential number (starting from one).
        2. The first and last nums of row are always 1, therefore they can be prepopulated.
        3. Values for current_row[1:len(current_row)-1] based on previous row sums,
        so that, e.g. cr[1] = pr[0] + pr[1], then cr[2] = pr[1] + pr[2] and so on.
    """
    def generate(self, numRows: int) -> list:
        pyramid = []
        for i in range(1, numRows+1):
            row = [0] * i
            row[0], row[-1] = 1, 1
            if not pyramid:
                pyramid.append(row)
                continue

            prev_row = pyramid[-1]
            for idx in range(1, len(prev_row)):
                row[idx] = prev_row[idx-1] + prev_row[idx]
            pyramid.append(row)

        return pyramid

class Solution2:
    """
    Runtime: 36 ms, faster than 86.90% of Python3.
    Memory Usage: 13 MB, less than 85.84% of Python3.

    Algorithm idea:
        Any row can be constructed using the offset sum of the previous row.
    Example:
           1 3 3 1 0
        +  0 1 3 3 1
        ------------
        =  1 4 6 4 1
    """

    def generate(self, numRows: int) -> list:
        if numRows <= 0 or not isinstance(numRows, int):
            return []

        res = [[1]]
        for _ in range(1, numRows):
            res.append(
                list(map(lambda x, y: x + y, res[-1] + [0], [0] + res[-1]))
            )
        return res


class Solution3:
    """
    DP approach. Simplified version of the first solution (the same idea behind).

    Runtime: 32 ms, faster than 50.83% of Python3
    Memory Usage: 14.3 MB, less than 8.78% of Python3
    """

    def generate(self, numRows: int) -> List[List[int]]:
        pyramid = []

        for i in range(numRows):  # curr row idx
            row = [1] * (i + 1)
            for j in range(1, len(row) - 1):  # first and last items already 1, so skip them
                row[j] = pyramid[i - 1][j - 1] + pyramid[i - 1][j]
            pyramid.append(row)

        return pyramid


if __name__ == "__main__":
    solutions = [Solution(), Solution2(), Solution3()]
    tc = [
        (0, []),
        (5, [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1],
        ])
    ]
    for s in solutions:
        for num_rows, exp in tc:
            assert s.generate(num_rows) == exp
