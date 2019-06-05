"""
You are given an array A of strings.

Two strings S and T are special-equivalent if after any number of moves, S == T.

A move consists of choosing two indices i and j with i % 2 == j % 2, and swapping S[i] with S[j].

Now, a group of special-equivalent strings from A is a non-empty subset S of A such that any
string not in S is not special-equivalent with any string in S.

Return the number of groups of special-equivalent strings from A.

Example 1:
Input: ["a","b","c","a","c","c"]
Output: 3
Explanation: 3 groups ["a","a"], ["b"], ["c","c","c"]

Note:
1 <= A.length <= 1000
1 <= A[i].length <= 20
All A[i] have the same length.
All A[i] consist of only lowercase letters.
"""

class Solution:
    """
    Runtime: 32 ms, faster than 99.84% of Python3.
    Memory Usage: 13.5 MB, less than 33.91% of Python3.

    The problem is special case of anagram problem.
    The algorithm is about to calculate unique groups.
    So, for "abc"[0::2] and "cba"[0::2] we have single group in set as sorted("ac")==sorted("ca").
    """
    def numSpecialEquivGroups(self, A: list) -> int:
        return len({(
            ''.join(sorted(s[0::2])),
            ''.join(sorted(s[1::2]))
            ) for s in A})


if __name__ == "__main__":
    s = Solution()
    assert s.numSpecialEquivGroups(["a","b","c","a","c","c"]) == 3
    assert s.numSpecialEquivGroups(["aa","bb","ab","ba"]) ==  4
    assert s.numSpecialEquivGroups(["abc","acb","bac","bca","cab","cba"]) == 3
    assert s.numSpecialEquivGroups(["abcd","cdab","adcb","cbad"]) == 1
