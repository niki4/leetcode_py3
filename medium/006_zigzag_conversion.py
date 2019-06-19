"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a
given number of rows like this: (you may want to display this pattern
in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion
given a number of rows:

string convert(string s, int numRows);

Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
"""


class Solution:
    """
    Runtime: 52 ms, faster than 99.34% of Python3.
    Memory Usage: 13.2 MB, less than 74.35% of Python3.

    Algorithm idea:
        1. Preallocate lists/strs with number == numRows
        2. Starting from idx=0, iterate over 's' string and append/add letter to the end of the according list/str
        3. At each iteration check direction (+1 to move down and -1 to move up) and flip it on corners
    """
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        line_idx, incr = 0, 1
        output = [''] * numRows

        for i in range(len(s)):
            output[line_idx] += s[i]
            line_idx += incr
            if line_idx == 0 or line_idx == numRows - 1:
                incr *= -1
        return ''.join(output)


class Solution2:
    """
    Runtime: 60 ms, faster than 93.85% of Python3.
    Memory Usage: 13.3 MB, less than 56.12% of Python3.
    """
    def location(self, bound):
        index, inc = 0, 1
        while True:
            yield index
            if index == bound:
                inc = -1
            elif index == 0:
                inc = 1
            index += inc

    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        zig = [''] * numRows
        loc = self.location(numRows-1)
        for c, l in zip(s, loc):
            zig[l] += c
        return ''.join(zig)


class Solution3:
    """
    Runtime: 72 ms, faster than 67.62% of Python3.
    Memory Usage: 13.4 MB, less than 24.29% of Python3.
    """
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        array = [[] for _ in range(numRows)]

        layer = 0
        direction = 1
        for i in range(len(s)):
            array[layer].append(s[i])
            layer += direction  # either top down (+1) or down top (-1)
            if layer == numRows:
                layer = numRows-2
                direction = -1
            elif layer == -1:
                layer = 1
                direction = 1
        result = ''
        for line in array:
            result += ''.join(line)
        return result


if __name__ == "__main__":
    sol1 = Solution().convert
    sol2 = Solution2().convert
    sol3 = Solution3().convert
    s = 'PAYPALISHIRING'
    assert sol1(s, 3) == sol2(s, 3) == sol3(s, 3) == 'PAHNAPLSIIGYIR'
    assert sol1(s, 4) == sol2(s, 4) == sol3(s, 4) == 'PINALSIGYAHRPI'
