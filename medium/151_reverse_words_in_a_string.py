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


if __name__ == '__main__':
    solutions = [Solution()]
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
