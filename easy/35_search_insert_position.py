"""
Given a sorted array and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:
Input: [1,3,5,6], 5
Output: 2

Example 2:
Input: [1,3,5,6], 2
Output: 1

Status: Accepted (Your runtime beats 51.69 % of python3 submissions.) TODO: Could be improved
Runtime: 44ms (https://leetcode.com/submissions/detail/150560398/)
"""


class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        else:
            if target > max(nums):
                return len(nums)
            elif target < min(nums):
                return 0 if nums.index(min(nums)) == 0 else nums.index(min(nums))-1
            elif min(nums) < target < max(nums):
                if target-1 in nums:
                    return nums.index(target-1) + 1
                elif target+1 in nums:
                    return 0 if nums.index(target+1) == 0 else nums.index(target+1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.searchInsert([1, 3, 5, 6], 5))  # expected 2
    print(sol.searchInsert([1, 3, 5, 6], 2))  # expected 1
    print(sol.searchInsert([1, 3, 5, 6], 7))  # expected 4

    print(sol.searchInsert([1, 3, 5, 6], 0))      # expected 0
    print(sol.searchInsert([2, 3, 4, 8, 10], 0))  # expected 0
    print(sol.searchInsert([3, 4, 5, 8, 10], 2))  # expected 0

    print(sol.searchInsert([3, 6, 7, 8, 10], 5))  # expected 1

    print(sol.searchInsert([2, 3, 4, 7, 8, 9], 11))  # expected 6
