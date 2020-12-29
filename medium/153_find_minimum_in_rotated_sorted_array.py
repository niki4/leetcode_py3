"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times.

For example, the array nums = [0,1,2,4,5,6,7] might become:
[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in
the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums, return the minimum element of this array.

Example 1:
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

Constraints:
n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
All the integers of nums are unique.
nums is sorted and rotated between 1 and n times.
"""
from typing import List


class Solution:
    """
    Bruteforce solution (we guaranteed in Constraints that there's at least one element, so no check for nums).

    Runtime: 40 ms, faster than 62.35% of Python3
    Memory Usage: 14.6 MB, less than 39.04% of Python3

    Time complexity: O(n)
    Space complexity: O(1)
    """

    def findMin(self, nums: List[int]) -> int:
        return min(nums)


class Solution2:
    """
    Binary search: in shifted array, lowest element is the first one after a continuous ascending sequence.

    Runtime: 44 ms, faster than 24.37% of Python3
    Memory Usage: 14.7 MB, less than 18.12% of Python3

    Time complexity: O(log n)
    Space complexity: O(1)
    """

    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        if nums[right] >= nums[0]:
            return nums[0]

        while right >= left:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid - 1] > nums[mid]:
                return nums[mid]

            if nums[mid] > nums[0]:
                left = mid + 1
            else:
                right = mid - 1


class Solution3:
    """
    Binary search. The same idea as in Solution2, but more concise code.
    Here we converge left and right borders toward the lowest element.

    Runtime: 40 ms, faster than 62.35% of Python3
    Memory Usage: 14.5 MB, less than 62.06% of Python3

    Time complexity: O(log n)
    Space complexity: O(1)
    """

    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        return nums[left]


if __name__ == '__main__':
    tc = (
        ([1], 1),
        ([3, 4, 5, 1, 2], 1),
        ([4, 5, 6, 7, 0, 1, 2], 0),
        ([11, 13, 15, 17], 11),
    )
    solutions = [Solution(), Solution2()]
    for s in solutions:
        for inp, exp in tc:
            res = s.findMin(inp)
            assert res == exp, f"{s.__class__.__name__}: for inp {inp} exp {exp}, got {res}"
