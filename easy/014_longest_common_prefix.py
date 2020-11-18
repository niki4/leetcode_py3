"""
Write a function to find the longest common prefix
string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""
import os
from typing import List


class Solution:
    def longestCommonPrefix(self, strs):
        """
        Runtime: 40 ms, faster than 72.98% of Python3.
        Memory Usage: 13.2 MB, less than 5.10% of Python3.
        """
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]

        max_pref = str()
        first = strs[0]

        for i in range(len(first)):
            curr_pref = first[:i + 1]
            if all(map(lambda x: x.startswith(curr_pref), strs)):
                max_pref = curr_pref
            else:
                break
        return max_pref


class Solution2:
    """
    Runtime: 36 ms, faster than 45.30% of Python3
    Memory Usage: 14.3 MB, less than 35.84% of Python3
    """

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        min_str = min(strs, key=len)
        if not min_str:
            return ""

        for i, v in enumerate(min_str):
            if all(s[i] == v for s in strs):
                if i == len(min_str) - 1:
                    return min_str
                else:
                    continue
            else:
                return min_str[:i]


class Solution3:
    def longestCommonPrefix(self, strs):
        """
        Albeit the following code is not what interviewers would expect
        from you, it's good to know there's some short path.

        Runtime: 40 ms, faster than 72.98% of Python3.
        Memory Usage: 13.4 MB, less than 5.10% of Python3.
        """
        return os.path.commonprefix(strs)


class Solution4:
    def longestCommonPrefix(self, strs):
        """
        Divide and conquer approach.

        Runtime: 40 ms, faster than 72.98% of Python3.
        Memory Usage: 13.3 MB, less than 5.10% of Python3.
        """
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]

        left = self.longestCommonPrefix(strs[:len(strs) // 2])
        right = self.longestCommonPrefix(strs[len(strs) // 2:])

        def common_prefix(left: str, right: str) -> str:
            min_len = min(len(left), len(right))
            for i in range(min_len):
                if left[i] != right[i]:
                    return left[:i]
            return left[:min_len]

        return common_prefix(left, right)


if __name__ == '__main__':
    solutions = [Solution(), Solution2(), Solution3(), Solution4()]
    tc = [
        (["flower", "flow", "flight"], "fl"),
        (["dog", "racecar", "car"], ""),
        ([""], ""),
    ]
    for s in solutions:
        for inp, exp in tc:
            assert s.longestCommonPrefix(inp) == exp
