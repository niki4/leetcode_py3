"""
Given an array nums, write a function to move all 0's to the end
of it while maintaining the relative order of the non-zero elements.

Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""
from typing import List


class Solution:
    """
    Runtime: 48 ms, faster than 86.25% of Python3.
    Memory Usage: 14.5 MB, less than 48.00% of Python3.
    """

    def moveZeroes(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_count = nums.count(0)
        zeroes = (0 for _ in range(zero_count))
        non_zeroes = [n for n in nums if n]
        nums.clear()
        nums.extend(non_zeroes)
        nums.extend(zeroes)


class Solution2:
    """
    Runtime: 36 ms, faster than 99.88% of Python3.
    Memory Usage: 14.4 MB, less than 70.66% of Python3.

    Iterating from the end of the list toward begin may reduce cost of rebuilding the array
    when we delete zero values from it whilst pushing zero right after we've removed it
    keeps indexing correct.

    Time complexity: O(n) for iteration over the list,
                     O(n-k) for deleting from the list where k is the position from the end,
                     O(1) for push zero to the end of the list
    Space complexity:O(1) as we are not creating new list, but modifying it in place
    """

    def moveZeroes(self, nums: list) -> None:
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == 0:
                del nums[i]
                nums.append(0)


class Solution3:
    """
    Two-pointer approach. Slow pointer points to zero so that we know when to swap it with non-zero element (fast ptr).

    Runtime: 40 ms, faster than 96.72% of Python3
    Memory Usage: 15.4 MB, less than 14.79% of Python3

    Time complexity: O(n)
    Space complexity: O(1)
    """

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1


if __name__ == "__main__":
    def get_tc():
        return [
            ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
            ([2, 1], [2, 1])
        ]


    solutions = [Solution(), Solution2(), Solution3()]
    for s in solutions:
        for inp, exp in get_tc():
            s.moveZeroes(inp)
            assert inp == exp, f'{s.__class__.__name__}: expected {exp}, got {inp}'
