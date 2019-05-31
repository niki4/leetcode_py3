"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p
will not be larger than 20,100.

The order of output does not matter.

Example 1:
Input:
    s: "cbaebabacd" p: "abc"
Output:
    [0, 6]
Explanation:
    The substring with start index = 0 is "cba", which is an anagram of "abc".
    The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
Input:
    s: "abab" p: "ab"
Output:
    [0, 1, 2]
Explanation:
    The substring with start index = 0 is "ab", which is an anagram of "ab".
    The substring with start index = 1 is "ba", which is an anagram of "ab".
    The substring with start index = 2 is "ab", which is an anagram of "ab".
"""

class Solution:
    """
    Runtime: 100 ms, faster than 97.22% of Python3.
    Memory Usage: 14.3 MB, less than 20.94% of Python3.

    The algorithm uses sliding window, which works on each iteration as below:
    1. Increase counter for current idx char
    2. Decrease counter for char that just left out of sliding window size
    3. Check if current list equal to the list made of 'p' arg. Then go next iteration.
    """
    def findAnagrams(self, s: str, p: str) -> list:
        result = []
        m = [0] * 26
        for char in p:
            m[ord(char) - 97] += 1  # count ltrs in p
        current = [0] * 26
        p_len = len(p)

        for idx, char in enumerate(s):
            current[ord(char) - 97] += 1
            if idx >= p_len:
                current[ord(s[idx - p_len]) - 97] -= 1  # decrease for val that left out of window

            if current == m:
                result.append(idx - p_len + 1)
        return result


if __name__ == "__main__":
    sol = Solution()
    assert sol.findAnagrams("cbaebabacdx", "abc") == [0, 6]
    assert sol.findAnagrams("abab", "ab") == [0, 1, 2]
