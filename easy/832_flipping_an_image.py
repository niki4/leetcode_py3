"""
Given a binary matrix A, we want to flip the image horizontally,
then invert it, and return the resulting image.

To flip an image horizontally means that each row of the image is reversed.
For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].

To invert an image means that each 0 is replaced by 1, and each 1 is
replaced by 0. For example, inverting [0, 1, 1] results in [1, 0, 0].

Example 1:
Input: [[1,1,0],[1,0,1],[0,0,0]]
Output: [[1,0,0],[0,1,0],[1,1,1]]

Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
"""

class Solution:
    def flipAndInvertImage(self, A: list) -> list:
        """
        Runtime: 44 ms, faster than 97.58% of Python3.
        Memory Usage: 13 MB, less than 74.15% of Python3.
        """
        result = list()
        for row in A:
            result.append(row[::-1])

        for i in range(len(result)):
            for j in range(len(result[i])):
                result[i][j] = 0 if result[i][j] else 1

        return result


if __name__ == "__main__":
    src = [[1,1,0],[1,0,1],[0,0,0]]
    exp = [[1,0,0],[0,1,0],[1,1,1]]
    sol = Solution()
    res = sol.flipAndInvertImage(src)
    for row in range(len(src)):
        # print('res[row]:', res[row], 'exp[row]:', exp[row])
        assert res[row] == exp[row]
