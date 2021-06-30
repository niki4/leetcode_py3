"""
You have n gardens, labeled from 1 to n, and an array paths where paths[i] = [Xi, Yi] describes a bidirectional path
between garden Xi to garden Yi. In each garden, you want to plant one of 4 types of flowers.

All gardens have at most 3 paths coming into or leaving it.

Your task is to choose a flower type for each garden such that, for any two gardens connected by a path, they have
different types of flowers.

Return any such a choice as an array answer, where answer[i] is the type of flower planted in the (i+1)th garden.
The flower types are denoted 1, 2, 3, or 4. It is guaranteed an answer exists.

Example 1:
Input: n = 3, paths = [[1,2],[2,3],[3,1]]
Output: [1,2,3]
Explanation:
    Gardens 1 and 2 have different types.
    Gardens 2 and 3 have different types.
    Gardens 3 and 1 have different types.
    Hence, [1,2,3] is a valid answer. Other valid answers include [1,2,4], [1,4,2], and [3,2,1].

Example 2:
Input: n = 4, paths = [[1,2],[3,4]]
Output: [1,2,1,2]

Example 3:
Input: n = 4, paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
Output: [1,2,3,4]

Constraints:
    1 <= n <= 104
    0 <= paths.length <= 2 * 104
    paths[i].length == 2
    1 <= Xi, Yi <= n
    Xi != Yi
    Every garden has at most 3 paths coming into or leaving it.
"""
from typing import List


class Solution:
    """
    Greedy approach (sum of optimal local solutions lead to the optimal result to the whole task).

    Runtime: 432 ms, faster than 78.15% of Python3
    Memory Usage: 21 MB, less than 86.94% of Python3

    Time complexity: O(N) with O(paths) = O(1.5N)
    Space complexity: O(N)
    """

    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        flowers = [0] * n
        routes = [[] for _ in range(n)]
        for x, y in paths:
            routes[x - 1].append(y - 1)
            routes[y - 1].append(x - 1)

        for i in range(n):
            # assign random flower that do not exist in linked gardens, this will return at least one option to choose
            # as coming from constraints "Every garden has at most 3 paths coming into or leaving it."
            flowers[i] = ({1, 2, 3, 4} - {flowers[other_garden] for other_garden in routes[i]}).pop()
        return flowers


if __name__ == '__main__':
    solutions = [Solution()]
    tc = (
        (3, [[1, 2], [2, 3], [3, 1]], [1, 2, 3]),
        (4, [[1, 2], [3, 4]], [1, 2, 1, 2]),
        (4, [[1, 2], [2, 3], [3, 4], [4, 1], [1, 3], [2, 4]], [1, 2, 3, 4]),
    )
    for sol in solutions:
        for inp_n, inp_paths, exp_answer in tc:
            answer = sol.gardenNoAdj(inp_n, inp_paths)
            assert answer == exp_answer, f"{sol.__class__.__name__}: {answer} != {exp_answer}"
