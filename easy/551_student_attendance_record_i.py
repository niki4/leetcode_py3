"""
You are given a string representing an attendance record for a student.
The record only contains the following three characters:
    'A' : Absent.
    'L' : Late.
    'P' : Present.
A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two
continuous 'L' (late).

You need to return whether the student could be rewarded according to his attendance record.

Example 1:
Input: ""
Output:
Example 2:
Input: ""
Output:
"""


class Solution:
    """
    Two-pointer approach

    Runtime: 44 ms, faster than 11.24% of Python3
    Memory Usage: 14.3 MB, less than 13.26% of Python3

    Time complexity: O(n)
    Space complexity: O(1)
    """

    def checkRecord(self, s: str) -> bool:
        a_seq = 0
        ll_seq = 0
        i = 0
        while i < len(s):
            if s[i] == "A":
                a_seq += 1
            elif s[i] == "L":
                j = i + 1
                while j < len(s) and s[j] == s[i]:
                    j += 1
                ll_seq = max(ll_seq, j - i)
            i += 1
        return a_seq <= 1 and ll_seq <= 2


class Solution2:
    """
    Maybe most pythonic way

    Runtime: 40 ms, faster than 15.12% of Python3
    Memory Usage: 14.3 MB, less than 13.26% of Python3

    Time complexity: O(n)   2-pass
    Space complexity: O(1)
    """

    def checkRecord(self, s: str) -> bool:
        return s.count("A") <= 1 and "LLL" not in s


if __name__ == '__main__':
    solutions = [Solution(), Solution2()]
    tc = (
        ("PPALLP", True),
        ("PPALLL", False),
        ("ALLAPPL", False),
    )
    for sol in solutions:
        for inp, exp in tc:
            assert sol.checkRecord(inp) is exp
