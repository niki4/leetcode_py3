"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""

class Solution:
    """
    Runtime: 64 ms, faster than 57.81% of Python3.
    Memory Usage: 14.1 MB, less than 12.99% of Python3.

    Naive approach is to compare sorted lists.
    """
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


class Solution2:
    """
    Runtime: 56 ms, faster than 74.85% of Python3.
    Memory Usage: 13.4 MB, less than 39.13% of Python3.

    Another way is to compare sum of hashes for chars in words.
    """

    def isAnagram(self, s: str, t: str) -> bool:
        return sum(hash(c) for c in s) == sum(hash(c) for c in t)


class Solution3:
    """
    Runtime: 48 ms, faster than 59.52% of Python3
    Memory Usage: 14.8 MB, less than 15.92% of Python3

    A couple of lazy evaluation optimizations of Solution1.
    """

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        s_sorted, t_sorted = sorted(s), sorted(t)
        for i, s_v in enumerate(s_sorted):
            if s_v != t_sorted[i]:
                return False
        return True


if __name__ == "__main__":
    solutions = [Solution(), Solution2(), Solution3()]
    tc = [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
    ]
    for sol in solutions:
        for s, t, expected in tc:
            assert sol.isAnagram(s, t) == expected
