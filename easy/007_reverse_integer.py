"""
Given a 32-bit signed integer, reverse digits of an integer.

Runtime: 56ms (Your runtime beats 97.98 % of python3 submissions on 2018-04-09)
Status: Accepted  https://leetcode.com/submissions/detail/149192344/
"""

__author__ = 'Ivan Nikiforov'

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        result = int(str(abs(x))[::-1])

        if (1 << 31) - 1 < result:  # max int on 32bit, 1 bit reserved for sign
            return 0

        return result if x >= 0 else -result
