"""
Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are
such that A[i] + B[j] + C[k] + D[l] is zero.

To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500.
All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.

Example:

Input:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

Output:
2

Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
"""
from collections import defaultdict

from typing import List


class Solution:
    """
    Runtime: 264 ms, faster than 86.36% of Python
    Memory Usage: 35 MB, less than 95.76% of Python3

    Time Complexity: O(n**2). We have 2 nested loops to count sums, and another 2 nested loops to find complements.
    Space Complexity: O(n**2) for the hashmap. There could be up to O(n**2) distinct a + b keys.
    """

    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        counter = 0
        mem = defaultdict(int)
        for a in A:
            for b in B:
                mem[a + b] += 1
        for c in C:
            for d in D:
                if -(c + d) in mem:
                    counter += mem[-(c + d)]  # so (a + b) - (c + d) == 0
        return counter


if __name__ == '__main__':
    solutions = [Solution()]
    tc = (
        ([1, 2], [-2, -1], [-1, 2], [0, 2], 2),
        ([-1, -1], [-1, 1], [-1, 1], [1, -1], 6),
    )
    for s in solutions:
        for a, b, c, d, exp in tc:
            res = s.fourSumCount(a, b, c, d)
            assert res == exp, f"want {exp}, got {res}"
