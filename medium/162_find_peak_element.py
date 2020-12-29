"""
A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its index.
If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Example 2:
Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2,
or index number 5 where the peak element is 6.

Constraints:
1 <= nums.length <= 1000
-231 <= nums[i] <= 231 - 1
nums[i] != nums[i + 1] for all valid i.

Follow up: Could you implement a solution with logarithmic complexity?
"""
from typing import List


class Solution:
    """
    Bruteforce solution.
    Algorithm idea: Peak's next element is lower (descent). Also there's special case when there only ascent, so the
    peak will be the last element in this case.

    Time complexity: O(n)
    """

    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                return i - 1
            elif nums[i] > nums[i - 1] and i == len(nums) - 1:
                return i


class Solution2:
    """
    Recursive Binary Search: "we keep on reducing the search space till we eventually reach a state where only one
    element is remaining in the search space. This single element is the peak element."

    Runtime: 48 ms, faster than 39.22% of Python3
    Memory Usage: 14.5 MB, less than 7.57% of Python3

    Time and Space complexity:  O(log2 (n)).  We reduce the search space in half at every step.
    Thus, the total search space will be consumed in log_2(n) steps.
    Here, n refers to the size of nums array, depth of recursion tree will go upto log_2(n).
    """

    def search(self, nums: List[int], left: int, right: int) -> int:
        if left == right:
            return left
        mid = (left + right) // 2
        if nums[mid] > nums[mid + 1]:
            return self.search(nums, left, mid)
        return self.search(nums, mid + 1, right)

    def findPeakElement(self, nums: List[int]) -> int:
        return self.search(nums, 0, len(nums) - 1)


class Solution3:
    """
    The same as Solution 2, but using closure function instead class method for the search helper.

    Runtime: 40 ms, faster than 90.22% of Python3
    Memory Usage: 14.6 MB, less than 7.57% of Python3
    """

    def findPeakElement(self, nums: List[int]) -> int:
        def search(left: int, right: int) -> int:
            if left == right:
                return left

            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                return search(left, mid)
            return search(mid + 1, right)

        return search(0, len(nums) - 1)


class Solution4:
    """
    Iterative Binary Search

    Runtime: 44 ms, faster than 71.24% of Python3
    Memory Usage: 14.4 MB, less than 56.78% of Python3

    Time complexity:  O(log2 (n))
    Space complexity: O(1)
    """

    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == '__main__':
    solutions = [Solution(), Solution2(), Solution3(), Solution4()]
    tc = (
        ([1, 2, 3, 1], [2]),
        ([1, 2, 1, 3, 5, 6, 4], [1, 5]),
        ([2, 1], [0]),
        ([6, 5, 4, 3, 2, 3, 2], [0, 5]),
    )
    for s in solutions:
        for inp, exp in tc:
            res = s.findPeakElement(inp)
            assert res in exp, f'{s.__class__.__name__}: for input {inp} found idx {res} not in expected {exp}'
