"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

Follow up:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?

Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Constraints:

1 <= nums.length <= 2 * 104
-231 <= nums[i] <= 231 - 1
0 <= k <= 105
"""
from typing import List


class Solution:
    """
    Runtime: 124 ms, faster than 17.15% of Python3
    Memory Usage: 15.3 MB, less than 11.01% of Python3

    Insert to the begin of the list (stack) is expensive for large sequences
    """

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        for _ in range(k):
            nums.insert(0, nums.pop())


class Solution2:
    """
    Another approach is to reduce the number of shifts by mod of len(nums) as we rotate cycled list.
    In other words, having len == 10 and k == 13 we can simply do 13%10=3 shifts instead of 13, with the same result.

    Runtime: 56 ms, faster than 88.43% of Python3
    Memory Usage: 15.4 MB, less than 11.01% of Python3
    """

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        shift = k % len(nums)
        # [:] operation replaces items in original list; but slicing is not free
        nums[:] = nums[-shift:] + nums[:-shift]


if __name__ == '__main__':
    def get_test_cases():
        return [
            ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),
            ([-1, -100, 3, 99], 2, [3, 99, -1, -100]),
        ]


    solutions = [
        Solution(),
        Solution2()
    ]

    for sol in solutions:
        for n, k, expected in get_test_cases():
            sol.rotate(n, k)
            assert n == expected, f'want {expected}, got {n}'
