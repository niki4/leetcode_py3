"""
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
You can return the answer in any order.

"""

import collections
import heapq
from typing import List


class Solution:
    """
    Algorithm: count, sort (keys by freq), filter k elements (slice)

    Runtime: 100 ms, faster than 74.36% of Python3
    Memory Usage: 18.6 MB, less than 92.20% of Python3

    Time complexity: O(n log n) due to sorting
    Space complexity: O(n)
    """

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ctr = collections.Counter(nums)
        return sorted(ctr, key=ctr.get, reverse=True)[:k]


class Solution2:
    """
    Algorithm: heapq (priority queue)

    Runtime: 92 ms, faster than 96.21% of Python3
    Memory Usage: 18.7 MB, less than 52.47% of Python3

    Time complexity: O(N log k)
    Space complexity: O(n)
    """

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):  # O(1). Special case to guarantee the rest code works not slower than O(N log k)
            return nums

        # O(N) - build hashmap with num as a key and its count as a value
        count = collections.Counter(nums)
        # O(N log k) - build heap of top k freq element, then convert
        # it into an output array.
        return heapq.nlargest(k, count.keys(), key=count.get)


class Solution3:
    """
    Algorithm: bucket sort (freq of the element is the index of the bucket where that element will be placed).

    Runtime: 100 ms, faster than 74.36% of Python3
    Memory Usage: 19.7 MB, less than 6.22% of Python3

    Time complexity: O(n)
    Space complexity: O(n)
    """

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums) + 1)]
        ctr = collections.Counter(nums)
        for n, count in ctr.items():
            bucket[count].append(n)
        flat_list = [item for sublist in bucket for item in sublist]
        return flat_list[-k:]


if __name__ == '__main__':
    solutions = [Solution(), Solution2(), Solution3()]
    tc = (
        ([1, 1, 1, 2, 2, 3], 2, [1, 2]),
        ([1], 1, [1]),
    )
    for s in solutions:
        for inp_nums, inp_k, exp in tc:
            res = s.topKFrequent(inp_nums, inp_k)
            assert sorted(res) == sorted(exp)
