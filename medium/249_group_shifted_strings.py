"""
Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

"abc" -> "bcd" -> ... -> "xyz"
Given a list of non-empty strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

Example:

Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
Output:
[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]
"""

from collections import defaultdict
from typing import List


class Solution:
    """
    Runtime: 40 ms, faster than 48.37% of Python3
    Memory Usage: 14.4 MB, less than 25.20% of Python3
    """

    def char_diff(self, s: str) -> tuple:
        """ calculates difference between adjacent chars.
            26 is the size of eng alpabet;
            ord returns integer codepoint for char;
        """
        res = ()
        for i in range(1, len(s)):
            res += (ord(s[i]) - ord(s[i - 1])) % 26,  # comma at the end makes a tuple
        return res

    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strings:
            groups[self.char_diff(word)].append(word)
        return list(groups.values())


if __name__ == '__main__':
    sol = Solution()
    tc = (
        (["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
         [
             ["abc", "bcd", "xyz"],
             ["az", "ba"],
             ["acef"],
             ["a", "z"]
         ]
         ),
    )
    for inp, exp in tc:
        res = sol.groupStrings(inp)
        assert sorted(res) == sorted(exp), f"expected {sorted(exp)},\ngot {sorted(res)}"
