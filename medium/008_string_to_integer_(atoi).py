"""
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until 
the first non-whitespace character is found. Then, starting from this character, 
takes an optional initial plus or minus sign followed by as many numerical digits 
as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral 
number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral 
number, or if no such sequence exists because either str is empty or it contains 
only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.
"""

import re


class Solution:
    """
    Runtime: 32 ms, faster than 76.02% of Python3
    Memory Usage: 14.1 MB, less than 35.39% of Python3
    """

    def find_num(self, src):
        pattern = r'[+-]?\d+'
        m = re.search(pattern, src)
        return m.group(0) if m else 0

    def myAtoi(self, s: str) -> int:
        s = s.strip()  # remove leading & trailing whitespaces

        if not s or not any([s[0].isdigit(), s[0] in '+-']):
            return 0

        if len(s) >= 2 and (s[0] in '+-' and not s[1].isdigit()):
            return 0

        num = int(self.find_num(s))

        int_max = (1 << 31) - 1
        int_min = -(1 << 31)

        if num > int_max:
            return int_max
        if num < int_min:
            return int_min
        return num


if __name__ == '__main__':
    solutions = [Solution()]
    tc = [
        ("42", 42, ""),
        ("   -42", -42, ""),
        ("4193 with words", 4193, ""),
        ("words and 987", 0, "expected 0 as string starts with non-whitesp or non-num"),
        ("-91283472332", -2147483648, "expected MIN_INT constant value as input less than it"),
        ("+", 0, ""),
        ("+-2", 0, ""),
    ]
    for sol in solutions:
        for inp_s, exp, comment in tc:
            res = sol.myAtoi(inp_s)
            assert res == exp, f"{sol.__class__.__name__}: result `{res}` ({type(res)}) != `{exp}` ({type(exp)})" \
                               f"\n{comment}"
