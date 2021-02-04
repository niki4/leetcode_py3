"""
Given two arrays, write a function to compute their intersection.
Note:
* Each element in the result must be unique.
* The result can be in any order.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
"""
from typing import List


class Solution:
    """
    Runtime: 32 ms, faster than 99.53% of Python3
    Memory Usage: 14.2 MB, less than 54.41% of Python3

    Using hash table/set here to extract distinct items, then their intersection.
    """

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1).intersection(nums2))  # actually, LC accept answer without converting type to list()
        # return list(set2 & set1)  # alternatively


class Solution2:
    """
    Runtime: 36 ms, faster than 97.48% of Python3
    Memory Usage: 14.3 MB, less than 54.41% of Python3

    Just for fun. I personally prefer the first solution.
    """

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1, nums2 = (nums1, set(nums2)) if len(nums1) <= len(nums2) else (nums2, set(nums1))
        unique_nums1 = dict.fromkeys(nums1)
        return [x for x in unique_nums1 if x in nums2]


if __name__ == "__main__":
    solutions = [Solution(), Solution2()]
    for s in solutions:
        assert sorted(s.intersection([1, 2, 2, 1], [2, 2])) == [2]
        assert sorted(s.intersection([4, 9, 5], [9, 4, 9, 8, 4])) == [4, 9]
