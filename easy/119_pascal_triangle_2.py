"""
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:
Input: 3
Output: [1,3,3,1]
Follow up:
Could you optimize your algorithm to use only O(k) extra space?
"""

class Solution:
    """
    Runtime: 32 ms, faster than 96.32% of Python3.
    Memory Usage: 13.3 MB, less than 6.08% of Python3.

    Algorithm idea:
        Any row can be constructed using the offset sum of the previous row.
    Example:
           1 3 3 1 0
        +  0 1 3 3 1
        ------------
        =  1 4 6 4 1
    """
    def getRow(self, rowIndex: int) -> list:
        if rowIndex < 0 or not isinstance(rowIndex, int):
            return []

        res = [[1]]
        for _ in range(1, rowIndex+1):
            res.append(
                list(map(lambda x, y: x+y, res[-1] + [0], [0] + res[-1]))
            )
        return res[rowIndex]

class Solution2:
    """
    Runtime: 36 ms, faster than 88.58% of Python3.
    Memory Usage: 13.3 MB, less than 7.16% of Python3.

    The same idea as in Solution1, but using 'zip' instead 'map'
    and keeping only the last row to return.
    """
    def getRow(self, rowIndex: int) -> list:
        if rowIndex < 0 or not isinstance(rowIndex, int):
            return []

        row = [1]
        for _ in range(rowIndex):
            row = [x + y for x, y in zip([0]+row, row+[0])]
        return row


if __name__ == "__main__":
    s = Solution()
    s2 = Solution2()
    assert s.getRow(3) == s2.getRow(3) == [1, 3, 3, 1]
    assert s.getRow(0) == s2.getRow(0) == [1]
