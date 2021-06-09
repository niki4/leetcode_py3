"""
Given an integer number n, return the difference between the product of its digits and the sum of its digits.

Example 1:
    Input: n = 234
    Output: 15
Explanation:
    Product of digits = 2 * 3 * 4 = 24
    Sum of digits = 2 + 3 + 4 = 9
    Result = 24 - 9 = 15

Example 2:
    Input: n = 4421
    Output: 21
Explanation:
    Product of digits = 4 * 4 * 2 * 1 = 32
    Sum of digits = 4 + 4 + 2 + 1 = 11
    Result = 32 - 11 = 21

Constraints:
    1 <= n <= 10^5
"""

from functools import reduce


class Solution:
    """
    Runtime: 52 ms, faster than 5.52% of Python3
    Memory Usage: 14.4 MB, less than 9.83% of Python3
    """

    def subtractProductAndSum(self, n: int) -> int:
        digits = [int(digit) for digit in str(n)]
        product = reduce(lambda a, b: a * b, digits)
        return product - sum(digits)


class Solution2:
    """
    Runtime: 48 ms, faster than 7.21% of Python3
    Memory Usage: 14.3 MB, less than 9.83% of Python3
    """

    def subtractProductAndSum(self, n: int) -> int:
        sum_ = 0
        product = 1
        for digit in str(n):
            sum_ += int(digit)
            product *= int(digit)
        return product - sum_


class Solution3:
    """
    Using modulo to operate with least significant digit of a number at each iteration, then reducing problem on it.

    Runtime: 36 ms, faster than 14.42% of Python3
    Memory Usage: 14.1 MB, less than 69.64% of Python3
    """

    def subtractProductAndSum(self, n: int) -> int:
        sum_ = 0
        product = 1
        while n:
            # e.g., for 234 last_digit will == 4 and n for next iteration will become 23
            last_digit = n % 10
            sum_ += last_digit
            product *= last_digit
            n //= 10
        return product - sum_


if __name__ == '__main__':
    solutions = [Solution(), Solution2(), Solution3()]
    tc = (
        (234, 15),
        (4421, 21),
        (1, 0),
        (100000, -1),
    )
    for sol in solutions:
        for inp_n, exp_result in tc:
            assert sol.subtractProductAndSum(inp_n) == exp_result
