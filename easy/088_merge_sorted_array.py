"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n)
to hold additional elements from nums2. The number of elements initialized in nums1
and nums2 are m and n respectively.

Runtime: 36 ms (Your runtime beats 100.00 % of python3 submissions.)
Status: Accepted  https://leetcode.com/submissions/detail/149848422/
"""

class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2  # shortcut of nums[:n]
        nums1.sort()

        print(nums1)
        print(nums2)

if __name__ == '__main__':
    sol = Solution()
    sol.merge([0], 0, [1], 1)
