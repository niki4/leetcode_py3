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


if __name__ == "__main__":
    sol = Solution()
    sol2 = Solution2()

    s1 = "anagram"
    t1 = "nagaram"
    s2 = "rat"
    t2 = "car"
    sol.isAnagram(s1, t1) == True
    sol.isAnagram(s2, t2) == False
    sol2.isAnagram(s1, t1) == True
    sol2.isAnagram(s2, t2) == False
