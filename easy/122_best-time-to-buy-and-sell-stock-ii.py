"""
Say you have an array prices for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
"""

class Solution:
    """
    Runtime: 64 ms, faster than 60.95% of Python3.
    Memory Usage: 15.1 MB, less than 7.32% of Python3.
    """
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                max_profit += prices[i] - prices[i-1]
        return max_profit

if __name__ == '__main__':
    test_data = [
    ([7,1,5,3,6,4], 7),
    ([1,2,3,4,5], 4),
    ([7,6,4,3,1], 0)
    ]
    sol = Solution()
    
    for case in test_data:
      input_, expected = case
      assert sol.maxProfit(input_) == expected
