"""
Given an array of integers, return indices of the two numbers such that
they add up to a specific target.

You may assume that each input would have exactly one solution, and you
may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


class Solution:
    """
    Runtime: 2228 ms  (https://leetcode.com/submissions/detail/150705433/)
    Status: Accepted (Your runtime beats 34.31 % of python3 submissions.)
    """
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

    """
    Runtime: 36 ms, faster than 99.34% of Python3.
    Memory Usage: 14.9 MB, less than 5.08% of Python3.
    """
    def twoSum2(self, nums, target: int):
        buffer = {}
        for i in range(len(nums)):
            curr = nums[i]
            if curr in buffer:
                return [buffer[curr], i]
            else:
                buffer[target - curr] = i


if __name__ == '__main__':
    s = Solution()
    ts = s.twoSum
    ts2 = s.twoSum2
    cases = (
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4],      6, [1, 2]),
        ([3, 3],         6, [0, 1]),
        ([3, 2, 4],      6, [1, 2]),
        ([0, 4, 3, 0],   0, [0, 3]),
    )
    for case in cases:
        nums, target, expected = case
        assert ts(nums, target) == expected
        assert ts2(nums, target) == expected
