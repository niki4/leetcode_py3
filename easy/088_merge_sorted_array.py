"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n)
to hold additional elements from nums2. The number of elements initialized in nums1
and nums2 are m and n respectively.

Do not return anything, modify nums1 in-place instead.
"""
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int):
        """
        Runtime: 36 ms, faster than 66.29% of Python3
        Memory Usage: 14.2 MB, less than 40.58% of Python3

        Time complexity: O((n+m)log(n+m)) because we first need to merge lists, and then sort result.
        """
        nums1[m:] = nums2  # shortcut of nums[:n]
        nums1.sort()


if __name__ == '__main__':
    def get_tc():
        return (
            ([0], 1, [1], 1, [0, 1]),
        )


    solutions = [Solution()]
    for s in solutions:
        for in_nums1, in_m, in_nums2, in_n, expected in get_tc():
            s.merge(in_nums1, in_m, in_nums2, in_n)
            assert in_nums1 == expected
