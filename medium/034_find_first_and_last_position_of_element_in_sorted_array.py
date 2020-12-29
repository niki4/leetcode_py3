"""
Given an array of integers nums sorted in ascending order, 
find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1].

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Runtime: 40 ms, faster than 81.34% of Python3.
Memory Usage: 13.9 MB, less than 5.06% of Python3.
"""
from typing import List


class Solution:
    """
    Binary search

    Runtime: 84 ms, faster than 65.92% of Python3
    Memory Usage: 15.3 MB, less than 54.98% of Python3

    Time complexity: O(log n)
    """

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                L, R = mid, mid
                while L >= low and nums[L] == target:
                    L -= 1
                while R <= high and nums[R] == target:
                    R += 1
                return [L + 1, R - 1]
            if nums[low] <= target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return [-1, -1]


class Solution2:
    """
    Linear search

    Runtime: 84 ms, faster than 65.92% of Python3
    Memory Usage: 15.4 MB, less than 34.65% of Python3

    Time complexity: O(2n) as we have to traverse list twice, this turns to O(n) because 2 is constant.
    """

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [-1, -1]
        for i in range(len(nums)):
            if nums[i] == target:
                result[0] = i
                break
        if result[0] != -1:
            for j in range(len(nums) - 1, result[0] - 1, -1):
                if nums[j] == target:
                    result[1] = j
                    break
        return result


class Solution3:
    """
    Linear search

    Runtime: 84 ms, faster than 65.92% of Python3
    Memory Usage: 15.5 MB, less than 34.65% of Python3

    Time complexity: O(n)
    """

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [-1, -1]
        for i in range(len(nums)):
            if nums[i] == target:
                if result[0] == -1:
                    result[:] = [i, i]
                else:
                    result[1] = i
        return result


if __name__ == '__main__':
    solutions = [Solution(), Solution2(), Solution3()]
    tc = (
        ([5, 7, 7, 8, 8, 10], 8, [3, 4]),
        ([5, 7, 7, 8, 8, 10], 6, [-1, -1]),
        ([1], 1, [0, 0]),
        ([1, 2, 3], 3, [2, 2]),
    )
    for s in solutions:
        for inp, trg, exp in tc:
            res = s.searchRange(inp, trg)
            assert res == exp, f'{s.__class__.__name__}: for inp {inp} with trg {trg}: exp {exp}, got {res}'
