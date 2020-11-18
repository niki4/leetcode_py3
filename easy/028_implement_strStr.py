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


class Solution2:
    """
    Runtime: 24 ms, faster than 95.03% of Python3
    Memory Usage: 14.4 MB, less than 20.96% of Python3
    """

    def strStr(self, haystack, needle):
        # str.find returns index of first substr occurrence, or -1 if not found
        return haystack.find(needle) if needle else 0


class Solution3:
    """
    Runtime: 20 ms, faster than 98.80% of Python3
    Memory Usage: 14.2 MB, less than 45.35% of Python3
    """

    def strStr(self, haystack, needle):
        if not needle:
            return 0
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1


if __name__ == '__main__':
    solutions = [Solution()]
    tc = [
        ('hello', 'll', 2),
        ('aaaaa', 'bba', -1),
        ('Test', '', 0),
        ('a', 'a', 0)
    ]
    for s in solutions:
        for hst, ndl, expected in tc:
            assert s.strStr(hst, ndl) == expected
