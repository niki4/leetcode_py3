"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by the sum
of the squares of its digits, and repeat the process until the number
equals 1 (where it will stay), or it loops endlessly in a cycle which
does not include 1. Those numbers for which this process ends in 1 are
happy numbers.

Example:

Input: 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""

class Solution:
    """
    Runtime: 32 ms, faster than 99.59% of Python3.
    Memory Usage: 13.2 MB, less than 54.55% of Python3.

    Algorithm sees a number it has seen before, then it follows that
    it will go on the same path and thus see it once again, creating
    an infinite loop. So a valid solution requires that all numbers
    seen on the way to reducing n to 1 be unique.
    """
    def isHappy(self, n: int) -> bool:
        memo = set()
        while n not in memo:
            memo.add(n)
            n = sum(int(x)**2 for x in str(n))
        return 1 in memo


if __name__ == "__main__":
    s = Solution()
    assert s.isHappy(19) == True
    assert s.isHappy(7) == True  # 7**2 = 49 -> 4**2 + 9**2 = 16 + 81 = 97 -> ...
    assert s.isHappy(1111111) == True  # 1**2 + ... + 1**2 = 7
    assert s.isHappy(0) == False
