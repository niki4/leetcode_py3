"""
Given two arrays, write a function to compute their intersection.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]

Note: Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
"""
from collections import Counter
from typing import List


class Solution:
    """
    Runtime: 56 ms, faster than 32.52% of Python3.
    Memory Usage: 13.1 MB, less than 74.01% of Python3.

    Simplest way is to use sets (hash tables) and built-in methods.
    """

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for num in set(nums1).intersection(nums2):
            result += [num] * min(nums1.count(num), nums2.count(num))
        return result


class Solution2:
    """
    Runtime: 76 ms, faster than 15.98% of Python3
    Memory Usage: 14.1 MB, less than 72.14% of Python3

    Using dict to track items and their count in smallest list.
    To save some space we'd use smallest array to store the result (I using a separate list though).
    """

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        primer_counter = dict()
        primer, test = (nums1, nums2) if len(nums1) < len(nums2) else (nums2, nums1)
        result = list()

        for n in primer:
            if n in primer_counter:
                primer_counter[n] += 1
            else:
                primer_counter[n] = 1
        for n in test:
            if n in primer and primer_counter[n] > 0:
                result.append(n)
                primer_counter[n] -= 1
        return result


class Solution3:
    """
    The same idea as Solution2, but more clear and concise syntax using Counter from "collections" lib.

    Runtime: 40 ms, faster than 96.08% of Python3
    Memory Usage: 14.6 MB, less than 10.88% of Python3
    """

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1ctr, nums2ctr = Counter(nums1), Counter(nums2)
        result = list()
        for n in nums1ctr:
            if n in nums2ctr:
                result += [n] * min(nums1ctr[n], nums2ctr[n])
        return result


class Solution4:
    """
    Runtime: 48 ms, faster than 56.92% of Python3
    Memory Usage: 14.3 MB, less than 51.86% of Python3

    Two pointers approach.
    Assuming both list are sorted, we may skip smallest from two different items.

    Time complexity: O(NlogN) + O(MlogM) where N and M are lengths of two arrays.
    Space complexity: O(logN + logM) to O(N + M) depending on sorting algorithm.
    """

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        result = list()

        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                result.append(nums1[i])
                i += 1
                j += 1
        return result


if __name__ == "__main__":
    solutions = [Solution(), Solution2(), Solution3(), Solution4()]
    for s in solutions:
        assert sorted(s.intersect([1, 2, 2, 1], [2, 2])) == sorted([2, 2])
        assert sorted(s.intersect([4, 9, 5], [9, 4, 9, 8, 4])) == sorted([4, 9])
