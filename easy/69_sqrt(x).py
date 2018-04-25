"""
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated
 and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2

Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since
             the decimal part is truncated, 2 is returned.
"""

import math

# Runtime: 68 ms (Your runtime beats 62.20 % of python3 submissions.)
# Status: Accepted (https://leetcode.com/submissions/detail/151563925/)
class Solution1:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        return int(math.sqrt(x))


# Runtime: 56 ms (Your runtime beats 98.93 % of python3 submissions.)
# Status: Accepted (https://leetcode.com/submissions/detail/151565040/)
class Solution2:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        return int(x ** 0.5)
