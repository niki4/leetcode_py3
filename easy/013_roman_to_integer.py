"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together.
12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
"""

rom2int = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}


class Solution:
    """
    Left-to-Right pass approach.

    Runtime: 48 ms, faster than 64.51% of Python3
    Memory Usage: 14.5 MB, less than 26.08% of Python3
    Time complexity: O(1) because there's known max num for roman num rules MMMCMXCIX which in our notation is 3,999.
    Space complexity: O(n) as we need additional array for conversed ints
    """

    def romanToInt(self, s: str):
        """
        :type s: str
        :rtype: int
        """
        nums = [rom2int[i] for i in s]
        result = 0
        i = 0

        while i < len(s):
            s1 = nums[i]
            s2 = nums[i + 1] if i <= len(s) - 2 else 0

            if s1 < s2:  # e.g, IV where s1 is "I" and s2 is "V", so we add (5-1)=4
                result += (s2 - s1)
                i += 2
            else:
                result += s1
                i += 1

        return result


class Solution2:
    """
     Right-to-Left Pass

     Runtime: 40 ms, faster than 93.07% of Python3
     Memory Usage: 14.2 MB, less than 81.41% of Python3

     Time and Space complexity: O(1)
    """

    def romanToInt(self, s: str) -> int:
        result = rom2int[s[-1]]

        for i in range(len(s) - 2, -1, -1):
            if rom2int[s[i]] < rom2int[s[i + 1]]:
                result -= rom2int[s[i]]
            else:
                result += rom2int[s[i]]
        return result


if __name__ == '__main__':
    solutions = [Solution(), Solution2()]
    tc = (
        ("MMMDCCCCLXXXXVIIII", 3999),
        ("MCMXCVI", 1996),  # 1000 + (1000-100) + (100-10) + 6
        ("III", 3),
        ("IV", 4),
        ("IX", 9),
        ("LVIII", 58),
    )
    for sol in solutions:
        for inp, exp in tc:
            assert sol.romanToInt(inp) == exp
