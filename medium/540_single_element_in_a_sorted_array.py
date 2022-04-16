"""
You are given a sorted array consisting of only integers where every element appears exactly twice,
except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.

Example 1:
Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2

Example 2:
Input: nums = [3,3,7,7,10,11,11]
Output: 10

Constraints:
1 <= nums.length <= 105
0 <= nums[i] <= 105
"""

from typing import List


class Solution:
    """
    Time complexity: O(N). Best if you have unsorted array.
    Space complexity: O(1)

    Runtime: 198 ms, faster than 70.56% of Python3
    Memory Usage: 23.6 MB, less than 91.44% of Python3
    """
    def singleNonDuplicate(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res ^= n  # XOR 'eats' duplicates, so that e.g. 123 ^ 123 == 0
        return res


class Solution2:
    """
    Time complexity: O(log N) because of binary search
    Space complexity: O(1)

    Every 2 numbers are partners. (even,odd), (even,odd).
    If mid is even, it's partner is next odd (right), if mid is odd, it's partner is previous even (left).
    """
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left + right) // 2
            pair = mid - 1 if mid % 2 else mid + 1

            if nums[mid] == nums[pair]:
                left = mid + 1
            else:
                right = mid

        return nums[left]


if __name__ == '__main__':
    solutions = [
        Solution(),
        Solution2(),
        ]
    tc = (
        ([1,1,2,3,3,4,4,8,8], 2),
        ([3,3,7,7,10,11,11], 10),
    )
    for sol in solutions:
        for inp_nums, exp_dup in tc:
            assert sol.singleNonDuplicate(inp_nums) == exp_dup
