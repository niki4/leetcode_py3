"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list,
and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:
    Input: [1,2,3]
    Output: [1,2,4]
    Explanation: The array represents the integer 123.
"""
from typing import List


class Solution:
    """
    Now LC requires handle leading zero case, so for input [0,0] return [0,1].
    This breaks this solution, so I left it just for info.

    Runtime: 40 ms  (Your runtime beats 95.20 % of python3 submissions.)
    """

    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        int_num = int(''.join(str(x) for x in digits)) + 1
        return [int(x) for x in str(int_num)]


class Solution2:
    """
    Runtime: 32 ms, faster than 62.19% of Python3
    Memory Usage: 14 MB, less than 78.76% of Python3

    This solution correctly handles leading zero case.
    """

    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[:]  # to avoid change input

        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1  # increase the rightmost non-nine digit
                return digits

        # case all digits are nines
        return [1] + digits


class Solution3:
    """
    Algorithm: keep the carry number and apply it to the current pos num.
    This approach may make more sense if we'd increase by other num than 1.

    Runtime: 36 ms, faster than 23.28% of Python3
    Memory Usage: 14.1 MB, less than 90.60% of Python3
    """

    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        digits = digits[:]

        for i in range(len(digits) - 1, -1, -1):
            if i == len(digits) - 1:
                digits[i] += 1
            digits[i] += carry
            carry = digits[i] // 10  # e.g., 10 // 10 == 1
            digits[i] %= 10  # e.g, 10 % 10 == 0

        return [carry] + digits if carry else digits


if __name__ == '__main__':
    solutions = [Solution2(), Solution3()]
    tc = (
        ([1, 2, 3], [1, 2, 4]),
        ([4, 3, 2, 1], [4, 3, 2, 2]),
        ([9, 9], [1, 0, 0]),
        ([0], [1]),
        ([0, 0], [0, 1])
    )
    for sol in solutions:
        for inp_digits, exp_digits in tc:
            result = sol.plusOne(inp_digits)
            assert result == exp_digits, f"{sol.__class__.__name__}: expected {exp_digits}, got {result}"
