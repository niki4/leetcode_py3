"""
Given a string S of lowercase letters, a duplicate removal consists
of choosing two adjacent and equal letters, and removing them.

We repeatedly make duplicate removals on S until we no longer can.

Return the final string after all such duplicate removals have been made.
It is guaranteed the answer is unique.

Example 1:
Input: "abbaca"
Output: "ca"

Explanation:
For example, in "abbaca" we could remove "bb" since the letters are
adjacent and equal, and this is the only possible move.  The result
of this move is that the string is "aaca", of which only "aa" is possible,
so the final string is "ca".

Note:
1 <= S.length <= 20000
S consists only of English lowercase letters.
"""


class Solution:
    """
    This is working solution, but got "Time Limit Exceeded" error on Leetcode
    """

    def removeDuplicates(self, s: str) -> str:
        dup_flag = True
        while dup_flag:
            for i in range(1, len(s)):
                if s[i - 1] == s[i]:
                    s = s[:i - 1] + s[i + 1:]
                    break
            else:
                dup_flag = False
        return s


class Solution2:
    """
    This solution is also got "Time Limit Exceeded" error on Leetcode :-(
    """

    def removeDuplicates(self, s: str) -> str:
        if not s:
            return ''

        for i in range(1, len(s)):
            if s[i - 1] == s[i]:
                if i == len(s) - 1:
                    s = s[:i - 1]
                else:
                    s = s[:i - 1] + s[i + 1:]
                return self.removeDuplicates(s)
        return s


class Solution3:
    """
    Runtime: 76 ms, faster than 82.87% of Python3.
    Memory Usage: 13.7 MB, less than 100.00% of Python3.
    """

    def removeDuplicates(self, s: str) -> str:
        stack = []
        for char in s:
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)


class Solution4:
    """
    Track curr position and move it accordingly in case of duplicates removed from string.

    Runtime: 96 ms, faster than 31.34% of Python3
    Memory Usage: 14.5 MB, less than 89.60% of Python3
    """

    def removeDuplicates(self, s: str) -> str:
        i = 1
        while i < len(s):
            if s[i - 1] == s[i]:
                s = s[:i - 1] + s[i + 1:]
                i = 1 if (i - 2 < 1) else (i - 2)
            else:
                i += 1
        return s


if __name__ == "__main__":
    solutions = [Solution(), Solution2(), Solution3()]
    tc = (
        ("abbaca", "ca"),
        ("azxxzy", "ay"),
    )
    for sol in solutions:
        for inp_s, exp_s in tc:
            assert sol.removeDuplicates(inp_s) == exp_s
