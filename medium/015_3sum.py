"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note:
The solution set must not contain duplicate triplets.

Example:
Given array nums = [-1, 0, 1, 2, -1, -4],
A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
from typing import List


class Solution:
    """
    Runtime: 1428 ms, faster than 21.17% of Python3.
    Memory Usage: 17.5 MB, less than 16.78% of Python3.

    Runtime: 2560 ms, faster than 5.04% of Python3.
    Memory Usage: 17.4 MB, less than 19.86% of Python3.

    k-sum that equal 0, where k is 3.
    """

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        def ksum(num, k, target):
            i = 0
            if k == 2:
                j = len(num) - 1
                while i < j:
                    if num[i] + num[j] == target:
                        yield num[i], num[j]
                        i += 1
                    elif num[i] + num[j] > target:
                        j -= 1
                    else:
                        i += 1
            else:
                while i < len(num) - k + 1:
                    new_target = target - num[i]
                    for sub in ksum(num[i + 1:], k - 1, new_target):
                        yield (num[i],) + sub
                    i += 1

        return [list(s_) for s_ in set(ksum(nums, 3, 0))]


class Solution2:
    """
    Runtime: 1132 ms, less than 33.53 % of python3.
    Memory Usage: 17.4 MB, less than 19.96 % of python3.

    Algorithm idea:
        The way to think about it is since it's 3 sum, there's only going to be 3 numbers.
        So to find the combinations of 3 numbers, we iterating through the list with
        the first pointer, and then trying to find two extra numbers to sum to 0.

        Since the list is ordered, the right pointer will always be higher than the
        middle pointer. So if the sum is too large, you can move the right pointer back one.
        On the other hand, if the sum is too small (below 0), then move the middle pointer up one.
    """

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums.sort()
        for i in range(len(nums) - 2):
            if nums[i] > 0:  # having sorted list there's no sense to continue once we reaches positive nums in list
                break
            if i > 0 and nums[i] == nums[i - 1]:  # optimization: skip duplicates (already tried)
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                elements = (nums[i], nums[l], nums[r])
                sum_elements = sum(elements)
                if sum_elements < 0:
                    l += 1
                elif sum_elements > 0:
                    r -= 1
                else:
                    result.add(elements)
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
        return [list(s) for s in result]


if __name__ == "__main__":
    solutions = [Solution(), Solution2()]
    src = [-1, 0, 1, 2, -1, -4]
    exp = [
        [-1, 0, 1],
        [-1, -1, 2]
    ]

    for s in solutions:
        assert sorted(s.threeSum(src)) == sorted(exp)
