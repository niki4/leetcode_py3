"""
Given a string s, find the longest palindromic substring in s.
You may assume that the maximum length of s is 1000.

Example 1:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: "cbbd"
Output: "bb"
"""


class Solution:
    """
    Bruteforce Approach (pick all possible start and end positions for a substring, and verify if it is a palindrome.)

    Runtime: 6856 ms, faster than 10.43% of Python3.
    Memory Usage: 13.3 MB, less than 28.45% of Python3.

    Runtime complexity: O(n**3).
    Two loops takes (n**2), Since verifying each substring takes O(n) time, the overall run time complexity is O(n**3).
    Space complexity: O(n) to store "longest_palindrome" which in worst case will be the same length as "s".
    We can optimize it to O(1) if we store/update idxs of longest substring rather than slice a string.

    Naive solution. Expectedly slow.
    """

    def longestPalindrome(self, s: str) -> str:
        longest_palindrome = ''
        for i in range(len(s)):
            for j in range(len(s), i, -1):
                substr = s[i:j]
                if substr == substr[::-1] and len(substr) > len(longest_palindrome):
                    longest_palindrome = substr
        return longest_palindrome


class Solution2:
    """
    Expand Around Center

    Runtime: 892 ms, faster than 81.94% of Python3.
    Memory Usage: 13.3 MB, less than 44.62% of Python3.

    Time complexity : O(n**2).
    We need O(n) for main iteration. Since expanding a palindrome around its center could take O(n) time.
    Space complexity : O(n).
    """

    def get_palindrome(self, s, left, right):
        """ Returns largest possible palindrome string starting from the provided center """
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    def longestPalindrome(self, s: str) -> str:
        longest_palindrome = s[0] if s else ''

        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:  # even string, e.g. "aa"
                p = self.get_palindrome(s, i - 1, i + 2)
                if len(p) > len(longest_palindrome):
                    longest_palindrome = p

            if len(s) > i + 2 and s[i] == s[i + 2]:  # odd string, e.g. "aba"
                p = self.get_palindrome(s, i - 1, i + 3)
                if len(p) > len(longest_palindrome):
                    longest_palindrome = p
        return longest_palindrome


class Solution3:
    """
    Runtime: 76 ms, faster than 96.95% of Python3.
    Memory Usage: 13.2 MB, less than 55.56% of Python3.
    """

    def longestPalindrome(self, s: str) -> str:
        len_s = len(s)
        if len_s <= 1:
            return s

        min_start, max_len, i = 0, 1, 0
        while i < len_s:
            if len_s - i <= max_len // 2:
                break
            j, k = i, i
            while k < len_s - 1 and s[k] == s[k + 1]:
                k += 1
            i = k + 1
            while k < len_s - 1 and j and s[k + 1] == s[j - 1]:
                k, j = k + 1, j - 1
            if k - j + 1 > max_len:
                min_start, max_len = j, k - j + 1
        return s[min_start:(min_start + max_len)]


if __name__ == "__main__":
    solutions = [Solution(), Solution2(), Solution3()]
    tc = (
        ("aaaa", "aaaa"),
        ("babad", "bab"),
        ("cbbd", "bb"),
        ("abcba", "abcba"),
        ("a", "a"),
        ("", ""),
        ("ccc", "ccc"),
    )
    for sol in solutions:
        for inp, exp in tc:
            res = sol.longestPalindrome(inp)
            assert res == exp, f'{sol.__class__.__name__}: for input "{inp}" expected "{exp}", got "{res}"'
