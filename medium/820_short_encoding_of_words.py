"""
A valid encoding of an array of words is any reference string s and array of indices indices such that:

    * words.length == indices.length
    * The reference string s ends with the '#' character.
    * For each index indices[i], the substring of s starting from indices[i] and up to (but not including) the next '#' character is equal to words[i].

Given an array of words, return the length of the shortest reference string s possible of any valid encoding of words.


Example 1:
    Input: words = ["time", "me", "bell"]
    Output: 10
Explanation: A valid encoding would be s = "time#bell#" and indices = [0, 2, 5].
words[0] = "time", the substring of s starting from indices[0] = 0 to the next '#' is underlined in "time#bell#"
words[1] = "me", the substring of s starting from indices[1] = 2 to the next '#' is underlined in "time#bell#"
words[2] = "bell", the substring of s starting from indices[2] = 5 to the next '#' is underlined in "time#bell#"

Example 2:
    Input: words = ["t"]
    Output: 2
Explanation: A valid encoding would be s = "t#" and indices = [0].
"""
from typing import List


class Solution:
    """
    Algorithm:
        1. If a word X is a suffix of Y, then it does not need to be considered, as the encoding of Y in the reference
        string will also encode X. For example, if "me" and "time" is in words, we can throw out "me" without changing
        the answer.
        2. If a word Y does not have any other word X (in the list of words) that is a suffix of Y, then Y must be part
        of the reference string.
        3. Thus, the goal is to remove words from the list such that no word is a suffix of another.
        The final answer would be sum(word.length + 1 for word in words).

        For example:
        In: sol.minimumLengthEncoding(["time", "me"])
        good init set: {'time', 'me'}
        discard word[k:] 'ime'		now good: {'time', 'me'}
        discard word[k:] 'me'		now good: {'time'}
        discard word[k:] 'e'		now good: {'time'}
        discard word[k:] 'e'		now good: {'time'}
        result string: 'time#'		return its len: 5
        Out: 5

        In: sol.minimumLengthEncoding(["t"])
        good init set: {'t'}
        result string: 't#'		return its len: 2
        Out: 2

    Runtime: 112 ms, faster than 92.44% of Python3
    Memory Usage: 15.1 MB, less than 83.72% of Python3

    Time Complexity: O(sum(Wi^2)) where Wi is the length of words[i]
    Space Complexity: O(sum(Wi)) the space used in storing suffixes.
    """

    def minimumLengthEncoding(self, words: List[str]) -> int:
        good = set(words)
        for word in words:
            for k in range(1, len(word)):
                good.discard(word[k:])
        return sum(len(word) + 1 for word in good)


if __name__ == '__main__':
    solutions = [Solution()]
    tc = (
        (["time", "me", "bell"], 10),
        (["t"], 2),
        (["me", "time"], 5),
    )
    for sol in solutions:
        for inp, exp in tc:
            res = sol.minimumLengthEncoding(inp)
            assert res == exp, f"{sol.__class__.__name__}: expected {exp}, got {res}"
