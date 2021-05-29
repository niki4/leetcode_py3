"""
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's
in the binary representation of i.

Example 1:
    Input: n = 2
    Output: [0,1,1]
    Explanation:
    0 --> 0
    1 --> 1
    2 --> 10

Example 2:
    Input: n = 5
    Output: [0,1,1,2,1,2]
    Explanation:
    0 --> 0
    1 --> 1
    2 --> 10
    3 --> 11
    4 --> 100
    5 --> 101

Constraints:
    0 <= n <= 105
Follow up:
    * It is very easy to come up with a solution with a runtime of O(n log n).
      Can you do it in linear time O(n) and possibly in a single pass?
    * Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?
"""
from typing import List


class Solution:
    """
    Maybe not the fastest solution, but it's pretty concise.

    Runtime: 80 ms, faster than 77.70% of Python3
    Memory Usage: 20.7 MB, less than 90.47% of Python3

    Time complexity: O(n*m) where n is the count of numbers in range(0, n+1) and m is the number of symbols in binary
    representation of the number.
    Space complexity: O(n)
    """

    def countBits(self, n: int) -> List[int]:
        return [bin(n)[2:].count("1") for n in range(n + 1)]


class Solution2:
    """
    For a number n, the number of 1's in its binary representation will be determined as follows:
        If n is odd, the last digit is a '1', so a right shift (which is the same as n//2) will eliminate one 1.
        If n is even, the last digit is a '0', so a right shift (i.e. n//2) will have the same number of 1's

    Runtime: 76 ms, faster than 89.59% of Python3
    Memory Usage: 20.9 MB, less than 39.65% of Python3

    Time/Space complexity: O(n)
    """

    def countBits(self, n: int) -> List[int]:
        out = [0]  # base case for n == 0
        for i in range(1, n + 1):
            out.append(out[i // 2] + (i % 2))
        return out


class Solution3:
    """
    The same approach as in Solution2, but using binary operators.

    Runtime: 80 ms, faster than 77.70% of Python3
    Memory Usage: 20.8 MB, less than 90.47% of Python3

    Time/Space complexity: O(n)
    """

    def countBits(self, n: int) -> List[int]:
        out = [0]  # base case for n == 0
        for i in range(1, n + 1):
            out.append(out[i >> 1] + (i & 1))
        return out


if __name__ == '__main__':
    solutions = [Solution(), Solution2(), Solution3()]
    tc = (
        (2, [0, 1, 1]),
        (5, [0, 1, 1, 2, 1, 2]),
    )
    for sol in solutions:
        for inp_num, exp_result in tc:
            result = sol.countBits(inp_num)
            assert result == exp_result, f"{sol.__class__.__name__}: actual {result} != {exp_result} expected"
