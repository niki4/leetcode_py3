"""
Alice has n candies, where the ith candy is of type candyType[i]. Alice noticed that she started to gain weight,
so she visited a doctor. The doctor advised Alice to only eat n / 2 of the candies she has (n is always even).
Alice likes her candies very much, and she wants to eat the maximum number of different types of candies while still
following the doctor's advice.

Given the integer array candyType of length n, return the maximum number of different types of candies she can eat
if she only eats n / 2 of them.

Example 1:
Input: candyType = [1,1,2,2,3,3]
Output: 3
Explanation: Alice can only eat 6 / 2 = 3 candies. Since there are only 3 types, she can eat one of each type.
"""
from typing import List


class Solution:
    """
    Runtime: 804 ms, faster than 56.15% of Python3
    Memory Usage: 16.4 MB, less than 11.68% of Python3

    Time complexity: O(n) to make set
    Space complexity: O(n) at worst we have all the unique candies so set will take the same size as input list
    """

    def distributeCandies(self, candyType: List[int]) -> int:
        unique = set(candyType)
        half = len(candyType) // 2
        return half if len(unique) >= half else len(unique)


class Solution2:
    """
    Variation of first solution with early termination

    Runtime: 804 ms, faster than 56.15% of Python3
    Memory Usage: 16.4 MB, less than 38.32% of Python3
    """

    def distributeCandies(self, candyType: List[int]) -> int:
        half = len(candyType) // 2
        seen = set()

        for candy in candyType:
            if candy not in seen:
                seen.add(candy)
            if len(seen) >= half:
                return half
        return len(seen)


if __name__ == '__main__':
    solutions = [
        Solution(),
        Solution2(),
    ]
    tc = (
        ([1, 1, 2, 2, 3, 3], 3),
        ([1, 1, 2, 3], 2),
        ([6, 6, 6, 6], 1),  # A. can only eat 4 / 2 = 2 candies. Even though she can eat 2 candies, she only has 1 type.
    )
    for s in solutions:
        for inp_candies, exp in tc:
            res = s.distributeCandies(inp_candies)
            assert res == exp, f"{s.__class__.__name__}: for inp {inp_candies} exp {exp}, got {res}"
