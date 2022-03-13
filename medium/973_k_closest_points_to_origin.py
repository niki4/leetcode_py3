"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k,
return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)^2 + (y1 - y2)^2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

More info: https://en.wikipedia.org/wiki/Euclidean_distance
"""

import math
from typing import List

class Solution:
    """
    Time complexity: O(NlogN)
    """
    def get_euclidian_distance(self, x, y):
        return math.sqrt((x - 0)**2 + (y - 0)**2)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return sorted(
            points,
            key=lambda point: self.get_euclidian_distance(point[0], point[1]),
        )[:k]


if __name__ == '__main__':
    solutions = [
        Solution(),
    ]
    tc = (
        ([[1,3],[-2,2]], 1, [[-2,2]]),
        ([[3,3],[5,-1],[-2,4]], 2, [[3,3],[-2,4]]),
    )
    for sol in solutions:
        for inp_points, inp_k, exp_output in tc:
            res = sol.kClosest(inp_points, inp_k)
            assert sorted(res) == sorted(exp_output), f'{sorted(res)} != {sorted(exp_output)}'
