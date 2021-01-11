"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2

Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
"""

import functools


class Solution:
    """
    Runtime: 36 ms, faster than 73.18% of Python3.
    Memory Usage: 13.2 MB, less than 5.18% of Python3.
    Timeit: 95.3 ns ± 0.489 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)
    """

    @functools.lru_cache()
    def climbStairs(self, n: int) -> int:
        return self.climbStairs(n - 1) + self.climbStairs(n - 2) if n > 2 else 2 if n == 2 else 1


class Solution2:
    """
    Actually, similar approach to the Solution one, but with regular dict instead lru_cache().
    LC stat is floating run-to-run so I've added `%timeit climbStairs(10)` comparison result as well.
    
    Runtime: 24 ms
    Memory Usage: 14.1 MB
    Timeit: 2.48 µs ± 27.6 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
    """

    def climbStairs(self, n: int) -> int:
        cache = {2: 2, 1: 1}

        def climb_rec(N):
            if N in cache:
                return cache[N]
            res = climb_rec(N - 1) + climb_rec(N - 2)
            cache[N] = res
            return res

        return climb_rec(n)


if __name__ == '__main__':
    solutions = [Solution(), Solution2()]
    for sol in solutions:
        assert sol.climbStairs(2) == 2
        assert sol.climbStairs(3) == 3
        assert sol.climbStairs(5) == 8
        assert sol.climbStairs(28) == 514229
