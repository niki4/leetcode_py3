"""
Given a string s, you are allowed to convert it to a palindrome by adding characters
in front of it. Find and return the shortest palindrome you can find by performing
this transformation.

Example 1:
Input: "aacecaaa"
Output: "aaacecaaa"

Example 2:
Input: "abcd"
Output: "dcbabcd"
"""

class Solution:
    """
    Runtime: 60 ms, faster than 82.89% of Python3.
    Memory Usage: 13.3 MB, less than 58.03% of Python3.

    Example: s = dedcba.
    Then r = abcded and we try these overlays:
    s          dedcba
    r[0:]      abcded    Nope...
    r[1:]   (a)bcded     Nope...
    r[2:]  (ab)cded      Nope...
    r[3:] (abc)ded       Yes! Return abc + dedcba
    """
    def shortestPalindrome(self, s: str) -> str:
        r = s[::-1]
        for i in range(len(s) + 1):
            if s.startswith(r[i:]):
                return r[:i] + s


class Solution2:
    """
    Runtime: 72 ms, faster than 60.54% of Python3.
    Memory Usage: 16.4 MB, less than 10.92% of Python3.

    https://en.wikipedia.org/wiki/Knuth–Morris–Pratt_algorithm
    (see section named '"Partial match" table (also known as "failure function")')
    Also the image below clearly illustrates the approach:
    https://leetcode.com/problems/shortest-palindrome/Figures/214/shortest_palindrome.png

    Time complexity: Since the two portions of the algorithm have, respectively,
    complexities of O(k) and O(n), the complexity of the overall algorithm is O(n + k).
    """
    def shortestPalindrome(self, s: str) -> str:
        a = s + '*' + s[::-1]
        cont = [0]
        for i in range(1, len(a)):  # note we iterate over 'a' string, not 's'!
            index = cont[i-1]
            while index > 0 and a[index] != a[i]:
                index = cont[index-1]
            cont.append(index + int(a[index] == a[i]))
        return s[cont[-1]:][::-1] + s


class Solution3:
    """
    Runtime: 40 ms, faster than 98.34% of Python3.
    Memory Usage: 13.5 MB, less than 33.62% of Python3.

    Algorithm idea: we use j to compare character from end of s and beginning of s.
    If it's equal, increment j by 1. So we can use j-len(s) to divide s in two parts.
    1. The first part its that we know for sure its the suffix of result and it may need
    reversed and insert at beginning of result (s[j:][::-1]).
    2. The second part is that we don't know it's Palindrome, we pass it to the next recursive call.
    """
    def shortestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        j = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == s[j]:
                j += 1
        return s[j:][::-1] + self.shortestPalindrome(s[:j-len(s)]) + s[j-len(s):]


if __name__ == "__main__":
    s1 = Solution().shortestPalindrome
    s2 = Solution2().shortestPalindrome
    s3 = Solution3().shortestPalindrome
    src1 = "aacecaaa"
    src2 = "abcd"
    exp1 = "aaacecaaa"
    exp2 = "dcbabcd"
    assert s1(src1) == s2(src1) == s3(src1) == exp1
    assert s1(src2) == s2(src2) == s3(src2) == exp2
