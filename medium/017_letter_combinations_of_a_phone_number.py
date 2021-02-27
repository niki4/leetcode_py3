"""
Given a string containing digits from 2-9 inclusive,
return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.

Constraints:
0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
"""
import itertools
from typing import List

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


class Solution:
    """
    Backtracking

    Runtime: 32 ms, faster than 64.08% of Python3
    Memory Usage: 14.3 MB, less than 35.65% of Python3

    Time complexity: O(3^N * 4^M) where N is the number of digits in the input that maps to 3 letters
                (e.g. 2, 3, 4, 5, 6, 8) and M is the number of digits in the input that maps to 4 letters (e.g. 7, 9),
                and N+M is the total number digits in the input.
    Space complexity: O(3^N * 4^M) since one has to keep 3^N * 4^M solutions.
    """

    def letterCombinations(self, digits: str) -> List[str]:
        cmb = [""] if digits else []
        for d in digits:
            cmb = [p + q for p in cmb for q in dial_pad[d]]
        return cmb


class Solution2:
    """
    Runtime: 20 ms, faster than 99.39% of Python3
    Memory Usage: 14.4 MB, less than 6.93% of Python3
    """

    def letterCombinations(self, digits: str) -> List[str]:
        letters = [dial_pad[d] for d in digits]
        return ["".join(cmb) for cmb in itertools.product(*letters)] if letters else []


if __name__ == '__main__':
    solutions = [Solution(), Solution2()]
    tc = (
        ("23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
        ("", []),
        ("2", ["a", "b", "c"]),
    )
    for s in solutions:
        for inp_digits, exp in tc:
            res = s.letterCombinations(inp_digits)
            assert res == exp, f"{s.__class__.__name__}: exp: {exp}\ngot: {res}"
