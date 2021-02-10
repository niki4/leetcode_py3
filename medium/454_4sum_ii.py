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
import collections
import itertools

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
        mem = collections.defaultdict(int)
        for a in A:
            for b in B:
                mem[a + b] += 1
        for c in C:
            for d in D:
                if -(c + d) in mem:
                    counter += mem[-(c + d)]  # so (a + b) - (c + d) == 0
        return counter


class Solution2:
    """
    This design allows to handle more than 4 lists of nums.
    Above, we divided 4 arrays into two equal groups, and processed each group independently.
    Same way, we will divide k arrays into two groups. For the first group, we will have k/2 nested loops to count sums.
    Another k/2 nested loops will enumerate arrays in the second group and search for complements.

    Time Complexity:  O(n ** (k/2)), or O(n**2) for 4Sum II.
                      We have k/2 nested loops to count sums, and another k/2 nested loops to find complements.
                      For odd size arrays, time complexity is O(n ** (k+1)/2)
    Space complexity: O(n ** (k/2)) for the hashmap.
    """

    def kSumCount(self, nums: List[List[int]]):
        k = len(nums)
        hashes = nums[:k // 2]  # arrays to be hashed
        iters = nums[k // 2:]  # arrays to be iterated over

        #  product(A, B) returns the same as:  ((x,y) for x in A for y in B).
        ctr = collections.Counter([sum(group) for group in itertools.product(*hashes)])
        iters_sum = [sum(group) for group in itertools.product(*iters)]

        res = 0
        for val in iters_sum:
            complement = 0 - val
            res += ctr.get(complement, 0)
        return res

    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        return self.kSumCount([A, B, C, D])


class Solution3:
    """
     collections.Counter returns 0 if no given key exists. We may utilize it and apply pattern from the above listed
     solutions ((a + b) + (-c - d) == 0) in a nicely looking 2-liner.

     Runtime: 264 ms, faster than 86.36% of Python3
     Memory Usage: 35 MB, less than 85.20% of Python3

     Time Complexity:  O(n**2).
     Space complexity: O(n ** (k/2)) for the hashmap.
    """

    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        ab_sum = collections.Counter(a + b for a in A for b in B)
        return sum(ab_sum[-c - d] for c in C for d in D)


if __name__ == '__main__':
    solutions = [Solution(), Solution2(), Solution3()]
    tc = (
        ([1, 2], [-2, -1], [-1, 2], [0, 2], 2),
        ([-1, -1], [-1, 1], [-1, 1], [1, -1], 6),
    )
    for s in solutions:
        for a_, b_, c_, d_, exp in tc:
            res = s.fourSumCount(a_, b_, c_, d_)
            assert res == exp, f"want {exp}, got {res}"
