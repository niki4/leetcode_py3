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


class Solution2:
    """
    Runtime: 36 ms, faster than 66.29% of Python3
    Memory Usage: 14.3 MB, less than 18.71% of Python3
    """

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int):
        if not nums1 or not nums2:
            nums1[len(nums1):] = nums2
            return

        nums1_copy = nums1[:m]
        nums1.clear()
        i, j = 0, 0

        while i < m and j < n:
            if nums1_copy[i] < nums2[j]:
                nums1.append(nums1_copy[i])
                i += 1
            elif nums1_copy[i] > nums2[j]:
                nums1.append(nums2[j])
                j += 1
            else:  # equal
                nums1 += [nums1_copy[i], nums2[j]]  # += for list works as 'extend' method
                i += 1
                j += 1

        # check if any values left unmerged in either list
        if i == m:
            nums1 += nums2[j:]
        if j == n:  # len(nums2)
            nums1 += nums1_copy[i:]


if __name__ == '__main__':
    def get_tc():
        return (
            ([0], 1, [1], 1, [0, 1]),
            ([1], 1, [], 0, [1]),
            ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
            ([1, 2, 4, 5, 6, 0], 5, [3], 1, [1, 2, 3, 4, 5, 6])
        )


    solutions = [Solution(), Solution2()]
    for s in solutions:
        for in_nums1, in_m, in_nums2, in_n, expected in get_tc():
            s.merge(in_nums1, in_m, in_nums2, in_n)
            assert in_nums1 == expected, f'{s.__class__.__name__}: want {expected}, got {in_nums1}'
