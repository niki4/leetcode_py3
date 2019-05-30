class Solution:
    """
    This solution works, but got 'Time Limit Exceeded' from Leetcode
    """
    def maxProfit(self, prices: list) -> int:
        max_profit = 0

        for idx in range(len(prices)-1):
            current_val = prices[idx]
            max_val = max(prices[idx+1:]) if prices[idx+1:] else 0
            profit = max_val - current_val
            if profit > max_profit:
                max_profit = profit

        return max_profit

class Solution2:
    """
    Runtime: 60 ms, faster than 15.56% of Python3.
    Memory Usage: 14.2 MB, less than 5.20% of Python3.

    Well, at least it accepted ;-)
    """
    def maxProfit(self, prices: list) -> int:
        max_profit, min_price = 0, float('inf')

        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)

        return max_profit


if __name__ == "__main__":
    s = Solution()
    s2 = Solution2()
    assert s.maxProfit([7,1,5,3,6,4]) == 5
    assert s.maxProfit([7,6,4,3,1]) == 0
    assert s.maxProfit([2,4,1]) == 2
    assert s.maxProfit([1]) == 0

    assert s2.maxProfit([7,1,5,3,6,4]) == 5
    assert s2.maxProfit([7,6,4,3,1]) == 0
    assert s2.maxProfit([2,4,1]) == 2
    assert s2.maxProfit([1]) == 0
