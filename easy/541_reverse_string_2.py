"""
Given a string and an integer k, you need to reverse the first k
characters for every 2k characters counting from the start of the string.

If there are less than k characters left, reverse all of them.
If there are less than 2k but greater than or equal to k characters,
then reverse the first k characters and left the other as original.

Example:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"

Restrictions:
1.  The string consists of lower English letters only.
2.  Length of the given string and k will in the range [1, 10000]
"""

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        """
        Runtime: 40 ms, faster than 65.28% of Python3.
        Memory Usage: 13.2 MB, less than 71.87% of Python3.

        Time Complexity: O(N), where N is the size of s.
        We build a helper array, plus reverse about half the characters in s.
        """

        chars = list(s)
        for i in range(0, len(chars), 2*k):
            chars[i:i+k] = reversed(chars[i:i+k])

        return ''.join(chars)


if __name__ == "__main__":
    s = Solution()
    assert s.reverseStr("abcdefg", 2) == "bacdfeg"
