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
from typing import List


class Solution:
    """
    Runtime: 2228 ms  (https://leetcode.com/submissions/detail/150705433/)
    Status: Accepted (Your runtime beats 34.31 % of python3 submissions.)

    This pretty inefficient solution as we excessively making slices with complexity O(k) for each operation, also
    besides main other loop "for num in nums" which takes O(n) we have at each iteration linear scan in slice O(n) to
    find element value and another operation to find the index.

    To sum up, we have O(n**3 + k) Time Complexity here
    Space complexity is O(n) as we need space for temporary storage
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for num in nums:
            if any([(target - num) in nums[nums.index(num) + 1:], (target - num) in nums[:nums.index(num)]]):
                return [
                    nums.index(num),
                    [idx for idx, val in enumerate(nums) if (val == (target - num) and idx != nums.index(num))][0]
                ]


class Solution2:
    """
    Bruteforce approach (compare all combinations to find sum that makes a target)

    Time complexity: O(n**2)
    Space complexity: O(1)
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


class Solution3:
    """
    Runtime: 36 ms, faster than 99.34% of Python3.
    Memory Usage: 14.9 MB, less than 5.08% of Python3.

    Time complexity: O(n) for linear scan and O(1) for get/set key to hash map (dict)
    Space complexity: O(n) for storing values in a hash map
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        buffer = {}
        for i in range(len(nums)):
            curr = nums[i]
            if curr in buffer:
                return [buffer[curr], i]
            else:
                buffer[target - curr] = i


class Solution4:
    """
    Slightly optimized second solution (one-pass hash table approach).

    Runtime: 44 ms, faster than 85.73% of Python3
    Memory Usage: 14.4 MB, less than 47.64% of Python3

    Time complexity: O(n)
    Space complexity: O(n)
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = dict()
        for i, n in enumerate(nums):
            if (target - n) in pairs:
                return [pairs[(target - n)], i]
            pairs[n] = i


if __name__ == '__main__':
    solutions = [Solution(), Solution2(), Solution3(), Solution4()]
    cases = (
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([0, 4, 3, 0], 0, [0, 3]),
    )
    for s in solutions:
        for in_nums, in_target, exp in cases:
            res = s.twoSum(in_nums, in_target)
            assert res == exp, f"{s.__class__.__name__}: for input {in_nums},{in_target} expected {exp}, got {res}"
