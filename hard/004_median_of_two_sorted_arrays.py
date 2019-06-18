"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:
nums1 = [1, 3]
nums2 = [2]
The median is 2.0

Example 2:
nums1 = [1, 2]
nums2 = [3, 4]
The median is (2 + 3)/2 = 2.5
"""

class Solution:
    """
    Runtime: 56 ms, faster than 88.08% of Python3.
    Memory Usage: 13.4 MB, less than 49.16% of Python3.
    """
    def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:
        src = sorted(nums1 + nums2)
        med_idx = len(src) // 2
        median = ((src[med_idx-1] + src[med_idx]) / 2) if len(src) % 2 == 0 else src[med_idx]
        return median


if __name__ == "__main__":
    s = Solution()
    assert s.findMedianSortedArrays([1, 3], [2]) == 2
    assert s.findMedianSortedArrays([1, 2], [3, 4]) == 2.5
