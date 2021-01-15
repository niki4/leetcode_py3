"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
"""


class Solution:
    """
    Runtime: 36 ms, faster than 83.46% of Python3.
    Memory Usage: 13.2 MB, less than 5.22% of Python3.
    """

    def isValid(self, s: str) -> bool:
        stack = []
        balanced = True
        idx = 0
        reverse_brackets = {'{': '}', '[': ']', '(': ')'}

        while idx < len(s) and balanced:
            symbol = s[idx]
            if symbol in '([{':
                stack.append(symbol)
            else:
                if len(stack) == 0:
                    balanced = False
                elif symbol == reverse_brackets[stack[-1]]:
                    stack.pop()
                else:
                    balanced = False
            idx += 1

        if balanced and len(stack) == 0:
            return True
        else:
            return False


class Solution2:
    """
    More clear version of first solution

    Runtime: 32 ms, faster than 62.13% of Python3
    Memory Usage: 14.3 MB, less than 63.01% of Python3
    """

    def isValid(self, s: str) -> bool:
        stack = list()
        opposite = {
            '}': '{',
            ']': '[',
            ')': '(',
        }

        for ch in s:
            if ch in "{([":
                stack.append(ch)
            elif ch in "})]":
                if not stack or stack[-1] != opposite[ch]:
                    return False
                stack.pop()
        return len(stack) == 0


if __name__ == '__main__':
    solutions = [Solution(), Solution2()]
    tc = (
        ('', True),
        ('()', True),
        ('()[]{}', True),
        ('{[]}', True),
        ('(]', False),
        ('([)]', False),
        ('(])', False),
    )
    for s in solutions:
        for inp, exp in tc:
            assert s.isValid(inp) == exp
