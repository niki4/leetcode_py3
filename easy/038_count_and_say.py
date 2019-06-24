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

Example 1:
    Input: 1
    Output: "1"

Example 2:
    Input: 4
    Output: "1211"
"""

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
                curr = prev[i]
                count = 1
                i += 1
                while i < len(prev) and prev[i] == curr:
                    count += 1
                    i += 1
                result += str(count) + str(curr)
        return result


if __name__ == "__main__":
    s = Solution()
    assert s.countAndSay(1) == '1'
    assert s.countAndSay(2) == '11'
    assert s.countAndSay(3) == '21'  # result means we seen 2 times of 1 on previous result (11)
    assert s.countAndSay(4) == '1211' # result means we seen 1 time of 2, then 1 time of 11 of previous result (21)
    assert s.countAndSay(5) == '111221' # on previous result (1211) we seen 1 - 1 time, then 2 also 1 time, then 1 - 2 times sequentially
    assert s.countAndSay(6) == '312211'
    assert s.countAndSay(7) == '13112221'
    assert s.countAndSay(8) == '1113213211'
    assert s.countAndSay(9) == '31131211131221'
    assert s.countAndSay(10) == '13211311123113112211'
