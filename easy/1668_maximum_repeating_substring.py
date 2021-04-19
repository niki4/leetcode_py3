"""
For a string sequence, a string word is k-repeating if word concatenated k times is a substring of sequence.
The word's maximum k-repeating value is the highest value k where word is k-repeating in sequence.
If word is not a substring of sequence, word's maximum k-repeating value is 0.

Given strings sequence and word, return the maximum k-repeating value of word in sequence.

Example 1:

Input: sequence = "ababc", word = "ab"
Output: 2
Explanation: "abab" is a substring in "ababc".

Example 2:
Input: sequence = "ababc", word = "ba"
Output: 1
Explanation: "ba" is a substring in "ababc". "baba" is not a substring in "ababc".

Example 3:
Input: sequence = "ababc", word = "ac"
Output: 0
Explanation: "ac" is not a substring in "ababc".

Constraints:
    1 <= sequence.length <= 100
    1 <= word.length <= 100
    sequence and word contains only lowercase English letters.
"""


class Solution:
    """
    Bruteforce solution: create a concatenated sequence from word until we reached max num of k_repeat

    Runtime: 32 ms, faster than 53.47% of Python3
    Memory Usage: 14.4 MB, less than 12.48% of Python3

    Time complexity: O(n^2)
    Space complexity: O(1)
    """

    def maxRepeating(self, sequence: str, word: str) -> int:
        k_repeat = 0
        while word * k_repeat in sequence:
            k_repeat += 1
        return k_repeat - 1  # the last word doesn't fit in sequence so discarded


class Solution2:
    """
    Optimized first solution.
    We may have at most len(sequence)//len(word) repeats so it's worth to count top down

    Runtime depends on given input, but in worst case it's the same as first solution (e.g., no word in sequence).
    """

    def maxRepeating(self, sequence: str, word: str) -> int:
        k_repeat = len(sequence) // len(word)
        while word * k_repeat not in sequence and k_repeat > 0:
            k_repeat -= 1
        return k_repeat


if __name__ == '__main__':
    solutions = [Solution(), Solution2()]
    tc = (
        ("ababc", "ab", 2),
        ("ababc", "ba", 1),
        ("ababc", "ac", 0),
    )
    for sol in solutions:
        for inp_seq, inp_word, exp_k in tc:
            assert sol.maxRepeating(inp_seq, inp_word) == exp_k
