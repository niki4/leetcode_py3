"""
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
"""

class Solution:
    """
    Runtime: 56 ms, faster than 32.52% of Python3.
    Memory Usage: 13.1 MB, less than 74.01% of Python3.
    """
    def intersect(self, nums1: list, nums2: list) -> list:
        result = []
        for num in set(nums1).intersection(nums2):
            result += [num] * min(nums1.count(num), nums2.count(num))
        return result

if __name__ == "__main__":
    s = Solution()
    assert sorted(s.intersect([1,2,2,1], [2,2])) == sorted([2,2])
    assert sorted(s.intersect([4,9,5], [9,4,9,8,4])) == sorted([4,9])
