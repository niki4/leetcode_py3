"""
Given an integer n (in base 10) and a base k, return sum of the digits of n after converting n from base 10 to base k.

After converting, each digit should be interpreted as a base 10 number, and the sum should be returned in base 10.

Example 1:
Input: n = 34, k = 6
Output: 9
Explanation: 34 (base 10) expressed in base 6 is 54. 5 + 4 = 9.

Example 2:
Input: n = 10, k = 10
Output: 1
Explanation: n is already in base 10. 1 + 0 = 1.

Constraints:
    1 <= n <= 100
    2 <= k <= 10
"""


class Solution:
    """
    Each digit (decimal place in base10) in the new base is remainder from division (%) of current number on that base.
    The next digit would be a result of whole-number division (//) of current number on that base.

    E.g., 19 (base 10) = 10011 (base 2)
            19 % 2 = 1
            9 % 2 = 1
            4 % 2 = 0
            2 % 2 = 0
            1 % 2 = 1

    Runtime: 32 ms, faster than 62.42% of Python3
    Memory Usage: 14.3 MB, less than 46.01% of Python3

    Time complexity: O(log k), where k is the target base
    Space complexity: O(1)
    """

    def sumBase(self, n: int, k: int) -> int:
        sum_ = 0
        while n != 0:
            sum_ += n % k
            n //= k
        return sum_


if __name__ == '__main__':
    solutions = [Solution()]
    tc = (
        (19, 2, 3),  # 19 (base 10) = 10011 (base 2) = 1 + 0 + 0 + 1 + 1 = 3
        (19, 6, 4),  # 19 (base 10) = 31 (base 6) -> 3+1 = 4
    )
    for sol in solutions:
        for inp_n, inp_k, exp_sum in tc:
            assert sol.sumBase(inp_n, inp_k) == exp_sum
