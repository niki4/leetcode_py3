"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and
it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of
money you can rob tonight without alerting the police.

Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
"""
from typing import List


class Solution:
    """
    Dynamic Programming

    Runtime: 28 ms, faster than 84.87% of Python3
    Memory Usage: 14.1 MB, less than 73.00% of Python3
    Time complexity: O(n)
    Space complexity: O(n) as we need extra space for our 'dp' list
    """

    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        # base cases (first & second home)
        dp = [nums[0], max(nums[0], nums[1])]

        for i in range(2, len(nums)):
            """
            At house i, we could rob it or not rub it.
            If we rob house i (current house), we know that our previously robbed house would be i - 2 since
            we can not rob adjacent house
            If we do not rob house i (current house), we know that our previously robbed house would be i - 1 since
            the same reason above.
            
            so the current accumulated sum at house i will be the max 
            of the two cases described above except if we rob, make sure
            we add the money in current house first before comparing so,
            if rob, the money will become: dp[i-2] + nums[i]
            if not rob, the money will become: dp[i-1] or simply last element dp[-1] which holds robbed money so far.
            dp[i] holds robbed so far
            """
            dp.append(max(dp[i - 2] + nums[i], dp[-1]))
        # Similar to Kadane's algorithm (see 053_maximum_subarray) max profit will be set in the last item
        return dp[-1]


class Solution2:
    """
    Dynamic programming. Optimized first solution.
    Runtime: 24 ms, faster than 95.78% of Python3
    Memory Usage: 14.2 MB, less than 47.35% of Python3
    Time complexity: O(n)
    Space complexity: O(1)

    Algorithm idea:
     Let us look at the case n = 1, clearly f(1) = A1.
     Now, let us look at n = 2, which f(2) = max(A1, A2).
        For n = 3, you have basically the following two options:
         Rob the third house, and add its amount to the first house's amount.
         Do not rob the third house, and stick with the maximum amount of the first two houses.
         Clearly, you would want to choose the larger of the two options at each step.
         Therefore, we could summarize the formula as following:
         f(k) = max(f(k – 2) + Ak, f(k – 1))
    The answer will be calculated as f(n). We could use an array to store and calculate the result,
    but since at each step you only need the previous two maximum values, two variables are suffice.
    """

    def rob(self, nums: List[int]) -> int:
        prev_max, curr_max = 0, 0
        for n in nums:
            tmp = curr_max
            curr_max = max(
                prev_max + n,  # rob house, add robbed value to the accumulator
                curr_max)  # do not rob house more profitable, use accumulator val
            prev_max = tmp
        return curr_max


if __name__ == '__main__':
    solutions = [Solution(), Solution2()]
    tc = (
        ([1, 2, 3, 1], 4),
        ([2, 7, 9, 3, 1], 12),
        ([2, 1, 1, 2], 4),
        ([1, 3, 1, 3, 100], 103)
    )
    for s in solutions:
        for inp, exp in tc:
            res = s.rob(inp)
            assert res == exp, f'{s.__class__.__name__}: For input {inp} expected result {exp}, got: {res}'
