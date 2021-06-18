"""
There is an integer array nums that consists of n unique elements, but you have forgotten it. However, you do remember
every pair of adjacent elements in nums.

You are given a 2D integer array adjacentPairs of size n - 1 where each adjacentPairs[i] = [ui, vi] indicates that the
elements ui and vi are adjacent in nums.

It is guaranteed that every adjacent pair of elements nums[i] and nums[i+1] will exist in adjacentPairs, either as
[nums[i], nums[i+1]] or [nums[i+1], nums[i]]. The pairs can appear in any order.

Return the original array nums. If there are multiple solutions, return any of them.

Example 1:
    Input: adjacentPairs = [[2,1],[3,4],[3,2]]
    Output: [1,2,3,4]
    Explanation: This array has all its adjacent pairs in adjacentPairs.
    Notice that adjacentPairs[i] may not be in left-to-right order.

Example 2:
    Input: adjacentPairs = [[4,-2],[1,4],[-3,1]]
    Output: [-2,4,1,-3]
    Explanation: There can be negative numbers.
    Another solution is [-3,1,4,-2], which would also be accepted.

Example 3:
    Input: adjacentPairs = [[100000,-100000]]
    Output: [100000,-100000]

Constraints:
    nums.length == n
    adjacentPairs.length == n - 1
    adjacentPairs[i].length == 2
    2 <= n <= 105
    -105 <= nums[i], ui, vi <= 105
    There exists some nums that has adjacentPairs as its pairs.
"""

import collections
from typing import List


class Solution:
    """
    Breadth-first search (BFS) approach

    Runtime: 1084 ms, faster than 77.60% of Python3
    Memory Usage: 62.9 MB, less than 84.88%
    """

    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        for a, b in adjacentPairs:  # build a graph of edges between nodes
            graph[a].append(b)
            graph[b].append(a)

        stack = collections.deque()
        for node in graph:  # find first element of the original array
            if len(graph[node]) == 1:
                stack.append(node)
                break

        result, seen = list(), set()
        while stack:  # BFS to traverse the path from start to end node
            node = stack.popleft()
            result.append(node)
            seen.add(node)
            for next_node in graph[node]:
                if next_node not in seen:
                    stack.append(next_node)
        return result


if __name__ == '__main__':
    solutions = [Solution()]
    tc = (
        ([[2, 1], [3, 4], [3, 2]], [1, 2, 3, 4]),
        ([[4, -2], [1, 4], [-3, 1]], [-2, 4, 1, -3]),
        ([[100000, -100000]], [100000, -100000]),
    )
    for sol in solutions:
        for inp_pairs, exp_result in tc:
            res = sol.restoreArray(inp_pairs)
            assert res == exp_result, f"{sol.__class__.__name__}: result {res} != {exp_result} expected"
