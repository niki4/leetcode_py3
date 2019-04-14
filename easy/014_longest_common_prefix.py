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

    def longestCommonPrefix2(self, strs):
        """
        Albeit the following code is not what interviewers would expect
        from you, it's good to know there's some short path.

        Runtime: 40 ms, faster than 72.98% of Python3.
        Memory Usage: 13.4 MB, less than 5.10% of Python3.
        """
        return os.path.commonprefix(strs)

    def longestCommonPrefix3(self, strs):
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
    s = Solution()
    lcp1 = s.longestCommonPrefix
    lcp2 = s.longestCommonPrefix2
    lcp3 = s.longestCommonPrefix3
    src1 = ["flower", "flow", "flight"]
    src2 = ["dog", "racecar", "car"]
    assert lcp1(src1) == lcp2(src1) == lcp3(src1) == "fl"
    assert lcp1(src2) == lcp2(src2) == lcp3(src2) == ""
