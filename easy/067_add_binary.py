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


if __name__ == '__main__':
    print(Solution1().addBinary("11", "1"))       # "100"
    print(Solution2().addBinary("1010", "1011"))  # "10101"
