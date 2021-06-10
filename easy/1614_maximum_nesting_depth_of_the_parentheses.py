"""
A string is a valid parentheses string (denoted VPS) if it meets one of the following:
    It is an empty string "", or a single character not equal to "(" or ")",
    It can be written as AB (A concatenated with B), where A and B are VPS's, or
    It can be written as (A), where A is a VPS.

We can similarly define the nesting depth depth(S) of any VPS S as follows:
    depth("") = 0
    depth(C) = 0, where C is a string with a single character not equal to "(" or ")".
    depth(A + B) = max(depth(A), depth(B)), where A and B are VPS's.
    depth("(" + A + ")") = 1 + depth(A), where A is a VPS.
For example, "", "()()", and "()(()())" are VPS's (with nesting depths 0, 1, and 2), and ")(" and "(()" are not VPS's.

Given a VPS represented as string s, return the nesting depth of s.

Example 1:
    Input: s = "(1+(2*3)+((8)/4))+1"
    Output: 3
    Explanation: Digit 8 is inside of 3 nested parentheses in the string.

Constraints:
    1 <= s.length <= 100
    s consists of digits 0-9 and characters '+', '-', '*', '/', '(', and ')'.
    It is guaranteed that parentheses expression s is a VPS.
"""


class Solution:
    """
    Algorithm idea: count open parentheses (as balance) and check if it's a new max depth, in case of closed parentheses
    simply decrease that balance counter. Since we guaranteed that parentheses expression s is a VPS we don't need to
    carry about invalid strings like ")((1+2)(".

    Runtime: 32 ms, faster than 59.58% of Python3
    Memory Usage: 14.3 MB, less than 40.67% of Python3

    Time complexity: O(n)
    Space complexity: O(1)
    """

    def maxDepth(self, s: str) -> int:
        curr_balance = 0
        max_depth = 0
        for char in s:
            if char == "(":
                curr_balance += 1
                max_depth = max(max_depth, curr_balance)
            elif char == ")":
                curr_balance -= 1
        return max_depth


if __name__ == '__main__':
    solutions = [Solution()]
    tc = (
        ("(1+(2*3)+((8)/4))+1", 3),
        ("(1)+((2))+(((3)))", 3),
        ("1+(2*3)/(2-1)", 1),
        ("1", 0),
        ("1+2/3", 0),
    )
    for sol in solutions:
        for inp_s, exp_depth in tc:
            assert sol.maxDepth(inp_s) == exp_depth
