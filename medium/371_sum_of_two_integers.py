"""
Given two integers a and b,
return the sum of the two integers without using the operators + and -.

Example 1:
Input: a = 1, b = 2
Output: 3

Example 2:
Input: a = 2, b = 3
Output: 5

Constraints:

-1000 <= a, b <= 1000

"""


class Solution:
    """
    Built-in function

    Runtime: 28 ms, faster than 76.18% of Python3
    Memory Usage: 14.3 MB, less than 12.83% of Python3
    """

    def getSum(self, a: int, b: int) -> int:
        return sum((a, b))


class Solution2:
    """
    Bit Manipulation

    Runtime: 32 ms, faster than 44.21% of Python3
    Memory Usage: 14.2 MB, less than 46.58% of Python3

    Time / Space complexity: O(1)
    """

    def getSum(self, a: int, b: int) -> int:
        x, y = abs(a), abs(b)
        if x < y:  # ensure x >= y
            return self.getSum(b, a)
        sign = 1 if a > 0 else -1

        if a * b >= 0:
            # sum of two positive integers
            while y:
                # x = answer, y = carry
                x, y = x ^ y, (x & y) << 1
        else:
            # difference of two positive integers
            while y:
                # x = answer, y = borrow.
                x, y = x ^ y, ((~x) & y) << 1

        return x * sign


if __name__ == '__main__':
    tc = (
        (1, 2, 3),
        (2, 3, 5),
        (-6, -7, -13),
        (-6, 7, 1),
        (7, -6, 1),
        (0, 0, 0),
    )
    solutions = [Solution(), Solution2()]
    for sol in solutions:
        for inp_a, inp_b, exp_sum in tc:
            assert sol.getSum(inp_a, inp_b) == exp_sum
