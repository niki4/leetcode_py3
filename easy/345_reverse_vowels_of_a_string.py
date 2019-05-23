"""
Write a function that takes a string as input and reverse only
the vowels of a string.

Example 1:
Input: "hello"
Output: "holle"

Example 2:
Input: "leetcode"
Output: "leotcede"

Note:
The vowels does not include the letter "y".
"""

class Solution:
    """
    Runtime: 100 ms, faster than 12.61% of Python3.
    Memory Usage: 15.3 MB, less than 11.30% of Python3.

    Well, at least this solution is easy to understand :)
    """
    def is_vowel(self, ltr: str) -> bool:
        vowels = 'aeiouAEIOU'
        return ltr in vowels

    def reverseVowels(self, s: str) -> str:
        vowel_idxs = []

        for idx, ltr in enumerate(s):
            if self.is_vowel(ltr):
                vowel_idxs.append(idx)

        chars = list(s)
        for i in range(len(chars)):
            if self.is_vowel(chars[i]):
                swap_to_idx = vowel_idxs.pop()
                chars[i] = s[swap_to_idx]
        return ''.join(chars)


if __name__ == "__main__":
    s = Solution()
    assert s.reverseVowels("hello") == "holle"
    assert s.reverseVowels("leetcode") == "leotcede"
    assert s.reverseVowels("aA") == "Aa"
