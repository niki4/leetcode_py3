"""
Given an integer array nums where every element appears three times except for one, which appears exactly once.
Find the single element and return it.

Example 1:
Input: nums = [2,2,3,2]
Output: 3

Example 2:
Input: nums = [0,1,0,1,0,1,99]
Output: 99

Constraints:
1 <= nums.length <= 3 * 104
-231 <= nums[i] <= 231 - 1
Each element in nums appears exactly three times except for one element which appears once.

Follow up: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""
from collections import Counter

from typing import List


class Solution:
    """
    Counter approach.

    Runtime: 48 ms, faster than 96.58% of Python3
    Memory Usage: 16.1 MB, less than 45.11% of Python3

    Time complexity: O(n) for iteration over nums, O(n logN) for sorting
    Space complexity: O(n) to hold values in counter

    counter = {0: 3, 1: 3, 99: 1}
    In [241]: timeit sorted(counter, key=lambda k: counter[k])[0]
        476 ns ± 2.09 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
    In [242]: timeit sorted(counter, key=counter.get)[0]
        350 ns ± 5.59 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
    """

    def singleNumber(self, nums: List[int]) -> int:
        counter = dict()
        for n in nums:
            if n in counter:
                counter[n] += 1
            else:
                counter[n] = 1
        # sort dict keys by value; return first (which has smallest count)
        return sorted(counter, key=lambda k: counter[k])[0]  # alt.: key=counter.get


class Solution2:
    """
    Using Counter type from collections lib.
    Other optimisation is simple linear scan for finding element that appears only once,
    so that it takes O(n) vs O(n logN) if we'd sorted dict by values.

    Runtime: 52 ms, faster than 90.26% of Python3
    Memory Usage: 16.2 MB, less than 29.11% of Python3
    """

    def singleNumber(self, nums: List[int]) -> int:
        counter = Counter(nums)
        for k in counter:
            if counter[k] == 1:
                return k


class Solution3:
    """
    Algorithm idea: make 'ideal' list where all nums appears 3 time, calculate sum of all elements from that list,
    then subtract from this sum another sum of given input list. As given input array has one num missed we get double
    (3-1=2) sum of desired num, so the last operation will be to divide it by half.
    e.g.,
    3×(a+b+c)−(a+a+a+b+b+b+c)=2c

    Runtime: 52 ms, faster than 90.26% of Python3
    Memory Usage: 16 MB, less than 45.11% of Python3

    Time complexity : O(N) to iterate over the input array.
    Space complexity : O(N) to keep the set of N/3 elements.
    """

    def singleNumber(self, nums: List[int]) -> int:
        return (sum(set(nums)) * 3 - sum(nums)) // 2


class Solution4:
    """
     O(1) space solution by using three bitwise operators
    ∼x    that means bitwise NOT
    x&y   that means bitwise AND
    x⊕y   that means bitwise XOR

    Runtime: 52 ms, faster than 90.26% of Python3
    Memory Usage: 15.7 MB, less than 88.79% of Python3

    Time complexity : O(N) to iterate over the input array.
    Space complexity : O(1) since no additional data structures are allocated.
    """

    def singleNumber(self, nums: List[int]) -> int:
        seen_once = seen_twice = 0
        for n in nums:
            """
            first appearance:
                add num to seen_once
                don't add to seen_twice because of presence in seen_once
            second appearance:
                remove num from seen_once
                add num to seen_twice
            third appearance:
                don't add to seen_once because of presence in see_twice
                remove num from seen_twice
            """
            seen_once = ~seen_twice & (seen_once ^ n)
            seen_twice = ~seen_once & (seen_twice ^ n)
        return seen_once


if __name__ == '__main__':
    solutions = [Solution(), Solution2(), Solution3(), Solution4()]
    tc = (
        ([2, 2, 3, 2], 3),
        ([0, 1, 0, 1, 0, 1, 99], 99),
    )
    for s in solutions:
        for inp, exp in tc:
            assert s.singleNumber(inp) == exp
