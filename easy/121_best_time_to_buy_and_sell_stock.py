from typing import List


class Solution:
    """
    This solution works, but got 'Time Limit Exceeded' from Leetcode
    """

    def maxProfit(self, prices: list) -> int:
        max_profit = 0

        for idx in range(len(prices) - 1):
            current_val = prices[idx]
            max_val = max(prices[idx + 1:]) if prices[idx + 1:] else 0
            profit = max_val - current_val
            if profit > max_profit:
                max_profit = profit

        return max_profit


class Solution2:
    """
    Runtime: 60 ms
    Memory Usage: 14.2 MB

    Dynamic Programming.
    Time complexity: O(n)
    Space complexity: O(1)
    """

    def maxProfit(self, prices: list) -> int:
        max_profit, min_price = 0, float('inf')

        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)

        return max_profit


class Solution3:
    """
    Runtime: 68 ms, faster than 32.54% of Python3
    Memory Usage: 15.1 MB, less than 62.41% of Python3

    Dynamic Programming.
    Time complexity: O(n)
    Space complexity: O(1)
    """

    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy_price = prices[0] if prices else 0
        for i in range(1, len(prices)):
            max_profit = max(max_profit, prices[i] - buy_price)
            buy_price = min(buy_price, prices[i])
        return max_profit


if __name__ == "__main__":
    solutions = [Solution(), Solution2(), Solution3()]
    tc = (
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0),
        ([2, 4, 1], 2),
        ([1], 0),
    )
    for s in solutions:
        for inp, exp in tc:
            assert s.maxProfit(inp) == exp
