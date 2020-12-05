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


class Solution2:
    """
    2-pointer approach to split string by words.

    Runtime: 76 ms, faster than 13.52% of Python3
    Memory Usage: 15.1 MB, less than 11.76% of Python3
    """

    def reverseWords(self, s: str) -> str:
        words = []
        l_ptr, p_ptr = 0, 0

        # split words
        while l_ptr < len(s) and p_ptr < len(s):
            while p_ptr < len(s) and s[p_ptr] != " ":
                p_ptr += 1

            words.append(s[l_ptr:p_ptr])
            if p_ptr >= len(s) - 1:
                break
            p_ptr += 1
            l_ptr = p_ptr

        # reverse words and concatenate result string
        reversed_s = ""
        for w in words:
            if not reversed_s:
                reversed_s = "".join(reversed(w))
            else:
                reversed_s += " " + "".join(reversed(w))
        return reversed_s


if __name__ == "__main__":
    solutions = [Solution(), Solution2()]
    src = "Let's take LeetCode contest"
    for s in solutions:
        assert s.reverseWords(src) == "s'teL ekat edoCteeL tsetnoc"
