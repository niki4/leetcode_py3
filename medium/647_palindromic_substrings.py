"""
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are
counted as different substrings even they consist of same characters.

Example 1:
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

Note:
The input string length won't exceed 1000.
"""

class Solution:
    """
    Runtime: 112 ms, faster than 90.60% of Python3.
    Memory Usage: 13.3 MB, less than 43.25% of Python3.

    Algorithm idea: expand (string while palindrome) around center where center is the
    current i-th element of the string.

    Time Complexity: O(N^2) where N is the length of S. Each expansion might do O(N) work.
    Space Complexity: O(1)
    """
    def countSubstrings(self, s: str) -> int:
        len_s = len(s)
        p_substr = 0

        for center in range(2*len_s-1):
            left = center // 2
            right = left + center % 2

            while left >= 0 and right < len_s and s[left] == s[right]:
                p_substr += 1
                left -= 1
                right += 1
        return p_substr


class Solution2:
    """
    Runtime: 340 ms, faster than 33.78% of Python3.
    Memory Usage: 21.7 MB, less than 16.04% of Python3.

    Algorithm idea:
        A Dynamic Programming approach to this problem is to build a table with all
        possible string[start:end] combinations, storing which are palindromes
        and which are not (True or False). At any given moment, when you're checking
        if string[i:j] is a palindrome, you only need to know two things:
            1. Is string[i] equal to string[j]?
            2. Is string[i+1:j-1] a palindrome?
        For condition (1), a simple check might do, for condition (2), you use the table.
        If both conditions are met, mark table[i][j] as True and increase your count.

    Time Complexity: O(n^2)
    Space Complexity: O(n^2)
    """
    def countSubstrings(self, s: str) -> int:
        len_s = len(s)
        dp = [[False for _ in range(len_s)] for _ in range(len_s)]
        count = 0
        for i in range(len_s-1, -1, -1):
            dp[i][i] = True
            count += 1
            for j in range(i+1, len(s)):
                if j == i+1 and s[i] == s[j]:
                    dp[i][j] = True
                    count += 1
                if j > i+1 and dp[i+1][j-1] and s[i] == s[j]:
                    dp[i][j] = True
                    count += 1
        return count


if __name__ == "__main__":
    s1 = Solution().countSubstrings
    s2 = Solution2().countSubstrings
    assert s1("abc") == s2("abc") == 3
    assert s1("aaa") == s2("aaa") == 6
    assert s1("fdsklf") == s2("fdsklf") == 6
