"""
A valid parentheses string is either empty (""), "(" + A + ")", or A + B,
where A and B are valid parentheses strings, and + represents string concatenation.
For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.

A valid parentheses string S is primitive if it is nonempty, and there does not exist
a way to split it into S = A+B, with A and B nonempty valid parentheses strings.

Given a valid parentheses string S, consider its primitive decomposition:
S = P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.

Return S after removing the outermost parentheses of every primitive string in
the primitive decomposition of S.

Example 1:
Input: "(()())(())"
Output: "()()()"
Explanation:
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".

Example 2:
Input: "()()"
Output: ""
Explanation:
The input string is "()()", with primitive decomposition "()" + "()".
After removing outer parentheses of each part, this is "" + "" = "".


Note:
S.length <= 10000
S[i] is "(" or ")"
S is a valid parentheses string
"""

class Solution:
    """
    Runtime: 40 ms, faster than 96.30% of Python3.
    Memory Usage: 13.2 MB, less than 65.19% of Python3.
    """
    def parse_groups(self, src: list) -> list:
        open_vs_closed = 0
        groups = []
        start = 0
        for idx, val in enumerate(src):
            if val == '(':
                open_vs_closed += 1
            elif val == ')':
                open_vs_closed -= 1

            if open_vs_closed == 0:
                group = src[start:idx+1]
                if group != '()':  # skip as this would be '' after removing outermost parentheses
                    groups.append(group)
                start = idx + 1
        return groups

    def removeOuterParentheses(self, S: str) -> str:
        valid_groups = self.parse_groups(S)

        for idx, group in enumerate(valid_groups):
            valid_groups[idx] = group[1:-1]
        return ''.join(valid_groups)


if __name__ == "__main__":
    s = Solution()
    assert s.removeOuterParentheses("(()())(())") == "()()()"
    assert s.removeOuterParentheses("(()())(())(()(()))") == "()()()()(())"
    assert s.removeOuterParentheses("()()") == ""
