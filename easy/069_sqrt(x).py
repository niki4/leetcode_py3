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


class Solution3:
    """
    Binary search

    Runtime: 40 ms, faster than 41.39% of Python3
    Memory Usage: 14.2 MB, less than 53.53% of Python3
    Time complexity: O(log n)
    Space complexity: O(1)

    Algorithm:
    * If x < 2, return x.
    * Set the left boundary to 2, and the right boundary to x / 2.
    * While left <= right:
        - Take num = (left + right) / 2 as a guess. Compute num * num and compare it with x:
            -- If num * num > x, move the right boundary right = pivot -1
            -- Else, if num * num < x, move the left boundary left = pivot + 1
            -- Otherwise num * num == x, the integer square root is here, let's return it
    * Return right
    """

    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        left, right = 2, x // 2  # For x≥2 the square root (a) is always: 0 < a < x/2
        while left <= right:
            mid = left + (right - left) // 2  # or (left + right) // 2
            mid_pow = mid * mid
            if mid_pow == x:
                return mid
            elif mid_pow > x:
                right = mid - 1
            else:
                left = mid + 1
        return right  # 'while' cycle stops when left > right, thus right is lower and we return it


if __name__ == '__main__':
    solutions = [Solution1(), Solution2(), Solution2()]
    tc = (
        (0, 0),
        (3, 1),
        (4, 2),
        (8, 2),
        (10, 3),
        (256, 16),
    )
    for s in solutions:
        for inp, exp in tc:
            assert s.mySqrt(inp) == exp
