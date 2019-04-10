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
    """

    @functools.lru_cache()
    def climbStairs(self, n: int) -> int:
        return self.climbStairs(n - 1) + self.climbStairs(n - 2) if n > 2 else 2 if n == 2 else 1


if __name__ == '__main__':
    sol = Solution()
    assert sol.climbStairs(2) == 2
    assert sol.climbStairs(3) == 3
    assert sol.climbStairs(5) == 8
    assert sol.climbStairs(28) == 514229
