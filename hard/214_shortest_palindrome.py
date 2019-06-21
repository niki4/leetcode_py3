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


if __name__ == "__main__":
    s1 = Solution()
    s2 = Solution2()
    src1 = "aacecaaa"
    src2 = "abcd"
    exp1 = "aaacecaaa"
    exp2 = "dcbabcd"
    assert s1.shortestPalindrome(src1) == exp1
    assert s1.shortestPalindrome(src2) == exp2
    assert s2.shortestPalindrome(src1) == exp1
    assert s2.shortestPalindrome(src2) == exp2
