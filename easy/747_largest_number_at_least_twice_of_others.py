"""
In a given integer array nums, there is always exactly one largest element.

Find whether the largest element in the array is at least twice as much as every other number in the array.

If it is, return the index of the largest element, otherwise return -1.

Example 1:
Input: nums = [3, 6, 1, 0]
Output: 1
Explanation: 6 is the largest integer, and for every other number in the array x,
6 is more than twice as big as x.  The index of value 6 is 1, so we return 1.

Example 2:
Input: nums = [1, 2, 3, 4]
Output: -1
Explanation: 4 isn't at least as big as twice the value of 3, so we return -1.

Note:
nums will have a length in the range [1, 50].
Every nums[i] will be an integer in the range [0, 99].
"""
from typing import List


class Solution:
    """
    Bruteforce approach

    Runtime: 36 ms, faster than 54.55% of Python3
    Memory Usage: 14.3 MB, less than 8.38% of Python3
    """

    def dominantIndex(self, nums: List[int]) -> int:
        if not nums:
            return -1
        if len(nums) == 1:
            return 0

        desc = sorted(nums, reverse=True)
        if desc[0] // 2 >= desc[1]:
            return nums.index(desc[0])
        return -1


class Solution2:
    """
    Optimized first solution so that we save some resources on search index of largest num.

    Runtime: 36 ms, faster than 54.55% of Python3
    Memory Usage: 14 MB, less than 77.60% of Python3

    Time complexity: O(NlogN) because of sorting
    Space complexity: O(N) to store sorted array
    """

    def dominantIndex(self, nums: List[int]) -> int:
        if not nums:
            return -1
        if len(nums) == 1:
            return 0

        desc = sorted(enumerate(nums), key=lambda x: x[1], reverse=True)
        if desc[0][1] // 2 >= desc[1][1]:
            return desc[0][0]
        return -1


class Solution3:
    """
    Single pass, no need to sort array.
    Keep track of first largest n (and its index) and second largest n to compare after array traverse.

    Runtime: 36 ms, faster than 54.55% of Python3
    Memory Usage: 14 MB, less than 96.07% of Python3

    Time complexity: O(N) to traverse list one time
    Space complexity: O(1), we only need to store 3 vars (constant size)
    """

    def dominantIndex(self, nums: List[int]) -> int:
        if not nums:
            return -1
        if len(nums) == 1:
            return 0

        first_max_n = nums[0]
        first_max_i = 0
        second_max_n = 0

        for i in range(1, len(nums)):
            if nums[i] > first_max_n:
                second_max_n = first_max_n
                first_max_n = nums[i]
                first_max_i = i
            elif nums[i] > second_max_n:
                second_max_n = nums[i]

        if first_max_n >= second_max_n * 2:
            return first_max_i
        return -1


if __name__ == '__main__':
    solutions = [Solution(), Solution2(), Solution3()]
    tc = [
        ([3, 6, 1, 0], 1),
        ([1, 2, 3, 4], -1),
        ([0, 0, 0, 1], 3),
        ([], -1),
        ([1, 0], 0)
    ]
    for s in solutions:
        for inp, exp in tc:
            assert s.dominantIndex(inp) == exp
