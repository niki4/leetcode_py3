"""
Today, the bookstore owner has a store open for customers.length minutes.  Every minute, some number of customers
(customers[i]) enter the store, and all those customers leave after the end of that minute.

On some minutes, the bookstore owner is grumpy.  If the bookstore owner is grumpy on the i-th minute, grumpy[i] = 1,
otherwise grumpy[i] = 0.  When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise
they are satisfied.

The bookstore owner knows a secret technique to keep themselves not grumpy for minutes minutes straight, but can only
use it once.

Return the maximum number of customers that can be satisfied throughout the day.

Example 1:
    Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3
    Output: 16
    Explanation: The bookstore owner keeps themselves not grumpy for the last 3 minutes.
    The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.

Note:
    1 <= minutes <= customers.length == grumpy.length <= 20000
    0 <= customers[i] <= 1000
    0 <= grumpy[i] <= 1
"""
from typing import List


class Solution:
    """
    TLE (Time Limit Exceeded)
    """

    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        satisfied = sum(customers[i] for i in range(len(grumpy)) if grumpy[i] == 0)
        max_satisfied = satisfied
        for i in range(minutes, len(customers) + 1):
            keep_calm = sum(customers[j] for j in range(i - minutes, i) if grumpy[j])
            max_satisfied = max(max_satisfied, satisfied + keep_calm)
        return max_satisfied


class Solution2:
    """
    The problem could be split into two subproblems:
    1.  count how many customers are already satisfied
    2.  find the maximum number who can be made satisfied by stopping the shop keeper from being grumpy for X time.

    Time complexity: O(n)
    Space complexity: O(1)
    """

    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        already_satisfied = 0
        # count already_satisfied, then discard them from further processing
        for i, customers_count in enumerate(customers):
            if not grumpy[i]:
                already_satisfied += customers[i]
                customers[i] = 0

        best_keep_calm, curr_keep_calm = 0, 0
        # use rolling sum approach to find the max sequence of unsatisfied customers
        for i, customers_count in enumerate(customers):
            curr_keep_calm += customers_count
            if i >= minutes:
                curr_keep_calm -= customers[i - minutes]
            best_keep_calm = max(best_keep_calm, curr_keep_calm)

        return already_satisfied + best_keep_calm


if __name__ == '__main__':
    solutions = [Solution(), Solution2()]
    tc = (
        ([1, 0, 1, 2, 1, 1, 7, 5], [0, 1, 0, 1, 0, 1, 0, 1], 3, 16),
    )
    for s in solutions:
        for inp_customers, inp_grumpy, inp_minutes, exp_satisfied in tc:
            assert s.maxSatisfied(inp_customers, inp_grumpy, inp_minutes) == exp_satisfied, f"{s.__class__.__name__}"
