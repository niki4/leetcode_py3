"""
Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and
is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces
' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide
evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

Note:
-    A word is defined as a character sequence consisting of non-space characters only.
-    Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
-    The input array words contains at least one word.

Example 1:
Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

Constraints:
    1 <= words.length <= 300
    1 <= words[i].length <= 20
    words[i] consists of only English letters and symbols.
    1 <= maxWidth <= 100
    words[i].length <= maxWidth
"""
from typing import List


class Solution:
    """
    Greedy approach: we first collate as many words as possible per each future string, then calculate needed spaces so
    that string will match with the maxWidth, then build that justified strings.

    Runtime: 32 ms, faster than 62.61% of Python3
    Memory Usage: 14.3 MB, less than 51.54% of Python3
    """

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        rows, result = [], []
        words = words[::-1]
        while words:
            row = []
            while words and (sum(len(word) for word in row) + len(words[-1]) + len(row)) <= maxWidth:
                row.append(words.pop())
            rows.append(row)

        for i in range(len(rows)):
            if i < len(rows) - 1 and len(rows[i]) > 1:
                chars_len = sum(len(word) for word in rows[i])
                spaces_len = maxWidth - chars_len
                gap_size, carry = divmod(spaces_len, len(rows[i]) - 1)
                justified_line = rows[i][0]
                for j in range(1, len(rows[i])):
                    justified_line += (" " * gap_size) + (" " if carry > 0 else "") + rows[i][j]
                    carry -= 1
            else:  # the last line of text, should be left justified and no extra space is inserted between words.
                justified_line = " ".join(rows[i]).ljust(maxWidth)
            result.append(justified_line)
        return result


if __name__ == '__main__':
    solutions = [Solution()]
    tc = (
        (["This", "is", "an", "example", "of", "text", "justification."], 16, [
            "This    is    an",
            "example  of text",
            "justification.  "
        ]),
        (["What", "must", "be", "acknowledgment", "shall", "be"], 16, [
            "What   must   be",
            "acknowledgment  ",
            "shall be        "
        ]),
        (["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.", "Art",
          "is", "everything", "else", "we", "do"], 20, [
             "Science  is  what we",
             "understand      well",
             "enough to explain to",
             "a  computer.  Art is",
             "everything  else  we",
             "do                  "
         ]),
    )
    for sol in solutions:
        for inp_words, inp_max_width, exp_result in tc:
            justify_result = sol.fullJustify(inp_words, inp_max_width)
            assert justify_result == exp_result
