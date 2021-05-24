"""
Given two strings str1 and str2 of the same length, determine whether you can transform str1 into str2 by doing zero
or more conversions.

In one conversion you can convert all occurrences of one character in str1 to any other lowercase English character.

Return true if and only if you can transform str1 into str2.

Example 1:
Input: str1 = "aabcc", str2 = "ccdee"
Output: true
Explanation: Convert 'c' to 'e' then 'b' to 'd' then 'a' to 'c'. Note that the order of conversions matter.

Example 2:
Input: str1 = "leetcode", str2 = "codeleet"
Output: false
Explanation: There is no way to transform str1 to str2.

Constraints:
    1 <= str1.length == str2.length <= 104
    str1 and str2 contain only lowercase English letters.
"""


class Solution:
    """
    Runtime: 32 ms, faster than 50.63% of Python3
    Memory Usage: 14.4 MB, less than 58.68% of Python3

    Time/Space complexity: O(n)
    """

    def canConvert(self, str1: str, str2: str) -> bool:
        if str1 == str2:
            return True

        conv_tbl = dict()  # conversion table
        for i in range(len(str1)):
            if str1[i] not in conv_tbl:
                conv_tbl[str1[i]] = str2[i]
            else:
                if str2[i] != conv_tbl[str1[i]]:
                    return False
        return len(set(str2)) < 26  # if all 26 characters are represented, there are no characters available to use
        # for temporary conversions, and the transformation is impossible. The only exception to this is if str1 is
        # equal to str2, so we handle this case at the start of the function.


if __name__ == '__main__':
    solutions = [Solution()]
    tc = (
        ("aabcc", "ccdee", True),
        ("leetcode", "codeleet", False),
        ("abcdefghijklmnopqrstuvwxyz", "bcadefghijklmnopqrstuvwxzz", True),
        ("abcdefghijklmnopqrstuvwxyz", "bcdefghijklmnopqrstuvwxyza", False),
    )
    for sol in solutions:
        for inp_s1, inp_s2, expected_res in tc:
            assert sol.canConvert(inp_s1, inp_s2) is expected_res, f"{sol.__class__.__name__}"
