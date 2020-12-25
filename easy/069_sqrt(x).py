"""
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated
 and only the integer part of the result is returned.

Example 2:
Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since
             the decimal part is truncated, 2 is returned.
"""

import math


class Solution1:
    """
    Standard library approach.

    Runtime: 68 ms (Your runtime beats 62.20 % of python3 submissions.)
    """

    def mySqrt(self, x: int) -> int:
        return int(math.sqrt(x))


class Solution2:
    """
    Universal way to calculate the square root is to take power of 0.5

    Runtime: 56 ms (Your runtime beats 98.93 % of python3 submissions.)
    """

    def mySqrt(self, x: int) -> int:
        return int(x ** 0.5)  # or int(pow(x, 0.5))


if __name__ == '__main__':
    solutions = [Solution1(), Solution2()]
    tc = (
        (4, 2),
        (8, 2),
        (256, 16),
    )
    for s in solutions:
        for inp, exp in tc:
            assert s.mySqrt(inp) == exp
