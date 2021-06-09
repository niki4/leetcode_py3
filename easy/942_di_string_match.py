"""
A permutation perm of n + 1 integers of all the integers in the range [0, n] can be represented as a string s of
length n where:
    s[i] == 'I' if perm[i] < perm[i + 1], and
    s[i] == 'D' if perm[i] > perm[i + 1].
Given a string s, reconstruct the permutation perm and return it. If there are multiple valid permutations perm,
return any of them.

Example 1:
Input: s = "IDID"
Output: [0,4,1,3,2]

Example 2:
Input: s = "III"
Output: [0,1,2,3]

Example 3:
Input: s = "DDI"
Output: [3,2,0,1]

Constraints:
    1 <= s.length <= 105
    s[i] is either 'I' or 'D'.
"""
from typing import List


class Solution:
    """
    Intuitive approach: use either max value (case "I") or min value (case "D").
    Handle special cases when len(s) == 1 separately.

    Runtime: 68 ms, faster than 36.71% of Python3
    Memory Usage: 15.4 MB, less than 7.12% of Python3
    """

    def diStringMatch(self, s: str) -> List[int]:
        if s == "I":
            return [0, 1]
        elif s == "D":
            return [1, 0]

        asc = list(range(len(s) + 1))
        desc = list(reversed(range(len(s) + 1)))
        result = []

        for permutation in s:
            if permutation == "I":
                result += [desc.pop()]
            elif permutation == "D":
                result += [asc.pop()]
        result += [asc.pop() if asc else desc.pop()]
        return result


class Solution2:
    """
    Slightly modified version of the first solution.

    Ad-Hoc approach (Greedy algorithm as we only consider the best choice for each stage):
        Intuition: If we see say S[0] == 'I', we can always put 0 as the first element; similarly, if we see S[0] == 'D'
        then we can always put N as the first element.
        Say we have a match for the rest of the string S[1], S[2], ... using N distinct elements. Notice it doesn't
        matter what the elements are, only that they are distinct and totally ordered. Then, putting 0 or N at the first
        character will match, and the rest of the elements (1, 2, ..., N or 0, 1, .., N-1) can use the matching we have.

    Algorithm: Keep track of the smallest and largest element we haven't placed. If we see an 'I', place the small
    element; otherwise place the large element.

    Runtime: 56 ms, faster than 95.29% of Python3
    Memory Usage: 15 MB, less than 93.28% of Python3

    Time Complexity: O(N), where N is the length of S.
    Space Complexity: O(N).
    """

    def diStringMatch(self, s: str) -> List[int]:
        asc, desc = 0, len(s)
        result = []

        for permutation in s:
            if permutation == "I":
                result.append(asc)
                asc += 1
            elif permutation == "D":
                result.append(desc)
                desc -= 1
        result.append(asc or desc)
        return result


if __name__ == '__main__':
    solutions = [Solution(), Solution2()]
    tc = (
        ("IDID", [0, 4, 1, 3, 2]),
        ("III", [0, 1, 2, 3]),
        ("DDI", [3, 2, 0, 1]),
        ("I", [0, 1]),
        ("D", [1, 0]),
    )
    for sol in solutions:
        for inp_s, exp_permutations in tc:
            assert sol.diStringMatch(inp_s) == exp_permutations
