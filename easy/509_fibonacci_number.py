"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence,
such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.

Given N, calculate F(N).

Example 1:

Input: 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
"""

__author__ = 'Ivan Nikiforov'


class Solution:

    def fib(self, N: 'int') -> 'int':
        """
        Runtime: 740 ms, faster than 28.75% of Python3.
        Memory Usage: 12.4 MB, less than 100.00% of Python3.
        """
        if N < 2:
            return N

        return self.fib(N - 1) + self.fib(N - 2)

    def fib2(self, N):
        """
        Runtime: 32 ms, faster than 100.00% of Python3.
        Memory Usage: 12.5 MB, less than 100.00% of Python3.
        """
        if N < 2:
            return N

        a, b = 0, 1
        for _ in range(1, N):
            a, b = b, a + b
        return b


if __name__ == '__main__':
    sol = Solution()
    assert sol.fib(0) == 0
    assert sol.fib(1) == 1
    assert sol.fib(2) == 1
    assert sol.fib(3) == 2
    assert sol.fib(4) == 3

    assert sol.fib2(0) == 0
    assert sol.fib2(1) == 1
    assert sol.fib2(2) == 1
    assert sol.fib2(3) == 2
    assert sol.fib2(4) == 3

