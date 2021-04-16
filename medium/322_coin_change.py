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

    To better understand how this approach works I printed out state of each dp[x] on every iteration:
    In [96]: sol.coinChange([1, 2, 5], 11)
        coin: 1
        min(dp[1] = inf, dp[1 - 1] + 1 = 1)	dp[1] = 1
        min(dp[2] = inf, dp[2 - 1] + 1 = 2)	dp[2] = 2
        min(dp[3] = inf, dp[3 - 1] + 1 = 3)	dp[3] = 3
        min(dp[4] = inf, dp[4 - 1] + 1 = 4)	dp[4] = 4
        min(dp[5] = inf, dp[5 - 1] + 1 = 5)	dp[5] = 5
        min(dp[6] = inf, dp[6 - 1] + 1 = 6)	dp[6] = 6
        min(dp[7] = inf, dp[7 - 1] + 1 = 7)	dp[7] = 7
        min(dp[8] = inf, dp[8 - 1] + 1 = 8)	dp[8] = 8
        min(dp[9] = inf, dp[9 - 1] + 1 = 9)	dp[9] = 9
        min(dp[10] = inf, dp[10 - 1] + 1 = 10)	dp[10] = 10
        min(dp[11] = inf, dp[11 - 1] + 1 = 11)	dp[11] = 11     (we can make amount 11 by 11th coins of den. 1)
        coin: 2
        min(dp[2] = 2, dp[2 - 2] + 1 = 1)	dp[2] = 1
        min(dp[3] = 3, dp[3 - 2] + 1 = 2)	dp[3] = 2
        min(dp[4] = 4, dp[4 - 2] + 1 = 2)	dp[4] = 2
        min(dp[5] = 5, dp[5 - 2] + 1 = 3)	dp[5] = 3
        min(dp[6] = 6, dp[6 - 2] + 1 = 3)	dp[6] = 3
        min(dp[7] = 7, dp[7 - 2] + 1 = 4)	dp[7] = 4
        min(dp[8] = 8, dp[8 - 2] + 1 = 4)	dp[8] = 4
        min(dp[9] = 9, dp[9 - 2] + 1 = 5)	dp[9] = 5
        min(dp[10] = 10, dp[10 - 2] + 1 = 5)	dp[10] = 5
        min(dp[11] = 11, dp[11 - 2] + 1 = 6)	dp[11] = 6     (we can make amount 11 by comb. 5pc*2 + 1pc*1)
        coin: 5
        min(dp[5] = 3, dp[5 - 5] + 1 = 1)	dp[5] = 1
        min(dp[6] = 3, dp[6 - 5] + 1 = 2)	dp[6] = 2
        min(dp[7] = 4, dp[7 - 5] + 1 = 2)	dp[7] = 2
        min(dp[8] = 4, dp[8 - 5] + 1 = 3)	dp[8] = 3
        min(dp[9] = 5, dp[9 - 5] + 1 = 3)	dp[9] = 3
        min(dp[10] = 5, dp[10 - 5] + 1 = 2)	dp[10] = 2
        min(dp[11] = 6, dp[11 - 5] + 1 = 3)	dp[11] = 3     (we can make amount 11 by comb. 2pc*5 + 1pc*1) <- winner
    Out[96]: 3

    """

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            # calculate lowest amount of combinations of coins with curr (and prev if any) denomination
            for x in range(coin, amount + 1):
                dp[x] = min(
                    dp[x],  # prev denomination coin amount
                    dp[x - coin] + 1)  # curr denomination coin (1 pc) that could replace prev denomination coin amount
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
