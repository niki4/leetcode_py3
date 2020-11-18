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

    Time and Space complexity: O(n)
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


if __name__ == '__main__':
    solutions = [Solution(), Solution2()]
    tc = [
        ("cc", -1),
        ("", -1),
        ("leetcode", 0),
        ("loveleetcode", 2),
    ]
    for s in solutions:
        for inp, exp in tc:
            assert s.firstUniqChar(inp) == exp
