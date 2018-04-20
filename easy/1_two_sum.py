"""
Given an array of integers, return indices of the two numbers such that
they add up to a specific target.

You may assume that each input would have exactly one solution, and you
may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

Status: Accepted (Your runtime beats 34.31 % of python3 submissions.)
Runtime: 2228 ms  (https://leetcode.com/submissions/detail/150705433/)
"""


class Solution:
    def twoSum(self, nums, target):
        """
        :param nums: List[int]
        :param target: int
        :return: List[int]
        """
        for num in nums:
            if any([
                    (target - num) in nums[nums.index(num)+1:],
                    (target - num) in nums[:nums.index(num)]]):
                    return [
                        nums.index(num),
                        [idx for idx, val in enumerate(nums) if (val == (target - num) and idx != nums.index(num))][0]
                    ]


if __name__ == '__main__':
    sol = Solution()
    print(sol.twoSum(nums=[2, 7, 11, 15], target=9))  # [0, 1]
    print(sol.twoSum(nums=[3, 2, 4], target=6)),      # [1, 2]
    print(sol.twoSum(nums=[3, 3], target=6))          # [0, 1]
    # assert sol.twoSum(nums=[2, 7, 11, 15], target=9) == [0, 1]
    # assert sol.twoSum(nums=[3, 2, 4], target=6) == [1, 2]
