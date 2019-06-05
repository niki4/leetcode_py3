"""
We are to write the letters of a given string S, from left to right into lines.
Each line has maximum width 100 units, and if writing a letter would cause
the width of the line to exceed 100 units, it is written on the next line.
We are given an array widths, an array where widths[0] is the width of 'a',
widths[1] is the width of 'b', ..., and widths[25] is the width of 'z'.

Now answer two questions: how many lines have at least one character from S,
and what is the width used by the last such line?
Return your answer as an integer list of length 2.

Example :
Input:
widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
S = "abcdefghijklmnopqrstuvwxyz"
Output: [3, 60]
Explanation:
All letters have the same length of 10. To write all 26 letters,
we need two full lines and one line with 60 units.
"""
from string import ascii_lowercase


class Solution:
    """
    Runtime: 32 ms, faster than 96.40% of Python3.
    Memory Usage: 13.1 MB, less than 81.30% of Python3.
    """
    def numberOfLines(self, widths: list, S: str) -> list:
        ltrs_cost = {ltr: widths[idx] for (idx, ltr) in enumerate(ascii_lowercase)}
        lines_count = line_sum = 0
        for ltr in S:
            if (line_sum + ltrs_cost[ltr]) <= 100:
                line_sum += ltrs_cost[ltr]
            else:
                lines_count += 1
                line_sum = ltrs_cost[ltr]

        num_of_lines = lines_count + 1 if line_sum else lines_count
        return [num_of_lines, line_sum]


if __name__ == "__main__":
    s = Solution()
    widths_1 = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
    widths_2 = [4, 10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
    S_1 = "abcdefghijklmnopqrstuvwxyz"
    S_2 = "bbbcccdddaaa"
    assert s.numberOfLines(widths_1, S_1) == [3, 60]
    assert s.numberOfLines(widths_2, S_2) == [2, 4]
