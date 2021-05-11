"""
Given an array of positive integers arr, calculate the sum of all possible odd-length subarrays.
A subarray is a contiguous subsequence of the array.
Return the sum of all odd-length subarrays of arr.

Example 1:
Input: arr = [1,4,2,5,3]
Output: 58
Explanation: The odd-length subarrays of arr and their sums are:
    [1] = 1
    [4] = 4
    [2] = 2
    [5] = 5
    [3] = 3
    [1,4,2] = 7
    [4,2,5] = 11
    [2,5,3] = 10
    [1,4,2,5,3] = 15
    If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58
"""
from typing import List


class Solution:
    """
    Runtime: 68 ms, faster than 52.92% of Python3
    Memory Usage: 14.3 MB, less than 49.04%
    """

    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        window_size = 1
        sum_odd_subarr = 0
        while window_size <= len(arr):
            for i in range(window_size, len(arr) + 1):
                sum_odd_subarr += sum(arr[i - window_size:i])
            window_size += 2
        return sum_odd_subarr


if __name__ == '__main__':
    solutions = [Solution()]
    tc = (
        ([1, 4, 2, 5, 3], 58),
        ([1, 2], 3),
        ([10, 11, 12], 66),
    )
    for sol in solutions:
        for inp_arr, exp_sum in tc:
            assert sol.sumOddLengthSubarrays(inp_arr) == exp_sum
