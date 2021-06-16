"""
Given a string s and an integer k. You should construct k non-empty palindrome strings using all the characters in s.

Return True if you can use all the characters in s to construct k palindrome strings or False otherwise.

Example 1:
    Input: s = "annabelle", k = 2
    Output: true
    Explanation: You can construct two palindromes using all characters in s.
    Some possible constructions "anna" + "elble", "anbna" + "elle", "anellena" + "b"

Constraints:
    1 <= s.length <= 10^5
    All characters in s are lower-case English letters.
    1 <= k <= 10^5
"""

import collections


class Solution:
    """
    The algorithm idea is that we can build a palindrome either by wrapping odd-count char by even-count chars,
    e.g. "aba", or leave it as a single char (e.g., "b"). Thus we need to calculate how many characters in string are
    odd-count - their number should be equal or less than k (number of palindrome-partitions).

    Time complexity: O(n)
    Space complexity: O(1)
    """

    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s):  # we cannot construct number of parts equal to k
            return False

        ctr = collections.Counter(s)
        odd_count = sum(1 if ch_ctr % 2 == 1 else 0 for ch_ctr in ctr.values())
        if odd_count > k:  # then minimum number of palindrome strings we can construct is > k
            return False

        # at this point we can construct exactly k palindrome strings
        return True


if __name__ == '__main__':
    solutions = [Solution()]
    tc = (
        ("annabelle", 2, True),  # possible constructions "anna" + "elble", "anbna" + "elle", "anellena" + "b"
        ("leetcode", 3, False),  # it is impossible to construct 3 palindromes using all the characters of s.
        ("true", 4, True),  # the only possible solution is to put each character in a separate string.
        ("yzyzyzyzyzyzyzy", 2, True),  # We can simply put all z's in one string and all y's in the other string.
        ("cr", 7, False),  # We don't have enough characters in s to construct 7 palindromes.
    )
    for sol in solutions:
        for inp_s, inp_k, can_be_constructed in tc:
            assert sol.canConstruct(inp_s, inp_k) is can_be_constructed
