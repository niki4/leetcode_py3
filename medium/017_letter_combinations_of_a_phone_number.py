"""
Given a string containing digits from 2-9 inclusive,
return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.

Constraints:
0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
"""
from typing import List


class Solution:
    """
    Backtracking

    Runtime: 32 ms, faster than 64.08% of Python3
    Memory Usage: 14.3 MB, less than 35.65% of Python3
    """

    def letterCombinations(self, digits: str) -> List[str]:
        dial_pad = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        cmb = [""] if digits else []
        for d in digits:
            cmb = [p + q for p in cmb for q in dial_pad[d]]
        return cmb


if __name__ == '__main__':
    solutions = [Solution()]
    tc = (
        ("23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
        ("", []),
        ("2", ["a", "b", "c"]),
    )
    for s in solutions:
        for inp_digits, exp in tc:
            assert s.letterCombinations(inp_digits) == exp
