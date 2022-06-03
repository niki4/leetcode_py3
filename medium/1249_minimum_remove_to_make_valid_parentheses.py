"""
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting
parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:
    It is the empty string, contains only lowercase characters, or
    It can be written as AB (A concatenated with B), where A and B are valid strings, or
    It can be written as (A), where A is a valid string.

Example 1:
    Input: s = "lee(t(c)o)de)"
    Output: "lee(t(c)o)de"
    Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
"""


class Solution:
    """
    Runtime: 120 ms, faster than 64.85% of Python3
    Memory Usage: 16.3 MB, less than 32.80% of Python3

    Time/Space complexity: O(n)
    """

    def minRemoveToMakeValid(self, s: str) -> str:
        idxs_to_exclude = set()
        stack = list()
        for idx, ch in enumerate(s):
            if ch in "()":
                if ch == "(":
                    stack.append(idx)
                elif not stack:
                    idxs_to_exclude.add(idx)
                else:  # ")"
                    stack.pop()
        idxs_to_exclude |= set(stack)  # union
        return "".join(ch for (idx, ch) in enumerate(s) if idx not in idxs_to_exclude)


class Solution2:
    """
    This solution seems slower than the first one, but it's easily
    expandable to include other types of brackets, if it'll be required later.

    Time/Space complexity: O(n)
    """
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        rev_brackets = {
            ')': '(',
        }
        for idx, ch in enumerate(s):
            if ch in '(':
                stack.append((ch, idx))
            elif ch in ')':
                if not stack or rev_brackets[ch] != stack[-1][0]:
                    stack.append((ch, idx))
                else: # valid par
                    stack.pop()
        invalid_par_idxs = [item[1] for item in stack]

        return "".join(
            ch for idx, ch in enumerate(s) if idx not in invalid_par_idxs)


if __name__ == '__main__':
    solutions = [Solution(), Solution2()]
    tc = (
        ("lee(t(c)o)de)", ["lee(t(c)ode)", "lee(t(c)o)de"]),
        ("a)b(c)d", ["ab(c)d"]),
        ("))((", [""]),
        ("(a(b(c)d)", ["a(b(c)d)"]),
    )
    for sol in solutions:
        for inp_s, exp_results in tc:
            result = sol.minRemoveToMakeValid(inp_s)
            assert result in exp_results, f"{sol.__class__.__name__}: expected result in {exp_results}, got {result}"
