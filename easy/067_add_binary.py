"""
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"

"""


# Runtime: 44 ms (Your runtime beats 98.30 % of python3 submissions.)
# Status: Accepted (https://leetcode.com/submissions/detail/151581806/)
class Solution1:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return format(int(a, 2) + int(b, 2), 'b')


# Runtime: 44 ms (Your runtime beats 98.30 % of python3 submissions.)
# Status: Accepted (https://leetcode.com/submissions/detail/151579081/)
class Solution2:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(int(a, 2) + int(b, 2))[2:]


class Solution3:
    """
    Bit manipulation approach.
    Algorithm:
        * Convert a and b into integers x and y, x will be used to keep an answer, and y for the carry.
        * While carry is nonzero: y != 0:
            -> Current answer without carry is XOR of x and y: answer = x^y.
            -> Current carry is left-shifted AND of x and y: carry = (x & y) << 1.
            -> Job is done, prepare the next loop: x = answer, y = carry.
        * Return x in the binary form.

    Runtime: 40 ms, faster than 11.17% of Python3
    Memory Usage: 14.3 MB, less than 12.26% of Python3
    """

    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        x, y = int(a, 2), int(b, 2)
        while y:
            # x holds XOR result, y remember carry for the next computation
            x, y = x ^ y, (x & y) << 1
        return bin(x)[2:]


if __name__ == '__main__':
    solutions = [Solution1(), Solution2(), Solution3()]
    tc = [
        ("11", "1", "100"),
        ("1010", "1011", "10101"),
    ]
    for s in solutions:
        for a_inp, b_inp, expected in tc:
            assert s.addBinary(a_inp, b_inp) == expected
