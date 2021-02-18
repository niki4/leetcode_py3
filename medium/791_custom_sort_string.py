"""
S and T are strings composed of lowercase letters. In S, no letter occurs more than once.

S was sorted in some custom order previously. We want to permute the characters of T so that they match the order that S was sorted. More specifically, if x occurs before y in S, then x should occur before y in the returned string.

Return any permutation of T (as a string) that satisfies this property.

Example :
Input:
S = "cba"
T = "abcd"
Output: "cbad"
Explanation:
"a", "b", "c" appear in S, so the order of "a", "b", "c" should be "c", "b", and "a".
Since "d" does not appear in S, it can be at any position in T. "dcba", "cdba", "cbda" are also valid outputs.

Note:

S has length at most 26, and no character is repeated in S.
T has length at most 200.
S and T consist of lowercase letters only.
"""


class Solution:
    """
    Use key function as a primer for sorted()

    Runtime: 32 ms, faster than 61.32% of Python3
    Memory Usage: 14.4 MB, less than 22.04% of Python3

    Time / Space complexity: O(n)
    """

    def customSortString(self, S: str, T: str) -> str:
        s_pos = {ch: i for (i, ch) in enumerate(S)}
        t_common_s = [ch for ch in T if ch in s_pos]
        t_diff_s = [ch for ch in T if ch not in s_pos]
        res = sorted(t_common_s, key=s_pos.get) + t_diff_s
        return "".join(res)


if __name__ == '__main__':
    solutions = [Solution()]
    for sol in solutions:
        assert sol.customSortString("cba", "abcd") == "cbad"
