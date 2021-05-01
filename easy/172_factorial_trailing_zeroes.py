"""
Given an integer n, return the number of trailing zeroes in n!.

Follow up: Could you write a solution that works in logarithmic time complexity?

Example 1:
Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.

Example 2:
Input: n = 5
Output: 1
Explanation: 5! = 120, one trailing zero.

Example 3:
Input: n = 0
Output: 0

Constraints: 0 <= n <= 104
"""

import math


class Solution:
    """
    Compute the factorial, then convert num to string and count zeroes from the end.

    Runtime: 2168 ms, faster than 27.98% of Python3
    Memory Usage: 14.5 MB, less than 13.79% of Python3

    Time complexity: O(n**2)
    """

    def trailingZeroes(self, n: int) -> int:
        n_factorial = str(math.factorial(n))
        trailing_zeroes = 0

        for i in range(len(n_factorial) - 1, -1, -1):
            if n_factorial[i] != "0":
                break
            trailing_zeroes += 1
        return trailing_zeroes


class Solution2:
    """
    Compute the factorial, then consequently divide by ten to find number of trailing zeroes.

    Runtime: 9112 ms, faster than 5.05% of Python3
    Memory Usage: 14.2 MB, less than 50.89% of Python3

    Time complexity: O(n**2)
    """

    def trailingZeroes(self, n: int) -> int:
        n_factorial = 1
        for i in range(1, n + 1):  # the same as math.factorial(n), but LC says this one slows comp by ~2000ms
            n_factorial *= i

        trailing_zeroes = 0
        while n_factorial % 10 == 0:  # e.g. 120
            n_factorial //= 10  # e.g. 12
            trailing_zeroes += 1
        return trailing_zeroes


class Solution3:
    """
    As the problem states n cannot be greater than 10000 and since there are only 4 powers of 5 below that namely
    25, 125, 625 and 3125, then we can also do it in O(1) time like below.

    Runtime: 32 ms, faster than 73.57% of Python3
    Memory Usage: 14.3 MB, less than 50.89% of Python3

    Time complexity: O(1)
    """

    def trailingZeroes(self, n: int) -> int:
        trailing_zeroes = 0
        for i in range(1, 6):
            trailing_zeroes += n // (5 ** i)  # thus, calculate sum([n//5, n//25, n//125, n//625, n//3125])
        return trailing_zeroes


class Solution4:
    """
    One-line solution - the same idea as in Solution3

    Runtime: 24 ms, faster than 96.35% of Python3
    Memory Usage: 14.4 MB, less than 23.63% of Python3

    Time complexity: O(1)
    """

    def trailingZeroes(self, n: int) -> int:
        return sum(n // (5 ** i) for i in range(1, 6))  # one can use math.floor() instead //


if __name__ == '__main__':
    solutions = [Solution(), Solution2(), Solution3(), Solution4()]
    tc = (
        (3, 0),
        (5, 1),
        (0, 0),
    )
    for sol in solutions:
        for inp_n, exp_tr_zeroes in tc:
            assert sol.trailingZeroes(inp_n) == exp_tr_zeroes
