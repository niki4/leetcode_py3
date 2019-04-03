"""
Given a sorted array nums, remove the duplicates in-place such that
each element appear only once and return the new length.

Do not allocate extra space for another array,
you must do this by modifying the input array in-place with O(1) extra memory.

Runtime: 60 ms (Your runtime beats 99.65 % of python3 submissions.)src
Note. An idiom nums[:] do not creates a new list and uses existing ones instead, so no extra memory overhead
"""


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # MEMORY ERROR :(
        # nums.sort()
        # for i in (x for x in nums if nums.count(x) > 1):
        #     while nums.count(i) > 1:
        #         nums.remove(i)
        # return nums

        nums[:] = set(nums)
        nums.sort()
        return len(nums)

if __name__ == '__main__':
    sol = Solution()
    print(sol.removeDuplicates([1, 1, 2, 1, 3, 1, 2, 4]))
