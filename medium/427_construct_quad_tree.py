"""
Given a n * n matrix grid of 0's and 1's only. We want to represent the grid with a Quad-Tree.
Return the root of the Quad-Tree representing the grid.

Notice that you can assign the value of a node to True or False when isLeaf is False, and both are accepted in answer.

A Quad-Tree is a tree data structure in which each internal node has exactly 4 children. Each node has 2 attributes:
    val: True if the node represents a grid of 1's or False if the node represents a grid of 0's.
    isLeaf: True if the node is leaf node on the tree or False if the node has the four children.

We can construct a Quad-Tree from a two-dimensional area using the following steps:
    1. If the current grid has the same value (i.e all 1's or all 0's) set isLeaf True and set val to the value of the
        grid and set the four children to Null and stop.
    2. If the current grid has different values, set isLeaf to False and set val to any value and divide the current
        grid into four sub-grids as shown in the photo.
    3. Recurse for each of the children with the proper sub-grid.

If you want to know more about the Quad-Tree, you can refer to the wiki.

Quad-Tree format:

The output represents the serialized format of a Quad-Tree using level order traversal, where null signifies a path
terminator where no node exists below.

It is very similar to the serialization of the binary tree. The only difference is that the node is represented as
a list [isLeaf, val].

If the value of isLeaf or val is True we represent it as 1 in the list [isLeaf, val] and if the value of isLeaf or val
is False we represent it as 0.

Example 1:
    Input: grid = [[0,1],[1,0]]
    Output: [[0,1],[1,0],[1,1],[1,1],[1,0]]
    Explanation: The explanation of this example is shown below:
    Notice that 0 represents False and 1 represents True in the photo representing the Quad-Tree.
More examples: https://leetcode.com/problems/construct-quad-tree/
"""

# Definition for a QuadTree node.
from typing import List


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    """
    Runtime: 116 ms, faster than 70.95% of Python3
    Memory Usage: 15.2 MB, less than 32.00% of Python3

    Time / Space complexity: O(n)
    """

    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        if self.is_leaf(grid, n):
            return Node(grid[0][0] == 1, True, None, None, None, None)
        # root node
        return Node(val="*", isLeaf=False,
                    topLeft=self.construct([row[:n // 2] for row in grid[:n // 2]]),
                    topRight=self.construct([row[n // 2:] for row in grid[:n // 2]]),
                    bottomLeft=self.construct([row[:n // 2] for row in grid[n // 2:]]),
                    bottomRight=self.construct([row[n // 2:] for row in grid[n // 2:]]))

    def is_leaf(self, grid: List[List[int]], n: int):
        """ It's leaf if the current grid has the same values (i.e all 1's or all 0's) """
        return all(grid[i][j] == grid[0][0] for i in range(n) for j in range(n))
