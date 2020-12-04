"""
Given a string, you need to reverse the order of characters
in each word within a sentence while still preserving whitespace
and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and
there will not be any extra space in the string.
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        """
        Runtime: 32 ms, faster than 99.26% of Python3.
        Memory Usage: 13.5 MB, less than 42.63% of Python3.

        Python is beautiful for this kind of problems :)
        """
        return ' '.join(word[::-1] for word in s.split())
    #   return ' '.join(reversed(inp[::-1].split()))  # another way


if __name__ == "__main__":
    s = Solution()
    src = "Let's take LeetCode contest"
    assert s.reverseWords(src) == "s'teL ekat edoCteeL tsetnoc"
