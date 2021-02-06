"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character, but a character may map to itself.
"""


class Solution:
    """
    Algorithm: collect and compare "s to t" and "t to s" char maps while traversing string.

    Runtime: 44 ms, faster than 54.54% of Python3
    Memory Usage: 14.4 MB, less than 53.31% of Python3

    Time complexity: O(n)
    Space complexity: O(n)
    """

    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        st_map, ts_map = dict(), dict()
        for i in range(len(s)):
            if s[i] not in st_map:
                st_map[s[i]] = t[i]
            if t[i] not in ts_map:
                ts_map[t[i]] = s[i]
            if t[i] != st_map[s[i]] or s[i] != ts_map[t[i]]:
                return False
        return True


class Solution2:
    """
    Runtime: 36 ms, faster than 89.22% of Python3
    Memory Usage: 14.3 MB, less than 76.38% of Python3

    Time complexity: O(n)
    Space complexity: O(n)
    """

    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))


if __name__ == '__main__':
    solutions = [Solution(), Solution2()]
    tc = (
        ("egg", "add", True),
        ("foo", "bar", False),
        ("paper", "title", True),
        ("badc", "baba", False),
        ("bbbaaaba", "aaabbbba", False)
    )
    for sol in solutions:
        for inp_s, inp_t, exp in tc:
            res = sol.isIsomorphic(inp_s, inp_t)
            assert res is exp, f"{sol.__class__.__name__}: for s={inp_s} t={inp_t} expected {exp}, got {res}"
