"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous
subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no
such subarray, return 0 instead.

Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0

Constraints:
    1 <= target <= 109
    1 <= nums.length <= 105
    1 <= nums[i] <= 105

Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity
is O(n log(n)).
"""

from typing import List


class Solution:
    """
    Time Limit Exceeded (TLE).
    """

    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        min_len = len(nums)
        sum_found = False

        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                subarray_sum = sum(nums[i:j])
                subarray_len = j - i
                if subarray_sum >= s:
                    sum_found = True
                    min_len = min(subarray_len, min_len)

        return min_len if sum_found else 0


class Solution2:
    """
    Another TLE. Trying to put two-pointer approach.
    Works ok on small arrays. LC fails on long array (with len 33168).

    Time complexity: O(n**3) - two cycles plus sum calculation on each subarray
    """

    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        i, k = 0, 0
        min_len = None
        while i < len(nums):
            k = i
            while k < len(nums):
                if sum(nums[i:k + 1]) >= s:
                    min_len = min((k + 1) - i, min_len) if min_len is not None else (k + 1) - i
                    break
                k += 1
            i += 1

        return min_len or 0


class Solution3:
    """
    LC proposed solution (ported from C++). Also got TLE, LOL :)

    Algorithm idea:
        In 1st/2nd solution sum is calculated for every subarray in O(n) time.
        But, we could easily find the sum in O(1) time by storing the cumulative sum from the beginning(Memoization).
        After we have stored the cumulative sum in sums, we could easily find the sum of any subarray from i to j.
    Time complexity: O(n**2)
    """

    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        len_n = len(nums)
        if len_n == 0 or len_n == 1:
            return len_n

        int32max = (1 << 31)
        ans = int32max
        sums = list()
        sums.append(nums[0])

        for i in range(1, len_n):
            sums.append(sums[i - 1] + nums[i])
        for i in range(len_n):
            for j in range(i, len_n):
                subarray_sum = sums[j] - sums[i] + nums[i]
                if subarray_sum >= s:
                    ans = min(ans, (j - i + 1))
                    # found the smallest subarray with sum >= s starting with current index i, move to the next index i.
                    break

        return ans if ans != int32max else 0


class Solution4:
    """
    Algorithm: scan from left to right, 'total' tracks the sum of the subarray.
    If the sum is less than s, right moves forward one step, else left moves forward one step.
    Left (tail) and right (head) form a window.

    Runtime: 72 ms, faster than 67.25% of Python3
    Memory Usage: 16.7 MB, less than 28.44% of Python3

    Time complexity: O(n)
    """

    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        total = left = right = 0
        res = len(nums) + 1  # found seq will never exceed that
        while right < len(nums):
            total += nums[right]
            while total >= s:
                res = min(res, right - left + 1)
                total -= nums[left]
                left += 1
            right += 1
        return res if res <= len(nums) else 0


if __name__ == '__main__':
    tc = [
        (11, [1, 2, 3, 4, 5], 3),
        (7, [2, 3, 1, 2, 4, 3], 2),
    ]
    solutions = [Solution(), Solution2(), Solution3(), Solution4()]
    for sol in solutions:
        for inp_s, inp_nums, expected in tc:
            assert sol.minSubArrayLen(inp_s, inp_nums) == expected
