"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

Note that division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a
result, and there will not be any division by zero operation.

Example 1:
    Input: tokens = ["2","1","+","3","*"]
    Output: 9
    Explanation: ((2 + 1) * 3) = 9

Constraints:
    1 <= tokens.length <= 104
    tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].

"""

import operator
from typing import List


class Solution:
    """
    Stack is the best structure for this kind of problems.

    Runtime: 56 ms, faster than 98.03% of Python3
    Memory Usage: 14.5 MB, less than 88.90% of Python3

    Time / Space complexity: O(n)
    """

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            # division truncating result toward 0 (floor division)
            "/": lambda dividend, divider: int(operator.truediv(dividend, divider)),
        }
        for token in tokens:
            if (token.isdigit() or
                    (token.startswith("-") and token[1:].isdigit())):
                stack.append(int(token))
            elif token in ops:
                b = stack.pop()
                a = stack.pop()
                result = ops[token](a, b)
                stack.append(result)
        return stack.pop()


if __name__ == '__main__':
    solutions = [Solution()]
    tc = (
        (["2", "1", "+", "3", "*"], 9),  # ((2 + 1) * 3) = 9
        (["4", "13", "5", "/", "+"], 6),  # (4 + (13 / 5)) = 6
        (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22),
    )
    for sol in solutions:
        for inp_tokens, exp_res in tc:
            assert sol.evalRPN(inp_tokens) == exp_res
