"""
There is a special keyboard with all keys in a single row.

Given a string keyboard of length 26 indicating the layout of the keyboard (indexed from 0 to 25), initially your finger
 is at index 0. To type a character, you have to move your finger to the index of the desired character. The time taken
 to move your finger from index i to index j is |i - j|.

You want to type a string word. Write a function to calculate how much time it takes to type it with one finger.

Example 1:
Input: keyboard = "abcdefghijklmnopqrstuvwxyz", word = "cba"
Output: 4
Explanation: The index moves from 0 to 2 to write 'c' then to 1 to write 'b' then to 0 again to write 'a'.
Total time = 2 + 1 + 1 = 4.

Example 2:
Input: keyboard = "pqrstuvwxyzabcdefghijklmno", word = "leetcode"
Output: 73

Constraints:
    keyboard.length == 26
    keyboard contains each English lowercase letter exactly once in some order.
    1 <= word.length <= 10^4
    word[i] is an English lowercase letter.
"""


class Solution:
    """
    Runtime: 48 ms, faster than 75.40% of Python3
    Memory Usage: 14.6 MB, less than 20.39% of Python3

    Time complexity: O(n) where n is the length of the "word"
    Space complexity: O(1) because len of keyboard/chars map is fixed to 26 eng letters
    """

    def calculateTime(self, keyboard: str, word: str) -> int:
        chars = {ch: i for i, ch in enumerate(keyboard)}
        prev_pos, move_sum = 0, 0

        for ch in word:
            move_sum += abs(chars[ch] - prev_pos)
            prev_pos = chars[ch]
        return move_sum


if __name__ == '__main__':
    solutions = [Solution()]
    tc = (
        ("abcdefghijklmnopqrstuvwxyz", "cba", 4),
        ("pqrstuvwxyzabcdefghijklmno", "leetcode", 73),
    )
    for s in solutions:
        for inp_keyboard, inp_word, exp in tc:
            res = s.calculateTime(inp_keyboard, inp_word)
            assert res == exp, f"{s.__class__.__name__}: expected {exp}, got {res}"
