"""
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.
Return the quotient after dividing dividend by divisor.

Example 1:
Input: dividend = 10, divisor = 3
Output: 3

Example 2:
Input: dividend = 7, divisor = -3
Output: -2

Note:
* Both dividend and divisor will be 32-bit signed integers.
* The divisor will never be 0.
* Assume we are dealing with an environment which could only store integers within
the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem,
assume that your function returns 231 − 1 when the division result overflows.

Runtime: 60 ms (Your runtime beats 85.45 % of python3 submissions.)
Status: Accepted (https://leetcode.com/submissions/detail/150103050/)
"""

class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :return: int
        """
        int32_min = -(2**31)
        int32_max = (2**31 - 1)

        result = dividend // divisor if (
                (dividend < 0 and divisor < 0) or (dividend > 0 and divisor > 0)
        ) else -(abs(dividend) // abs(divisor))

        if result < int32_min:
            return int32_min
        elif result > int32_max:
            return int32_max
        else:
            return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.divide(-1, -1))   # expected: 1
    print(sol.divide(10, 3))    # expected: 3
    print(sol.divide(-2147483648, -1))  # expected: 2147483647
    print(sol.divide(-2147483648, 1))   # expected: -2147483648
