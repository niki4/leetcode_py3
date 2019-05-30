"""
Given a matrix A, return the transpose of A.

The transpose of a matrix is the matrix flipped over it's main diagonal,
switching the row and column indices of the matrix.

Example 1:
Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]

Example 2:
Input: [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]

Note:
1 <= A.length <= 1000
1 <= A[0].length <= 1000
"""

class Solution:
    """
    Runtime: 60 ms, faster than 91.00% of Python3.
    Memory Usage: 13.8 MB, less than 30.99% of Python3.
    """
    def transpose(self, A: list) -> list:
        if not A:
            return []

        result_size = len(A[0])
        result = [None] * result_size

        for i in range(result_size):  # number of result lists
            temp = []
            for j in range(len(A)):   # number of source list
                temp.append(A[j][i])
            result[i] = temp
        return result


class Solution2:
    """
    Runtime: 64 ms, faster than 74.98% of Python3.
    Memory Usage: 13.8 MB, less than 25.37% of Python3.

    Probably, the most pythonic way to transpose matrix using zip() :)
    """
    def transpose(self, A: list) -> list:
        return [list(x) for x in zip(*A)]


if __name__ == "__main__":
    s = Solution()
    s2 = Solution2()
    input1 = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
        ]
    output1 = [
        [1,4,7],
        [2,5,8],
        [3,6,9]
        ]
    input2 = [
        [1,2,3],
        [4,5,6]
        ]
    output2 = [
        [1,4],
        [2,5],
        [3,6]
        ]
    assert s.transpose(input1) == output1
    assert s.transpose(input2) == output2
    assert s2.transpose(input1) == output1
    assert s2.transpose(input2) == output2
