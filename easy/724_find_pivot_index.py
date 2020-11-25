"""
Given an array of integers nums, write a method that returns the "pivot" index of this array.

We define the pivot index as the index where the sum of all the numbers to the left of the index
is equal to the sum of all the numbers to the right of the index.

If no such index exists, we should return -1. If there are multiple pivot indexes, you should return
the left-most pivot index.

Example 1:
Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation: The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the sum of numbers to the right of index 3.
Also, 3 is the first index where this occurs.
"""
from typing import List


class Solution:
    """
    Bruteforce solution. Slicing is expensive: ~O(2*n/2) for n times so we have O(n**2)

    Runtime: 8476 ms, faster than 11.25% of Python3
    Memory Usage: 15.4 MB, less than 6.66% of Python3
    """

    def pivotIndex(self, nums: List[int]) -> int:
        if not nums:
            return -1
        if len(nums) == 1:
            return nums[0]

        for i in range(len(nums)):
            if sum(nums[:i]) == sum(nums[i + 1:]):
                return i
        return -1


class Solution2:
    """
    Runtime: 152 ms, faster than 41.80% of Python3
    Memory Usage: 15.3 MB, less than 23.78% of Python3

    Another solution is to calculate sum (of right part) once
    and then amend int of left/right sums whilst iterating over array.
    """

    def pivotIndex(self, nums: List[int]) -> int:
        if not nums:
            return -1
        if len(nums) == 1:
            return nums[0]

        left_sum = 0
        right_sum = sum(nums[1:])
        for i in range(len(nums)):
            if left_sum == right_sum:
                return i
            # print(nums, f'\t nums[{i}] = {nums[i]}', '\t\t', left_sum, right_sum)
            left_sum += nums[i]
            right_sum -= nums[i + 1] if i < len(nums) - 1 else 0
        return -1


if __name__ == '__main__':
    solutions = [Solution(), Solution2()]
    tc = [
        ([1, 7, 3, 6, 5, 6], 3),
        ([1, 2, 3], -1),
        ([], -1),
        ([1], 1),
        ([-1, -1, -1, 0, 1, 1], 0),
        ([-1, -1, 0, 1, 1, 0], 5),
    ]
    for s in solutions:
        for inp, exp in tc:
            res = s.pivotIndex(inp)
            assert res == exp, f'for input {inp} want result {exp}, got: {res}'
