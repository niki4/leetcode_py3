"""
Given an array of strings words representing an English Dictionary, return the longest word in words that can be built
one character at a time by other words in words.

If there is more than one possible answer, return the longest word with the smallest lexicographical order.
If there is no answer, return the empty string.

Example 1:
    Input: words = ["w","wo","wor","worl","world"]
    Output: "world"
    Explanation: The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
Example 2:
    Input: words = ["a","banana","app","appl","ap","apply","apple"]
    Output: "apple"
    Explanation: Both "apply" and "apple" can be built from other words in the dictionary.
                 However, "apple" is lexicographically smaller than "apply".

Constraints:
    1 <= words.length <= 1000
    1 <= words[i].length <= 30
    words[i] consists of lowercase English letters.
"""
import collections
from typing import List


class Solution:
    """
    Bruteforce approach: collect all words that could be formed from the prefixes from the given list (so that, a word
    "world" could be formed from prefixes ["w", "wo", "wor", "worl"], also note that the last letter not counts). Then
    sort result list first by len, then by alphabet. Return the first item from the result list or "" if there no words.

    Runtime: 1628 ms, faster than 5.04% of Python3
    Memory Usage: 14.9 MB, less than 32.27% of Python3

    Time complexity: O(n^2) because we have to traverse the whole words list for each word from the list (find prefixes)
    Space complexity: O(n)
    """

    def longestWord(self, words: List[str]) -> str:
        words_with_prefixes = set()
        for word in words:
            prefixes = {pr for pr in words if word.startswith(pr) and pr != word}
            # if can be built one character at a time by other words in words.
            if len(prefixes) == len(word) - 1:
                words_with_prefixes.add(word)

        # sort by len in reverse order, then by lexicographical order
        sorted_words = sorted(words_with_prefixes, key=lambda w: (-len(w), w))
        return sorted_words[0] if sorted_words else ""


class Solution2:
    """
    Sort the words, then keep prefixes in the set and check for nextWord[:-1] in the set before comparing lengths.

    Runtime: 96 ms, faster than 55.17% of Python3
    Memory Usage: 14.6 MB, less than 84.38% of Python3

    Time complexity: O(N^2)
    Space complexity: O(N)
    """

    def longestWord(self, words: List[str]) -> str:
        words = sorted(words)  # lexicographical order
        prefixes, longest_word = {""}, ""
        for word in words:
            if word[:-1] in prefixes:
                if len(word) > len(longest_word):
                    longest_word = word
                prefixes.add(word)  # for the next candidate
        return longest_word


class TrieNode:
    def __init__(self):
        self.edges = collections.defaultdict(TrieNode)  # Map<Character, TrieNode>
        self.is_word_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for char in word:
            current = current.edges[char]  # create new edge if not exist
        current.is_word_end = True

    def can_be_built(self, word):  # from other words (one character at a time)
        current = self.root
        for char in word:
            if char not in current.edges:
                return False
            current = current.edges[char]
            if not current.is_word_end:
                return False
        return True


class Solution3:
    """
    Using Trie (prefix tree) which allows to share common prefixes in the words, as well as track each word end.

    Runtime: 176 ms, faster than 23.23% of Python3
    Memory Usage: 15.7 MB, less than 10.03% of Python3
    """

    def longestWord(self, words: List[str]) -> str:
        answer = ""
        trie = Trie()
        for word in words:
            trie.insert(word)

        for word in words:
            if trie.can_be_built(word):
                if answer == "" or len(answer) < len(word):
                    answer = word
                elif len(answer) == len(word):
                    answer = min(answer, word)  # keep alphabetical order
        return answer


if __name__ == '__main__':
    solutions = [Solution(), Solution2(), Solution3()]
    tc = (
        (["w", "wo", "wor", "worl", "world"], "world"),
        (["a", "banana", "app", "appl", "ap", "apply", "apple"], "apple"),
        (["wo", "wor", "worl", "world"], ""),
    )
    for sol in solutions:
        for inp_words, exp_longest in tc:
            result = sol.longestWord(inp_words)
            assert result == exp_longest, f"{sol.__class__.__name__}: actual '{result}' != '{exp_longest}' expected"
