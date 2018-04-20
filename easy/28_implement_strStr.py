"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

Runtime: 36 ms (Your runtime beats 99.32 % of python3 submissions)
Status: Accepted (https://leetcode.com/submissions/detail/150246110/)
"""

class Solution:
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
    sol = Solution()
    print(sol.strStr('hello', 'll'))  # expected: 2
    print(sol.strStr('aaaaa', 'bba'))  # expected: -1
    print(sol.strStr(haystack='Test', needle=''))  # expected: 0


#  Another 1-row solution for this is simply 'return haystack.find(needle)'
