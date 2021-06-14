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

    Time complexity: O(n^2)
    Space complexity: O(M+N), the maximum size of the answer.
                      M and N are the lengths of firstList and secondList respectively.
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


class Solution2:
    """
    Merge Intervals

    Intuition:
        "In an interval [a, b], call b the "endpoint".
        Among the given intervals, consider the interval A[0] with the smallest endpoint. (Without loss of generality,
        this interval occurs in array A.)

        Then, among the intervals in array B, A[0] can only intersect one such interval in array B. (If two intervals
        in B intersect A[0], then they both share the endpoint of A[0] -- but intervals in B are disjoint (meaning
        not intersecting each other), which is a contradiction.)

    Algorithm:
        If A[0] has the smallest endpoint, it can only intersect B[0]. After, we can discard A[0] since it cannot
        intersect anything else.

        Similarly, if B[0] has the smallest endpoint, it can only intersect A[0], and we can discard B[0] after since
        it cannot intersect anything else.

        We use two pointers, i and j, to virtually manage "discarding" A[0] or B[0] repeatedly."


    Runtime: 156 ms, faster than 33.39% of Python
    Memory Usage: 15.1 MB, less than 34.14% of Python3

    Time Complexity: O(M + N), where M and N are the lengths of firstList and secondList respectively.
    Space complexity: O(M+N), the maximum size of the answer.
    """

    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        intersections = []
        i = j = 0
        while i < len(firstList) and j < len(secondList):
            low = max(firstList[i][0], secondList[j][0])  # start point of intersection (rightmost of two starts)
            high = min(firstList[i][1], secondList[j][1])  # end point (leftmost of two ends)
            if low <= high:  # firstList[i] intersects secondList[j]
                intersections.append([low, high])

            # "remove" the interval with smallest endpoint
            if firstList[i][1] <= secondList[j][1]:
                i += 1
            else:
                j += 1
        return intersections


if __name__ == '__main__':
    solutions = [Solution(), Solution2()]
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
