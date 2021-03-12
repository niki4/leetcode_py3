"""
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.


Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

Constraints:
    1 <= k <= nums.length <= 104
    -104 <= nums[i] <= 104
"""
import heapq
from typing import List


class Solution:
    """
    Sort array, then take k-th element (-1 because input starting from 1)

    Time complexity: O(n logN) because of sorting
    Space complexity: O(n) to store sorted array
    """

    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = sorted(nums, reverse=True)
        return nums[k - 1]


class Solution2:
    """
    Heap queue

    Runtime: 60 ms, faster than 88.37% of Python3
    Memory Usage: 15.2 MB, less than 18.76% of Python3

    Time complexity: O(N logK). The time complexity of adding an element in a heap of size K is O(logK), and we do it
    N times that means (N logK) time complexity for the algorithm.
    Space complexity: O(k) to store the heap elements.
    """

    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]


if __name__ == '__main__':
    solutions = [Solution(), Solution2()]
    tc = (
        ([3, 2, 1, 5, 6, 4], 2, 5),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4)
    )
    for s in solutions:
        for inp_nums, inp_k, exp in tc:
            assert s.findKthLargest(inp_nums, inp_k) == exp
