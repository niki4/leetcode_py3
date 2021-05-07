"""
You are given a string allowed consisting of distinct characters and an array of strings words.
A string is consistent if all characters in the string appear in the string allowed.

Return the number of consistent strings in the array words.

Example 1:
Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
Output: 2
Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.
"""
from typing import List


class Solution:
    """
    For each word iterate over it and check all letters are in allowed (consistent).

    Runtime: 248 ms, faster than 51.48% of Python3
    Memory Usage: 16.2 MB, less than 13.60% of Python3

    Time complexity: O(n*k) where n is the length of the words list and k is the median length of word.
    Space complexity: O(1)
    """

    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        consistent = 0
        for word in words:
            if all(ltr in allowed for ltr in word):
                consistent += 1
        return consistent


class Solution2:
    """
    Using hash set, for each word compare (letters) difference between a word and allowed.

    Runtime: 288 ms, faster than 18.49% of Python3
    Memory Usage: 16 MB, less than 92.44% of Python3

    Time complexity: O(n*k)
    Space complexity: O(1)
    """

    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        consistent = 0
        for word in words:
            if len(set(word).difference(allowed)) == 0:
                consistent += 1
        return consistent


if __name__ == '__main__':
    solutions = [Solution(), Solution2()]
    tc = (
        ("ab", ["ad", "bd", "aaab", "baa", "badab"], 2),
        ("abc", ["a", "b", "c", "ab", "ac", "bc", "abc"], 7),
        ("cad", ["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"]),
    )
