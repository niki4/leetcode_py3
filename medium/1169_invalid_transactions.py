"""
A transaction is possibly invalid if:
-    the amount exceeds $1000, or;
-    if it occurs within (and including) 60 minutes of another transaction with the same name in a different city.

You are given an array of strings transaction where transactions[i] consists of comma-separated values representing the
name, time (in minutes), amount, and city of the transaction.

Return a list of transactions that are possibly invalid. You may return the answer in any order.

Example 1:
Input: transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
Output: ["alice,20,800,mtv","alice,50,100,beijing"]
Explanation: The first transaction is invalid because the second transaction occurs within a difference of 60 minutes,
have the same name and is in a different city. Similarly the second one is invalid too.

Example 2:
Input: transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
Output: ["alice,50,1200,mtv"]

Example 3:
Input: transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
Output: ["bob,50,1200,mtv"]
"""
from typing import List


class Solution:
    """
    Probably, most downvoted problem on LC due to its ambiguous/vague description and a number of corner cases.

    Runtime: 148 ms, faster than 44.76% of Python3
    Memory Usage: 14.7 MB, less than 91.39% of Python3

    Time complexity: O(n^2) as we need to compare at worst all possible pairs of transactions
    Space complexity: O(n) - in worst case all transactions are invalid
    """

    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        invalid = list()
        for i, first in enumerate(transactions):
            name1, time1, amount1, city1 = first.split(",")
            time1 = int(time1)
            if int(amount1) > 1000:
                invalid.append(first)
                continue
            for j, second in enumerate(transactions):
                name2, time2, amount2, city2 = second.split(",")
                time2 = int(time2)
                if i != j and name1 == name2 and abs(time1 - time2) <= 60 and city1 != city2:
                    invalid.append(first)
                    break
        return invalid


if __name__ == '__main__':
    solutions = [Solution()]
    tc = (
        (["alice,20,1220,mtv", "alice,20,1220,mtv"], ["alice,20,1220,mtv", "alice,20,1220,mtv"]),
        (["alice,20,800,mtv", "alice,50,100,beijing"], ["alice,20,800,mtv", "alice,50,100,beijing"]),
        (["alice,20,800,mtv", "alice,50,1200,mtv"], ["alice,50,1200,mtv"]),
        (["alice,20,800,mtv", "bob,50,1200,mtv"], ["bob,50,1200,mtv"]),
        (["alice,20,800,mtv", "alice,50,100,mtv", "alice,51,100,frankfurt"],
         ["alice,20,800,mtv", "alice,50,100,mtv", "alice,51,100,frankfurt"]),
        (["bob,689,1910,barcelona", "bob,832,1726,barcelona", "bob,820,596,bangkok", "bob,175,221,amsterdam"],
         ["bob,689,1910,barcelona", "bob,832,1726,barcelona", "bob,820,596,bangkok"]),
    )
    for sol in solutions:
        for inp_tr, exp_res in tc:
            result = sol.invalidTransactions(inp_tr)
            assert sorted(result) == sorted(exp_res), f"actual {sorted(result)} != {sorted(exp_res)} expected"
