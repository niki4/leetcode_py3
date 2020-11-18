"""
Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

Examples:
s = "leetcode" -> return 0.
s = "loveleetcode" -> return 2.

Note: You may assume the string contains only lowercase English letters.
"""
from collections import Counter


class Solution:
    """
    Bruteforce solution.  Time Limit Exceeded.

    For the len(long_str) == 23779 we got timings:
        timeit sol.firstUniqChar(long_str)
        723 ms ± 503 µs per loop (mean ± std. dev. of 7 runs, 1 loop each)
    """

    def firstUniqChar(self, s: str) -> int:
        if not s:
            return -1
        char = min(s, key=lambda x: s.count(x))
        if s.count(char) > 1:
            return -1
        return s.index(char)


class Solution2:
    """
    Using hashmap to track&count idx's for each ltr.

    This approach significantly speeds up the process (albeit in cost of using additional memory for storing dict):
        timeit sol2.firstUniqChar(long_str)
        3.64 ms ± 5.17 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)

    Runtime: 124 ms, faster than 49.50% of Python3
    Memory Usage: 15.6 MB, less than 5.54% of Python3
    Time: O(n)
    Space complexity: O(1) because we may have at most O(26) keys eq to english alphabet.
    """

    def firstUniqChar(self, s: str) -> int:
        if not s:
            return -1
        counter = dict()

        for idx, char in enumerate(s):
            if char in counter:
                counter[char].append(idx)
            else:
                counter[char] = [idx]

        min_count_char = min(counter, key=lambda k: len(counter[k]))
        if len(counter[min_count_char]) > 1:
            return -1

        return counter[min_count_char][0]


class Solution3:
    """
    Runtime: 64 ms, faster than 95.05% of Python3
    Memory Usage: 14.4 MB, less than 18.25% of Python3
    """

    def firstUniqChar(self, s: str) -> int:
        if not s: return -1
        ch_ctr = Counter(s)  # makes pairs like Counter({'p': 946, 'u': 972})
        min_ch = min(ch_ctr, key=ch_ctr.get)
        return s.index(min_ch) if ch_ctr[min_ch] == 1 else -1


if __name__ == '__main__':
    solutions = [Solution(), Solution2(), Solution3()]
    tc = [
        ("cc", -1),
        ("", -1),
        ("leetcode", 0),
        ("loveleetcode", 2),
    ]
    for s in solutions:
        for inp, exp in tc:
            assert s.firstUniqChar(inp) == exp
