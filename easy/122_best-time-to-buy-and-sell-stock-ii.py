"""
Say you have an array prices for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit.
You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Example 1:
Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
"""
from typing import List


class Solution:
    """
    The solution comes from "Solution 2" (below).
    Instead of looking for every peak following a valley, we can simply go on crawling over the slope and keep on
    adding the profit obtained from every consecutive transaction.

    This would save us few bytes on keeping track of valley and peak (and few lines of code too).

    Runtime: 64 ms, faster than 60.95% of Python3.
    Memory Usage: 15.1 MB, less than 7.32% of Python3.
    """

    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
        return max_profit


class Solution2:
    """
    Peak Valley Approach.

    The idea is to find all segments from lower point (a valley) to the top (a peak).
    The max profit is the sum of differences between valleys and peaks.

    Runtime: 64 ms, faster than 36.46% of Python3
    Memory Usage: 14.9 MB, less than 100.00% of Python3
    """

    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        max_profit, i = 0, 0

        while i < len(prices) - 1:
            while i < len(prices) - 1 and prices[i] >= prices[i + 1]:  # descending to start
                i += 1
            valley = prices[i]
            while i < len(prices) - 1 and prices[i] <= prices[i + 1]:  # ascending to end
                i += 1
            peak = prices[i]
            max_profit += peak - valley

        return max_profit


if __name__ == '__main__':
    test_data = [
        ([7, 1, 5, 3, 6, 4], 7),
        ([1, 2, 3, 4, 5], 4),
        ([7, 6, 4, 3, 1], 0)
    ]
    sol = Solution()
    sol2 = Solution2()

    for case in test_data:
        input_, expected = case
        assert sol.maxProfit(input_) == expected
        assert sol2.maxProfit(input_) == expected
