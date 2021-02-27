"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""


class Solution:
    """
    Runtime: 132 ms, faster than 5.00% of Python3
    Memory Usage: 13.6 MB, less than 12.73% of Python3.

    Bruteforce Algorithm:
        To generate all sequences, we use a recursion. All sequences of length n is just '(' plus
        all sequences of length n-1, and then ')' plus all sequences of length n-1.

        To check whether a sequence is valid, we keep track of balance, the net number of opening
        brackets minus closing brackets. If it falls below zero at any time, or doesn't end in zero,
        the sequence is invalid - otherwise it is valid.
    """

    def generateParenthesis(self, n: int) -> list:
        def generate(A=[]):
            if len(A) == 2 * n:
                if valid(A):
                    ans.append(''.join(A))
            else:
                A.append('(')
                generate(A)
                A.pop()
                A.append(')')
                generate(A)
                A.pop()

        def valid(A):
            bal = 0
            for c in A:
                if c == '(':
                    bal += 1
                else:
                    bal -= 1

                if bal < 0:
                    return False
            return bal == 0

        ans = []
        generate()
        return ans


class Solution2:
    """
    Runtime: 44 ms, faster than 57.80% of Python3.
    Memory Usage: 13.3 MB, less than 61.01% of Python3.

    Backtracking Algorithm:
        Instead of adding '(' or ')' every time as in Approach 1, let's only add them when we know it
        will remain a valid sequence. We can do this by keeping track of the number of opening and
        closing brackets we have placed so far.

        We can start an opening bracket if we still have one (of n) left to place. And we can start a
        closing bracket if it would not exceed the number of opening brackets.
    """

    def generateParenthesis(self, n: int) -> list:
        ans = []

        def backtrack(s='', left=0, right=0):
            if len(s) == 2 * n:  # num of opening brackets + num of closing brackets
                ans.append(s)
                return
            if left < n:
                backtrack(s + '(', left + 1, right)
            if right < left:
                backtrack(s + ')', left, right + 1)

        backtrack()
        return ans


class Solution3:
    """
    Runtime: 44 ms, faster than 57.80% of Python3.
    Memory Usage: 13.3 MB, less than 69.98% of Python3.

    Closure Number algorithm:
        For each closure number c, we know the starting and ending brackets must be at index 0 and 2*c + 1.
        Then, the 2*c elements between must be a valid sequence, plus the rest of the elements must be a
        valid sequence.
    """

    def generateParenthesis(self, n: int) -> list:
        if n == 0:
            return ['']
        ans = []
        for c in range(n):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(n - 1 - c):
                    ans.append(f'({left}){right}')
        return ans


if __name__ == "__main__":
    solutions = [Solution(), Solution2(), Solution3()]
    tc = (
        (3, ["((()))", "(()())", "(())()", "()(())", "()()()"]),
        (1, ["()"]),
    )
    for sol in solutions:
        for inp_n, exp in tc:
            assert sorted(sol.generateParenthesis(inp_n)) == sorted(exp)
