"""
Given an array of strings arr. String s is a concatenation of a sub-sequence of arr which have unique characters.

Return the maximum possible length of s.

Example 1:
Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All possible concatenations are "","un","iq","ue","uniq" and "ique".
Maximum length is 4.

Example 2:
Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible solutions are "chaers" and "acters".

Example 3:
Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26

Constraints:
    1 <= arr.length <= 16
    1 <= arr[i].length <= 26
    arr[i] contains only lower case English letters.
"""
from typing import List


class Solution:
    """
    Dynamic Programming (DP) approach. Seems slow in the terms of the task.

    Runtime: 1176 ms, faster than 7.82% of Python3
    Memory Usage: 25.4 MB, less than 23.91% of Python3
    """

    def maxLength(self, arr: List[str]) -> int:
        comb = [""]
        for subseq in arr:
            comb += [c + subseq for c in comb]
        unique_only = [c for c in comb if len(c) == len(set(c))]
        return len(max(unique_only, key=len))


class Solution2:
    """
    Optimized first solution. Seem there's quite little difference for the performance.

    Runtime: 1112 ms, faster than 8.27% of Python3
    Memory Usage: 25.5 MB, less than 23.91% of Python3
    """

    def maxLength(self, arr: List[str]) -> int:
        comb = [""]
        unique_len = 0

        for subseq in arr:
            if len(subseq) == len(set(subseq)):
                comb += [c + subseq for c in comb]

        for c in comb:
            if len(c) == len(set(c)):
                unique_len = max(unique_len, len(c))
        return unique_len


class Solution3:
    """
    DP solution adopted from
    problems/maximum-length-of-a-concatenated-string-with-unique-characters/discuss/414172/PythonC%2B%2BJava-Set-Solution
        "For each string,
        we check if it's conflict with the combination that we found.
        If they have intersection of characters (s & c), we skip it.
        If not, we append this new combination (s | c) to result."

    "x1 & x2" is equivalent to "x1.intersection(x2)" and return set of elements common to both x1 and x2.
    "x1 | x2" is equivalent to "x1.union(x2)" and return set of all elements from both x1 and x2.

    Runtime: 96 ms, faster than 78.20% of Python3
    Memory Usage: 58 MB, less than 9.58% of Python3

    Time complexity: O(2^N), where N is the number of strings in the input vector.
    """

    def maxLength(self, arr: List[str]) -> int:
        comb = [set("")]
        for subseq in arr:
            if len(subseq) == len(set(subseq)):
                s = set(subseq)
                comb += [(s | c) for c in comb if not (s & c)]
        return len(max(comb, key=len))


if __name__ == '__main__':
    tc = (
        (["un", "iq", "ue"], 4),
        (["cha", "r", "act", "ers"], 6),
        (["abcdefghijklmnopqrstuvwxyz"], 26),
        ([], 0),
    )
    solutions = (
        Solution(),
        Solution2(),
        Solution3(),
    )
    for sol in solutions:
        for inp_arr, exp_max in tc:
            assert sol.maxLength(inp_arr) == exp_max
