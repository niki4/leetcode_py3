"""
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

If multiple answers are possible, return any of them.

It is guaranteed that the length of the answer string is less than 104 for all the given inputs.
"""


class Solution:
    """
    Runtime: 20 ms, faster than 99.13% of Python3
    Memory Usage: 14.3 MB, less than 65.77% of Python3
    """

    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator % denominator == 0:  # e.g, 4 % 2 == 0
            return str(numerator // denominator)

        sign = "-" if numerator * denominator < 0 else ""
        numerator, denominator = abs(numerator), abs(denominator)

        whole = sign + str(numerator // denominator)
        numerator %= denominator  # remainder from division, e.g. 7 % 2 = 5

        i, fractional = 0, ""
        memo = {numerator: i}
        while numerator % denominator:
            # shift number rank left by one (so, e.g. 0.123 -> 1.23) to take fractional part
            numerator *= 10
            i += 1
            remainder = numerator % denominator
            fractional += str(numerator // denominator)
            if remainder in memo:  # found repeating pattern
                fractional = fractional[:memo[remainder]] + "(" + fractional[memo[remainder]:] + ")"
                break
            memo[remainder] = i
            numerator = remainder
        return whole + "." + fractional


if __name__ == '__main__':
    solutions = [Solution()]
    tc = (
        (1, 2, "0.5"),
        (2, 1, "2"),
        (2, 3, "0.(6)"),  # because 2/3 = 0.6666666 where 6 are repeated pattern so 0.(6)
        (4, 333, "0.(012)"),
        (1, 5, "0.2"),
        (1, 6, "0.1(6)"),
        (1, 8, "0.125"),
        (1, 90, "0.0(1)"),
        (-50, 8, "-6.25"),
    )
    for sol in solutions:
        for in_numerator, in_denominator, exp_res in tc:
            res = sol.fractionToDecimal(in_numerator, in_denominator)
            assert res == exp_res, f"expected {exp_res}, got {res}"
