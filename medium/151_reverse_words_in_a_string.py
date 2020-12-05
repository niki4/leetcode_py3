"""
Given an input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words.
The returned string should only have a single space separating the words. Do not include any extra spaces.
"""


class Solution:
    """
    Python built-in methods

    Runtime: 24 ms, faster than 95.15% of Python3
    Memory Usage: 14.5 MB, less than 13.26% of Python3

    Time complexity: O(n)
    Space complexity: O(n) for new string created after join
    """

    def reverseWords(self, s: str) -> str:
        return " ".join(word for word in reversed(s.split(" ")) if word)


class Solution2:
    """
    Solution without built-ins. Good to know for the interview.

    Runtime: 48 ms, faster than 9.23% of Python3
    Memory Usage: 14.5 MB, less than 13.74% of Python3
    """

    def reverseWords(self, s: str) -> str:
        words = []
        l_ptr, r_ptr = 0, 0

        # split words using 2-pointer approach
        while l_ptr < len(s) and r_ptr < len(s):
            while l_ptr < len(s) and s[l_ptr] == " ":
                l_ptr += 1
            while r_ptr < len(s) and s[r_ptr] != " ":
                r_ptr += 1
            word = s[l_ptr:r_ptr]
            if word:
                words.append(word)
            l_ptr = r_ptr + 1
            r_ptr = l_ptr

        # iterate words in reverse order and concatenate result string
        reversed_s = ""
        for i in range(len(words) - 1, -1, -1):
            if not reversed_s:
                reversed_s = words[i]
            else:
                reversed_s += " " + words[i]
        return reversed_s


if __name__ == '__main__':
    solutions = [Solution(), Solution2()]
    tc = [
        ("the sky is blue", "blue is sky the"),
        ("  hello world  ", "world hello"),
        ("a good   example", "example good a"),
        ("  Bob    Loves  Alice   ", "Alice Loves Bob"),
        ("Alice does not even like bob", "bob like even not does Alice"),
    ]
    for sol in solutions:
        for inp, exp in tc:
            assert sol.reverseWords(inp) == exp
