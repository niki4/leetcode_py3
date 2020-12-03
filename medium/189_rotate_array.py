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
from collections import deque
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


class Solution3:
    """
    Runtime: 48 ms, faster than 99.23% of Python3.
    Memory Usage: 15.5 MB, less than 34.77% of Python3.

    From python docs (https://wiki.python.org/moin/TimeComplexity):
    "A deque (double-ended queue) is represented internally as a doubly linked list.
    (Well, a list of arrays rather than objects, for greater efficiency.) Both ends are accessible,
    but even looking at the middle is slow, and adding to or removing from the middle is slower still."
        Time complexity for Pop/Append to both sides are O(1).
    """

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums: return
        shift = k % len(nums)
        nums_dq = deque(nums)
        nums_dq.rotate(shift)
        nums[:] = nums_dq


class Solution4:
    """
    Runtime: 52 ms, faster than 96.45% of Python3.
    Memory Usage: 15.6 MB, less than 8.83% of Python3.

    This approach is based on the fact that when we rotate the array k times,
    k elements from the back end of the array come to the front and the rest
    of the elements from the front shift backwards.

    Let n = 7 and k = 3.
    Original List                   : 1 2 3 4 5 6 7
    After reversing all numbers     : 7 6 5 4 3 2 1
    After reversing first k numbers : 5 6 7 4 3 2 1
    After revering last n-k numbers : 5 6 7 1 2 3 4 --> Result

    Time complexity: O(n)
    Space complexity: O(1)
    """

    def reverse(self, nums: List[int], start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        if not nums: return

        n = len(nums)
        k %= n  # shift size
        self.reverse(nums, 0, n - 1)  # reverse whole list
        self.reverse(nums, 0, k - 1)  # reverse first part back
        self.reverse(nums, k, n - 1)  # reverse second part back


if __name__ == '__main__':
    def get_test_cases():
        return [
            ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),
            ([-1, -100, 3, 99], 2, [3, 99, -1, -100]),
        ]


    solutions = [
        Solution(),
        Solution2(),
        Solution3(),
        Solution4(),
    ]
    for sol in solutions:
        for n, k, expected in get_test_cases():
            sol.rotate(n, k)
            assert n == expected, f'want {expected}, got {n}'
