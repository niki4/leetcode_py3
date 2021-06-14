"""
You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [STARTi, ENDi] and
secondList[j] = [STARTj, ENDj]. Each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

A closed interval [a, b] (with a < b) denotes the set of real numbers x with a <= x <= b.

The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed
interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].

Example 1:
https://assets.leetcode.com/uploads/2019/01/30/interval1.png
Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
"""
from typing import List


class Solution:
    """
    Bruteforce approach (combine and compare all possible pairs of intervals from both lists)

    Runtime: 2316 ms, faster than 5.15% of Python3
    Memory Usage: 15.1 MB, less than 56.44% of Python3
    """

    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        intersections = []
        for first_interval in firstList:
            for second_interval in secondList:
                first, second = sorted([first_interval, second_interval])
                if second[0] <= first[1]:  # second interval started before first ends, so there's overlap
                    intersections.append(
                        [second[0], min(first[1], second[1])])
        return intersections


if __name__ == '__main__':
    solutions = [Solution()]
    tc = (([[0, 2], [5, 10], [13, 23], [24, 25]],
           [[1, 5], [8, 12], [15, 24], [25, 26]],
           [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]),
          ([[1, 3], [5, 9]], [], []),
          ([], [[4, 8], [10, 12]], []),
          ([[1, 7]], [[3, 10]], [[3, 7]]),
          ([[3, 5], [9, 20]],
           [[4, 5], [7, 10], [11, 12], [14, 15], [16, 20]],
           [[4, 5], [9, 10], [11, 12], [14, 15], [16, 20]]))
    for sol in solutions:
        for first_list, second_list, expected_intersections in tc:
            result = sol.intervalIntersection(first_list, second_list)
            assert result == expected_intersections, f"{sol.__class__.__name__}: {result} != {expected_intersections}"
