"""
Determine whether an integer is a palindrome. Do this without extra space.

Runtime: 284 ms  (Your runtime beats 83.63 % of python3 submissions.)
Status: Accepted  https://leetcode.com/submissions/detail/149562176/
"""

__author__ = 'Ivan Nikiforov'

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x) == str(x)[::-1]


        # Another solution;
        # Not accepted, but probably more correct if we need to work with negate nums
        # if all([isinstance(x, int),
        #        abs(x) < (1 << 31) - 1,
        #        int(str(abs(x))[::-1]) < (1 << 31) - 1
        # ]):
        #     return str(abs(x)) == str(abs(x))[::-1]
        # else:
        #     return False
