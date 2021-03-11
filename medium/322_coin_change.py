"""
You are given coins of different denominations and a total amount of money amount. Write a function to compute the
fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any
combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1
"""
from typing import List


class Solution:
    """
    Algorithm: "Dynamic programming - Bottom up"
    For the iterative solution, we think in bottom-up manner.
    Before calculating F(i), we have to compute all minimum counts for amounts up to i.

    Runtime: 1124 ms, faster than 82.07% of Python3
    Memory Usage: 14.2 MB, less than 92.44% of Python3

    Time complexity:   O(S∗n). On each step the algorithm finds the next F(i) in nn iterations, where S1≤i≤S.
                       Therefore in total the iterations are S*nS∗n. Here S is the amount to change.
    Space complexity:  O(S). We use extra space for the memoization table.
    """

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1


if __name__ == '__main__':
    solutions = [Solution()]
    tc = (
        ([1, 2, 5], 11, 3),
        ([2], 3, -1),
        ([1], 0, 0),
        ([1], 1, 1),
        ([1], 2, 2),
        ([186, 419, 83, 408], 6249, 20),
    )
    for s in solutions:
        for inp_coins, inp_amount, exp_count in tc:
            assert s.coinChange(inp_coins, inp_amount) == exp_count
