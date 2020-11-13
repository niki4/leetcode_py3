"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list,
and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Runtime: 40 ms  (Your runtime beats 95.20 % of python3 submissions.)
Status: Accepted  (https://leetcode.com/submissions/detail/150407185/)
"""
from typing import List


class Solution:
    """
    Now LC requires handle leading zero case, so for input [0,0] return [0,1].
    This breaks this solution, so I left it just for info.
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
        n = len(digits)

        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1  # increase the rightmost non-nine digit
                return digits

        # case all digits are nines
        return [1] + digits


if __name__ == '__main__':
    sol = Solution()
    print(sol.plusOne([1, 2, 3]))  # expected: [1, 2, 4]
    print(sol.plusOne([9]))  # expected: [1, 0]
    print(sol.plusOne([9, 9]))  # expected: [1, 0, 0]
    print(sol.plusOne([0, 0]))  # [1], however LC now need [0,1]
