import math


class Solution:

    # Own naive implementation.
    # Runtime: 228 ms, faster than 5.36% of Python3.
    # Memory Usage: 13.2 MB, less than 5.53% of Python3.
    def myPow(self, x: float, n: int) -> float:
        # special cases
        if x == 1 or n == 0:
            return 1.0
        if x == 0 and n != 0:
            return 0.0
        if x == -1:
            if n % 2 == 0:
                return 1.0
            else:
                return -1.0

        # signed int32 overflow
        if n >= (1 << 31) - 1 or n <= (-1 << 31):
            return 0.0

        res = x if (n > 0) else (1 / x)  # init value

        for _ in range(1, abs(n)):
            if n > 0:
                res *= x
            else:
                res /= x

        return res

    # Thanks to standard library 'math' module.
    # Runtime: 56 ms, faster than 20.58% of Python3.
    # Memory Usage: 13.2 MB, less than 5.53% of Python3.
    def myPow2(self, x: float, n: int) -> float:
        return math.pow(x, n)

    # This method is based on the fact that n^6 = n^4 * n^2
    # Runtime: 44 ms, faster than 40.31% of Python3.
    # Memory Usage: 13.1 MB, less than 5.53% of Python3.
    def myPow3(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n

        res = 1
        while n:
            if n & 1:
                res *= x
            x *= x
            n >>= 1
        return res


if __name__ == '__main__':
    sol = Solution()
    assert math.isclose(sol.myPow(2.00000, 10), math.pow(2.00000, 10)), "expected 1024.00000"
    assert math.isclose(sol.myPow(2.10000, 3), math.pow(2.10000, 3)), "expected 9.26100"
    assert math.isclose(sol.myPow(2.00000, -2), math.pow(2.00000, -2)), "expected 0.25000"
    assert math.isclose(sol.myPow(1.00000, 2147483647), math.pow(1.00000, 2147483647)), "expected 1.0"
    assert math.isclose(sol.myPow(2.00000, -2147483648), math.pow(2.00000, -2147483648)), "expected 0.0"

    assert math.isclose(sol.myPow3(2.00000, 10), math.pow(2.00000, 10)), "expected 1024.00000"
    assert math.isclose(sol.myPow3(2.10000, 3), math.pow(2.10000, 3)), "expected 9.26100"
    assert math.isclose(sol.myPow3(2.00000, -2), math.pow(2.00000, -2)), "expected 0.25000"
    assert math.isclose(sol.myPow3(1.00000, 2147483647), math.pow(1.00000, 2147483647)), "expected 1.0"
    assert math.isclose(sol.myPow3(2.00000, -2147483648), math.pow(2.00000, -2147483648)), "expected 0.0"
