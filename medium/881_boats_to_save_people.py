"""
You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where
each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum
of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.

Example 1:
    Input: people = [1,2], limit = 3
    Output: 1
    Explanation: 1 boat (1, 2)

Example 2:
    Input: people = [3,2,2,1], limit = 3
    Output: 3
    Explanation: 3 boats (1, 2), (2) and (3)

Example 3:
    Input: people = [3,5,3,4], limit = 5
    Output: 4
    Explanation: 4 boats (3), (3), (4), (5)

Constraints:
    1 <= people.length <= 5 * 104
    1 <= people[i] <= limit <= 3 * 104
"""
from typing import List


class Solution:
    """
    Greedy approach

    Time complexity: O(N logN) because of sorting. Traversing the people list will take O(n).
    Space complexity: O(N) because we creating a copy of sorted list
    """

    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        i, j = 0, len(people) - 1
        boats = 0

        while i <= j:
            boats += 1  # at least one people will always board (heavier first)
            if people[i] + people[j] <= limit:  # lighter person fits, onboard both
                i += 1
            j -= 1
        return boats


if __name__ == '__main__':
    solutions = [Solution()]
    tc = (
        ([1, 2], 3, 1),
        ([3, 2, 2, 1], 3, 3),
        ([3, 5, 3, 4], 5, 4),
    )
    for sol in solutions:
        for inp_people, inp_limit, exp_boats in tc:
            assert sol.numRescueBoats(inp_people, inp_limit) == exp_boats
