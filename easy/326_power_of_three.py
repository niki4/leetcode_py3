"""
Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.
"""


class Solution:
    """
    Runtime: 84 ms, faster than 44.74% of Python3.
    Memory Usage: 14.1 MB, less than 76.28% of Python3

    Algorithm idea: while we can divide without remainder (n%3==0) - divide of num of its power until we get 1 (
    so 9 is 3*3, thus we doing 9/3 = 3, then 3/3 = 1) or not (45/3=15, 15/3=5, 5%3=2 -> 5 != 1 thus return False for 45)

    Time complexity : O(log b(n)). In our case that is O(log3 n). The number of divisions is given by that logarithm.
    Space complexity : O(1). We are not using any additional memory.

    """

    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        while n % 3 == 0:
            n /= 3  # if power of 3, we should get 3 / 3 == 1 on the last iteration
        return n == 1


if __name__ == '__main__':
    tc = (
        (27, True),
        (0, False),
        (9, True),
        (45, False),
        (1, True),
    )
    solutions = [Solution()]
    for s in solutions:
        for inp, exp in tc:
            assert s.isPowerOfThree(inp) == exp
