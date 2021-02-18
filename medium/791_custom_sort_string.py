"""
S and T are strings composed of lowercase letters. In S, no letter occurs more than once.

S was sorted in some custom order previously. We want to permute the characters of T so that they match the order that S was sorted. More specifically, if x occurs before y in S, then x should occur before y in the returned string.

Return any permutation of T (as a string) that satisfies this property.

Example :
Input:
S =     "cba"
T =     "abcd"
Output: "cbad"
Explanation:
"a", "b", "c" appear in S, so the order of "a", "b", "c" should be "c", "b", and "a".
Since "d" does not appear in S, it can be at any position in T. "dcba", "cdba", "cbda" are also valid outputs.

Note:
    S has length at most 26, and no character is repeated in S.
    T has length at most 200.
    S and T consist of lowercase letters only.
"""
import collections

"""
For all solutions
Time Complexity:  O(S.length+T.length), the time it takes to iterate through S and T
Space Complexity: O(T.length). 
                  We count at most 26 different lowercase letters, but the final answer has the same length as T.
"""


class Solution:
    """
    Use key function as a primer for sorted()

    Runtime: 32 ms, faster than 61.32% of Python3
    Memory Usage: 14.4 MB, less than 22.04% of Python3
    """

    def customSortString(self, S: str, T: str) -> str:
        s_pos = {ch: i for (i, ch) in enumerate(S)}
        t_common_s = [ch for ch in T if ch in s_pos]
        t_diff_s = [ch for ch in T if ch not in s_pos]
        res = sorted(t_common_s, key=s_pos.get) + t_diff_s
        return "".join(res)


class Solution2:
    """
    Optimized first solution. Now key function improved so that it returns -1 order for non intersecting keys (that
    means all those keys will be prefixed the result sorted letters)

    Runtime: 16 ms, faster than 99.85% of Python3
    Memory Usage: 14.2 MB, less than 55.02% of Python3
    """

    def customSortString(self, S: str, T: str) -> str:
        s_pos = {ch: i for (i, ch) in enumerate(S)}
        return "".join(sorted(T, key=lambda t_key: s_pos.get(t_key, -1)))


class Solution3:
    """
    Using counter (hash map) to count num of values per each letter, and S string as a primer.

    Runtime: 28 ms, faster than 84.35% of Python3
    Memory Usage: 14.4 MB, less than 22.04% of Python3
    """

    def customSortString(self, S: str, T: str) -> str:
        result = ""
        t_ctr = collections.Counter(T)

        for ch in S:
            result += ch * t_ctr[ch]  # e.g., "a" * 3 = "aaa"
            t_ctr[ch] = 0  # discard counter for char we just processed

        # add chars that are not present in S
        for ch in t_ctr:
            if t_ctr[ch]:
                result += ch * t_ctr[ch]
        return result


if __name__ == '__main__':
    solutions = [Solution(), Solution2(), Solution3()]
    for sol in solutions:
        res = sol.customSortString("cba", "abcd")
        assert res in ("cbad", "dcba", "cdba")
