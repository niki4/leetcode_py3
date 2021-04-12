"""
A string s is called good if there are no two different characters in s that have the same frequency.

Given a string s, return the minimum number of characters you need to delete to make s good.

The frequency of a character in a string is the number of times it appears in the string.
For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.

Example 1:
Input: s = "aab"
Output: 0
Explanation: s is already good.

Example 2:
Input: s = "aaabbbcc"
Output: 2
Explanation: You can delete two 'b's resulting in the good string "aaabcc".
Another way it to delete one 'b' and one 'c' resulting in the good string "aaabbc".

Example 3:
Input: s = "ceabaacb"
Output: 2
Explanation: You can delete both 'c's resulting in the good string "eabaab".
Note that we only care about characters that are still in the string at the end (i.e. frequency of 0 is ignored).

Constraints:
    1 <= s.length <= 105
    s contains only lowercase English letters.
"""

import collections


class Solution:
    """
    Greedy algorithm

    Runtime: 116 ms, faster than 88.01% of Python3
    Memory Usage: 15.2 MB, less than 10.69% of Python3

    Time: O(n) to traverse s and make frequency counters
    Space: O(1) as we limited to only lowercase English letters (so freq list size never exceed 26 items).
    """

    def minDeletions(self, s: str) -> int:
        freq = list(collections.Counter(s).values())
        diff = 0
        for i in range(len(freq)):
            while freq.count(freq[i]) >= 2 and freq[i] > 0:
                freq[i] -= 1
                diff += 1
        return diff


class Solution2:
    """
    Optimized first solution:
    do not look for duplicates into list for each iteration, use set instead which has O(1) lookup

    Runtime: 108 ms, faster than 96.85% of Python3
    Memory Usage: 15.1 MB, less than 10.69% of Python3
    """

    def minDeletions(self, s: str) -> int:
        freq = collections.Counter(s)
        seen, diff = set(), 0
        for ch_freq in freq.values():
            while ch_freq in seen:  # we already counted char with the same frequency, decrease count of curr char
                ch_freq -= 1
                diff += 1
            if ch_freq > 0:
                seen.add(ch_freq)
        return diff


if __name__ == '__main__':
    tc = (
        ("aab", 0),
        ("aaabbbcc", 2),
        ("ceabaacb", 2),
    )
    solutions = (
        Solution(),
        Solution2(),
    )
    for sol in solutions:
        for inp_s, exp_diff in tc:
            assert sol.minDeletions(inp_s) == exp_diff
