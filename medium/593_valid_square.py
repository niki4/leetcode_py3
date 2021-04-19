"""
Given the coordinates of four points in 2D space p1, p2, p3 and p4, return true if the four points construct a square.
The coordinate of a point pi is represented as [xi, yi]. The input is not given in any order.
A valid square has four equal sides with positive length and four equal angles (90-degree angles).

Example 1:
Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
Output: true

Example 2:
Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,12]
Output: false

Example 3:
Input: p1 = [1,0], p2 = [-1,0], p3 = [0,1], p4 = [0,-1]
Output: true

Constraints:
    p1.length == p2.length == p3.length == p4.length == 2
    -104 <= xi, yi <= 104
"""
from typing import List


class Solution:
    """
    Algorithm: sort the points and figure out where the last two points should be with the coordinates of the first two.

    Runtime: 32 ms, faster than 78.95% of Python3
    Memory Usage: 14.4 MB, less than 11.12% of Python3

    Time complexity : O(1). Sorting 4 points takes constant time.
    Space complexity : O(1). Constant space is required.
    """

    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        if p1 == p2 == p3 == p4:
            return False

        p1, p2, p3, p4 = sorted([p1, p2, p3, p4])
        if p2[1] < p3[1]:
            p2, p3 = p3, p2

        return (p3 == [p1[0] + (p2[1] - p1[1]), p1[1] - (p2[0] - p1[0])] and
                p4 == [p2[0] + (p2[1] - p1[1]), p2[1] - (p2[0] - p1[0])])


class Solution2:
    """
    Math solution from
    https://leetcode.com/problems/valid-square/discuss/103482/Python-Straightforward-with-Explanation
        "Suppose points ABCD have pairwise distances in sorted order S, S, S, S, S*sqrt(2), S*sqrt(2).
         We want to show ABCD is a square. Let us call S a "small side" and S*sqrt(2) a "large side".
         Without loss of generality, suppose AC is a large side. If BD is a large side, then AB and BC are small sides,
         so B lies on the intersection of circles between A and C; similarly, D lies on the same intersection, and thus
         ABCD is a square (as two different circles of the same radius only intersect in two different points)."

    Runtime: 36 ms, faster than 52.15% of Python3
    Memory Usage: 14.2 MB, less than 89.11% of Python3
    """

    def dist(self, p1: List[int], p2: List[int]) -> int:
        return (p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2

    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        D = [self.dist(p1, p2), self.dist(p1, p3), self.dist(p1, p4),
             self.dist(p2, p3), self.dist(p2, p4), self.dist(p3, p4)]
        D.sort()
        # For input [0, 0], [1, 1], [1, 0], [0, 1] result D will be [1, 1, 1, 1, 2, 2] == True
        # For input [1, 1], [5, 3], [3, 5], [7, 7] D will be [8, 20, 20, 20, 20, 72] == False
        return 0 < D[0] == D[1] == D[2] == D[3] and 2 * D[0] == D[4] == D[5]


if __name__ == '__main__':
    solutions = [Solution(), Solution2()]
    tc = (
        ([0, 0], [1, 1], [1, 0], [0, 1], True),
        ([0, 0], [1, 1], [1, 0], [0, 12], False),
        ([1, 0], [-1, 0], [0, 1], [0, -1], True),
        ([1, 1], [5, 3], [3, 5], [7, 7], False),
    )
    for sol in solutions:
        for p1_, p2_, p3_, p4_, valid_square in tc:
            assert sol.validSquare(p1_, p2_, p3_, p4_) is valid_square
