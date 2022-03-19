"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

Input: nums = [1,2,3], k = 3
Output: 2
Explanation: there's possible to make 2 combinations that sums to 3: [1, 2] and [3]

Constraints:
    1 <= nums.length <= 2 * 104
    -1000 <= nums[i] <= 1000
    -107 <= k <= 107
"""

from collections import defaultdict
from typing import List

class Solution:
    """
    Running sum approach (https://en.wikipedia.org/wiki/Running_total)

    Time complexity: O(n)
    Space complexity: O(n)
    """
    def subarraySum(self, nums: List[int], k: int) -> int:
        s_sum = 0
        sum_count = defaultdict(int)
        count = 0  # number of subarrays whose sum equals to k

        for n in nums:
            s_sum += n
            count += (s_sum == k) + sum_count[s_sum-k]
            sum_count[s_sum] += 1

        return count


if __name__ == '__main__':
    solutions = [Solution()]
    tc = (
        ([1,1,1], 2, 2),
        ([1,2,3], 3, 2),
    )

    for sol in solutions:
        for inp_nums, inp_k, exp in tc:
            assert sol.subarraySum(inp_nums, inp_k) == exp
