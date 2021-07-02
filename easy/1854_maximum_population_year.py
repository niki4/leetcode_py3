"""
You are given a 2D integer array logs where each logs[i] = [birth-i, death-i] indicates the birth and death years of the
i-th person.

The population of some year x is the number of people alive during that year. The ith person is counted in year x's
population if x is in the inclusive range [birth-i, death-i - 1]. Note that the person is not counted in the year that
they die.

Return the earliest year with the maximum population.

Example 1:
Input: logs = [[1993,1999],[2000,2010]]
Output: 1993
Explanation: The maximum population is 1, and 1993 is the earliest year with this population.

Example 2:
Input: logs = [[1950,1961],[1960,1971],[1970,1981]]
Output: 1960
Explanation:
The maximum population is 2, and it had happened in years 1960 and 1970.
The earlier year between them is 1960.

Constraints:
    1 <= logs.length <= 100
    1950 <= birthi < deathi <= 2050
"""

import collections
from typing import List


class Solution:
    """
    Use counter to calculate population at each year in the ranges. Then calculate year(s) with the max population.
    Finally return earliest year with the max_population.

    Runtime: 44 ms, faster than 65.89% of Python3
    Memory Usage: 14.4 MB, less than 36.81% of Python3
    """

    def maximumPopulation(self, logs: List[List[int]]) -> int:
        ctr = collections.Counter()
        for birth_year, death_year in logs:
            ctr.update(range(birth_year, death_year))

        max_population = max(ctr.values())
        return sorted(year for year, population in ctr.items() if population == max_population)[0]


if __name__ == '__main__':
    solutions = [Solution()]
    tc = (
        ([[1993, 1999], [2000, 2010]], 1993),
        ([[1950, 1961], [1960, 1971], [1970, 1981]], 1960),
    )
    for sol in solutions:
        for inp_logs, exp_year in tc:
            assert sol.maximumPopulation(inp_logs) == exp_year
