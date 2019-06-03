"""
Given a List of words, return the words that can be typed
using letters of alphabet on only one row's of American
keyboard like the image below.

Example:
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]

Note:
You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.
"""
import re


class Solution:
    """
    Runtime: 24 ms, faster than 99.93% of Python3.
    Memory Usage: 13 MB, less than 90.27% of Python3.
    """
    def findWords(self, words: list) -> list:
        us_keyboard_rows = [
            ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
            ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'],
            ['Z', 'X', 'C', 'V', 'B', 'N', 'M'],
        ]
        one_row_words = []
        for row in us_keyboard_rows:
            for word in words:
                if all([(ltr in row) for ltr in word.upper()]):
                    one_row_words.append(word)
        return one_row_words

class Solution2:
    """
    Runtime: 32 ms, faster than 95.55% of Python3.
    Memory Usage: 13.2 MB, less than 46.01% of Python3.
    """
    def findWords(self, words: list) -> list:
        rows = re.compile('(?i)([qwertyuiop]*|[asdfghjkl]*|[zxcvbnm]*)$')  # (?i) means 'case insensitive'
        return list(filter(rows.match, words))


if __name__ == "__main__":
    s = Solution()
    s2 = Solution2()
    input_src = ["Hello", "Alaska", "Dad", "Peace"]
    expected = ['Alaska', 'Dad']
    assert sorted(s.findWords(input_src)) == sorted(expected)
    assert sorted(s2.findWords(input_src)) == sorted(expected)
