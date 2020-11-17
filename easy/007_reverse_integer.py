"""
Given a 32-bit signed integer, reverse digits of an integer.

Note:
    Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range:
    [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""

__author__ = 'Ivan Nikiforov'


class Solution:
    """
    Runtime: 56ms (Your runtime beats 97.98 % of python3 submissions on 2018-04-09)
    Status: Accepted  https://leetcode.com/submissions/detail/149192344/
    """

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        result = int(str(abs(x))[::-1])

        if (1 << 31) - 1 < result:  # max int on 32bit, 1 bit reserved for sign
            return 0

        return result if x >= 0 else -result


class Solution2:
    """
    Runtime: 28 ms, faster than 83.57% of Python3
    Memory Usage: 14.1 MB, less than 68.69% of Python3
    """

    def reverse(self, x):
        sign = 1
        if x < 0:
            sign = -1
            x *= -1

        res = 0
        while x != 0:
            digit = x % 10
            res = res * 10 + digit
            x = x // 10
        res *= sign

        max_border = pow(2, 31) - 1
        min_border = -pow(2, 31)

        if res > max_border or res < min_border:
            return 0
        return res if x >= 0 else -res


if __name__ == '__main__':
    solutions = [Solution(), Solution2()]
    tc = [
        (123, 321),
        (-123, -321),
        (120, 21),  # 021->21
        (0, 0),
    ]
    for s in solutions:
        for inp, exp in tc:
            assert s.reverse(inp) == exp, f'want {exp}, got {s.reverse(inp)}'
