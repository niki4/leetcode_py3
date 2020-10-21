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


class Solution2:
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
    solutions = [Solution(), Solution2()]
    for sol in solutions:
        assert sol.lengthOfLongestSubstring("abcabcbb") == 3
        assert sol.lengthOfLongestSubstring("bbbbb") == 1
        assert sol.lengthOfLongestSubstring("pwwkew") == 3
        assert sol.lengthOfLongestSubstring("aab") == 2
        assert sol.lengthOfLongestSubstring("dvdf") == 3
        assert sol.lengthOfLongestSubstring("anviaj") == 5
        assert sol.lengthOfLongestSubstring("tvqnkvovks") == 5
        assert sol.lengthOfLongestSubstring("") == 0
        assert sol.lengthOfLongestSubstring("cekwrebvhvtlesh") == 7
        assert sol.lengthOfLongestSubstring("gsqygebs") == 6
        assert sol.lengthOfLongestSubstring(" ") == 1
