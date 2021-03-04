"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color
are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
"""
import collections
from typing import List


class Solution:
    """
    Simplest (and pythonic) way

    Runtime: 28 ms, faster than 92.67% of Python3
    Memory Usage: 14.1 MB, less than 91.95% of Python3

    Time complexity: O(n logN)
    Space complexity: O(1)
    """

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()


class Solution2:
    """
    Count sort: Rebuild list in place using counters of elements

    Runtime: 32 ms, faster than 77.82% of Python3
    Memory Usage: 14.3 MB, less than 14.25% of Python3

    Time complexity: O(2n)
    """

    def sortColors(self, nums: List[int]) -> None:
        counter = collections.Counter(nums)
        nums[:] = [0] * counter[0] + [1] * counter[1] + [2] * counter[2]


class Solution3:
    """
    Dijkstra's https://en.wikipedia.org/wiki/Dutch_national_flag_problem
    Algorithm idea: we divide the whole list in three parts:
            (0, low-1)              contain 0
            (low, high)             contain 1
            (high+1, len(nums)-1)   contain 2

    Runtime: 32 ms, faster than 77.82% of Python3
    Memory Usage: 14.2 MB, less than 48.32% of Python3

    Time complexity: O(n)
    Space complexity: O(1)
    """

    def sortColors(self, nums: List[int]) -> None:
        low = index = 0
        high = len(nums) - 1

        while index <= high:
            if nums[index] == 0:  # move 0's to begin of list
                nums[low], nums[index] = nums[index], nums[low]
                low += 1
                index += 1
            elif nums[index] == 2:  # move 2's to end of list
                nums[high], nums[index] = nums[index], nums[high]
                high -= 1
            else:  # nums[index] == 1  # no move need for 1's, they between low and high
                index += 1


if __name__ == '__main__':
    def get_tc():
        return (
            ([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]),
            ([2, 0, 1], [0, 1, 2]),
            ([0], [0]),
            ([1], [1]),
        )


    solutions = [Solution(), Solution2(), Solution3()]
    for s in solutions:
        for inp, exp in get_tc():
            s.sortColors(inp)
            assert inp == exp
