"""
The count-and-say sequence is the sequence of integers with the first five
terms as following:
1.     1
2.     11
3.     21
4.     1211
5.     111221

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the
count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.
"""
import re


class Solution:
    """
    Runtime: 32 ms, faster than 98.43% of Python3
    Memory Usage: 13.1 MB, less than 78.72% of Python3.

    Algorithm idea: Use previous string value to generate a new one
    """

    def countAndSay(self, n: int) -> str:
        result = '1'
        for _ in range(n - 1):
            prev = result
            result = ''
            i = 0
            while i < len(prev):
                curr_digit = prev[i]
                count = 1
                i += 1
                while i < len(prev) and prev[i] == curr_digit:
                    count += 1
                    i += 1
                result += f'{count}{curr_digit}'
        return result


class Solution2:
    """
    Regexp pattern matching, where we find out all those repetitive groups of digits.

    Runtime: 48 ms, faster than 20.79% of Python3
    Memory Usage: 14.5 MB, less than 6.85% of Python3

    Time complexity: O(2**n) where n is the index of the desired seq.
    https://en.wikipedia.org/wiki/Time_complexity#Superpolynomial_time
    Space complexity: O(2**(n-1))
    """

    def countAndSay(self, n: int) -> str:
        curr_seq = '1'
        # match 0 to n repetitions digit
        pattern = r'((.)\2*)'  # outer brackets stands for group1, inner for group2

        for i in range(n - 1):
            next_seq = []
            for g1, g2 in re.findall(pattern, curr_seq):
                # append <count, digit> pair
                next_seq.append(str(len(g1)))
                next_seq.append(g2)
            # prepare next iteration
            curr_seq = ''.join(next_seq)
        return curr_seq


if __name__ == "__main__":
    solutions = [Solution(), Solution2()]
    tc = [
        (1, '1'),
        (2, '11'),
        (3, '21'),  # result means we seen 2 times of 1 on previous result (11)
        (4, '1211'),  # result means we seen 1 time of 2, then 1 time of 11 of previous result (21)
        (5, '111221'),  # on previous result (1211) we saw 1 - 1 time, then 2 also 1 time, then 1 - 2 times sequentially
        (6, '312211'),
        (7, '13112221'),
        (8, '1113213211'),
        (9, '31131211131221'),
        (10, '13211311123113112211'),
    ]
    for s in solutions:
        for inp, exp in tc:
            assert s.countAndSay(inp) == exp
