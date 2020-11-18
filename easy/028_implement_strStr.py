"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2

Clarification:
What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string.
This is consistent to C's strstr() and Java's indexOf().
"""


class Solution:
    """
    Runtime: 28 ms, faster than 83.05% of Python3
    Memory Usage: 14.2 MB, less than 76.33% of Python3
    """

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not isinstance(needle, str) or needle == '':
            return 0

        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1


if __name__ == '__main__':
    solutions = [Solution()]
    tc = [
        ('hello', 'll', 2),
        ('aaaaa', 'bba', -1),
        ('Test', '', 0),
    ]
    for s in solutions:
        for hst, ndl, expected in tc:
            assert s.strStr(hst, ndl) == expected

#  Another 1-row solution for this is simply 'return haystack.find(needle)'
