"""
Given a string columnTitle that represents the column title as appear in an Excel sheet, return its corresponding column number.

For example:
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...

Constraints:
    1 <= columnTitle.length <= 7
    columnTitle consists only of uppercase English letters.
    columnTitle is in the range ["A", "FXSHRXW"].
"""
import string


class Solution:
    """
    Right-to-Left

    Algorithm idea: each position has its cost (current column number + num of further combinations after current pos).
    The lowest cost has rightmost position (e.g., given columnTitle "ZY" its "Y" which is 25th letter of alphabet).
    Each next position toward begin, apart its own position cost, also need take in mind possible number of combinations
    thus formula for num of variants from current pos: "curr_position * base**power" where base is alphabet size and
    power increases by 1 at each offset (started from 0).

    Thus for columnTitle "ZY" computations will be as below:
    column_num = 0
    # take rightmost position - "Y"
    column_num += 25 * (26 ** 0)      #  == 0 +  (25 * (1)) == 25th column
    # take next position toward begin "Z"
    column_num += 26 * (26 ** 1)      #  == 25 + (26 * (26)) == 25 + (676) == 701

    Runtime: 36 ms, faster than 37.48% of Python3
    Memory Usage: 14.3 MB, less than 43.74% of Python3

    Time complexity: O(n) where n is the number of characters in the input string.
    Space complexity: O(1) - even though we have an alphabet to index mapping, it is always constant.
    """

    def titleToNumber(self, columnTitle: str) -> int:
        ltr_to_pos = {ltr: i + 1 for i, ltr in enumerate(string.ascii_uppercase)}
        alphabet_size = len(string.ascii_uppercase)  # 26 for english alphabet
        column_num = 0

        chars_seq = 0
        for i in range(len(columnTitle) - 1, -1, -1):
            curr_pos = ltr_to_pos[columnTitle[i]]
            num_variants = curr_pos * (alphabet_size ** chars_seq)
            column_num += num_variants
            chars_seq += 1

        return column_num


class Solution2:
    """
    Left-to-Right

    Similarly to Right-to-Left approach, we can start from begin and move toward end increasing power of base on each
    iteration. E.g., with base 10 we'd split the num 1234 as below:
        1. "1" = 1
        2. "12" = (1 * 10) + 2 = 12
        3. "123" = (12 * 10) + 3 = 123
        4. "1234" = (123 * 10) + 4 = 1234
    So we just need to replace the base to num of letters in alphabet (26). E.g., for title "ZY" computation would be:
        1. "Z" = (0 * 26) + 26 = 26
        2. "ZY" = (26 * 26) + 25 = 701

    Runtime: 24 ms, faster than 96.82% of Python3
    Memory Usage: 14.1 MB, less than 72.48% of Python3

    Time complexity: O(n)
    Space complexity: O(1)
    """

    def titleToNumber(self, columnTitle: str) -> int:
        column_num = 0
        for i in range(len(columnTitle)):
            column_num *= 26
            column_num += ord(columnTitle[i]) - ord("A") + 1
        return column_num


if __name__ == '__main__':
    solutions = [Solution(), Solution2()]
    tc = (
        ("A", 1),
        ("AB", 28),
        ("ZY", 701),
        ("FXSHRXW", 2147483647),
    )
    for sol in solutions:
        for inp_column, exp_num in tc:
            assert sol.titleToNumber(inp_column) == exp_num
