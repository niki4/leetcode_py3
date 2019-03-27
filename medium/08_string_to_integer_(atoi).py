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

Runtime: 44 ms, faster than 100.00% of Python3.
Memory Usage: 13.1 MB, less than 5.00% of Python3.
"""

import re

class Solution:
    def find_num(self, src):
        pattern = f'[+-]?\d+'
        m = re.search(pattern, src)
        if m:
            return m.group(0)

    def myAtoi(self, str: str) -> int:
        cleaned_s = str.strip()

        if not cleaned_s or not any(
        [cleaned_s[0].isdigit(), cleaned_s[0] in '+-']):
            return 0

        if len(cleaned_s) >= 2:
            if cleaned_s[0] in '+-' and not cleaned_s[1].isdigit():
                return 0

        num = self.find_num(str)
        if num:
            num = int(num)
        else:
            return 0

        int_max = (1 << 31) - 1
        int_min = (-1 << 31)

        if num > int_max:
            return int_max
        if num < int_min:
            return int_min

        return num
        

f __name__ == '__main__':
    s = Solution()
    assert s.myAtoi('42') == 42
    assert s.myAtoi('   -42') == -42
    assert s.myAtoi('4193 with words') == 4193
    assert s.myAtoi('words and 987') == 0, 'expected 0 as string starts with non-whitesp or non-num'
    assert s.myAtoi('-91283472332') == -2147483648, 'expected MIN_INT constant value as input less than it'
    assert s.myAtoi('+') == 0
    assert s.myAtoi('+-2') == 0
