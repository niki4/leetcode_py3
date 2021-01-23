"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:
Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

"""

__author__ = 'Ivan Nikiforov'


class Solution:
    """
    Bruteforce solution. TLE.

    Time complexity: O(n**3)
    Space complexity: O(k) where k is the size for slice
    """

    def lengthOfLongestSubstring(self, s: str) -> int:
        max_substr = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if len(s[i:j]) == len(set(s[i:j])):  # no duplicates
                    max_substr = max(max_substr, len(s[i:j]))
        return max_substr


class Solution2:
    """
    Runtime: 948 ms, faster than 7.40% of Python3 online submissions.
    Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions.
    """

    def lengthOfLongestSubstring(self, s: 'str') -> 'int':
        word = str()
        max_word = int()

        len_s = len(s)
        if len_s <= 1:
            return len_s

        idx = 1
        while idx <= len(s) - 1:
            prev_ltr, curr_ltr = s[idx - 1], s[idx]

            if not word:
                word = prev_ltr

            if curr_ltr != prev_ltr:
                if curr_ltr not in word:
                    word += curr_ltr
                else:
                    dup_idx = word.index(curr_ltr) + 1

                    s = s[s.index(word) + dup_idx:]  # truncate left to exclude dup ltr in old word
                    if s:
                        idx = 0
                        word = s[idx]
            else:
                word = curr_ltr

            len_word = len(word)
            if len_word > max_word:
                max_word = len_word

            idx += 1

        return max_word


class Solution3:
    """
    Runtime:  476 ms, faster than 15.36% of Python3 online submissions.
    Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions.

    Using sliding window
    """

    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_sstr_len = 0
        visited = set()
        end = 0

        for i in range(len(s)):
            for j in range(i, len(s)):
                ltr = s[j]
                if ltr in visited:
                    visited.clear()
                    break
                end = j
                visited.add(ltr)
            longest_sstr_len = max(longest_sstr_len, len(s[i:end + 1]))

        return longest_sstr_len


if __name__ == '__main__':
    solutions = [Solution(), Solution2(), Solution3()]
    tc = (
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("aab", 2),
        ("dvdf", 3),
        ("anviaj", 5),
        ("tvqnkvovks", 5),
        ("", 0),
        (" ", 1),
        ("cekwrebvhvtlesh", 7),
        ("gsqygebs", 6),
        ("au", 2),
    )
    for sol in solutions:
        for inp, exp in tc:
            res = sol.lengthOfLongestSubstring(inp)
            assert res == exp, f'{sol.__class__.__name__}: for input {inp} result {res} != {exp}'
