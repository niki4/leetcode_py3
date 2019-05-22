"""
Given a non-negative integer num, repeatedly add all its digits
until the result has only one digit.

Example:

Input: 38
Output: 2
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2.
             Since 2 has only one digit, return it.
Follow up:
Could you do it without any loop/recursion in O(1) runtime?
"""

class Solution:
    def addDigits(self, num: int) -> int:
        """
        Runtime: 40 ms, faster than 89.53% of Python3.
        Memory Usage: 13.2 MB, less than 66.58% of Python3.

        Runtime complexity: O(n)
        """
        digits = str(num)
        while len(digits) > 1:
            digits = str(sum([int(n) for n in digits]))
        return int(digits)

    def addDigits2(self, num: int) -> int:
        """
        Runtime: 32 ms, faster than 98.39% of Python3
        Memory Usage: 13.2 MB, less than 57.90% of Python3.

        Runtime complexity: O(1)
        """
        if not num:
            return 0
        return num % 9 or 9


if __name__ == "__main__":
    sol = Solution()
    assert sol.addDigits(38) == 2
    assert sol.addDigits(0) == 0
    assert sol.addDigits2(38) == 2
    assert sol.addDigits2(0) == 0
