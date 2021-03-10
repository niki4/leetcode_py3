"""
Given a string num which represents an integer, return true if num is a strobogrammatic number.

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Example 1:

Input: num = "69"
Output: true

Example 2:
Input: num = "88"
Output: true

Example 3:
Input: num = "962"
Output: false
"""


class Solution:
    """
    Build rotated string and compare with the source string. Strobogrammatic strings shall equal.

    Runtime: 28 ms, faster than 80.88% of Python3
    Memory Usage: 14.3 MB, less than 12.53% of Python3

    Time / Space complexity: O(n)
    """

    def isStrobogrammatic(self, num: str) -> bool:
        strob = {"0": "0", "1": "1", "6": "9", "9": "6", "8": "8"}
        rev_num = list()
        for n in num:
            if n in strob:
                rev_num.append(strob[n])
            else:
                return False
        return num == "".join(reversed(rev_num))


class Solution2:
    """
    Two-pointers approach

    Runtime: 28 ms, faster than 80.88% of Python3
    Memory Usage: 14 MB, less than 99.05% of Python3

    Time complexity: O(n) as we need to check all the digits in num
    Space complexity: O(1) as we use constant extra space for "strob" dict
    """

    def isStrobogrammatic(self, num: str) -> bool:
        strob = {"0": "0", "1": "1", "6": "9", "9": "6", "8": "8"}
        i, j = 0, len(num) - 1
        while i <= j:
            if num[i] not in strob or strob[num[i]] != num[j]:
                return False
            i += 1
            j -= 1
        return True


if __name__ == '__main__':
    solutions = [Solution(), Solution2()]
    tc = (
        ("69", True),
        ("88", True),
        ("962", False),
        ("1", True),
        ("2", False),
        ("101", True),
    )
    for s in solutions:
        for inp, exp in tc:
            res = s.isStrobogrammatic(inp)
            assert res is exp, f"{s.__class__.__name__}: for input {inp} expected {exp}, got {res}"
