"""
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Example 1:
    Input: 6
    Output: true
    Explanation: 6 = 2 × 3

Example 2:
    Input: 8
    Output: true
    Explanation: 8 = 2 × 2 × 2

Example 3:
    Input: 14
    Output: false
    Explanation: 14 is not ugly since it includes another prime factor 7.

Note:
1 is typically treated as an ugly number.
Input is within the 32-bit signed integer range: [−231,  231 − 1].
"""

class Solution:
    def isUgly(self, num: int) -> bool:
        """
        Runtime: 40 ms, faster than 91.29% of Python3.
        Memory Usage: 13.2 MB, less than 51.59% of Python3.

        For a given number (2, 3, 5) is the factor of the number. When we make a division to the number,
        we eliminate a factor of the number. If all the factors (2, 3, 5) are eliminated and which
        remained is number 1, it is to say that the factors of the number is only (2, 3, 5).
        """
        for p in 2, 3, 5:
            while (num % p == 0) and (0 < num):
                num /= p
        return num == 1


if __name__ == "__main__":
    s = Solution()
    assert s.isUgly(1) == True
    assert s.isUgly(6) == True
    assert s.isUgly(8) == True
    assert s.isUgly(25) == True

    assert s.isUgly(14) == False
    assert s.isUgly(-2147483648) == False
    assert s.isUgly(-14) == False
    assert s.isUgly(0) == False
    assert s.isUgly(7) == False
    assert s.isUgly(214797179) == False
    assert s.isUgly(937351770) == False
