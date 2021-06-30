"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then
right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
"""
from typing import List

from tools.binary_tree import TreeNode


class Solution:
    """
    DFS (Deep-First Search) traversal: we maintain the results in a global array that is indexed by the level, i.e.
    the element array[level] would contain all the nodes that are at the same level. The global array would then be
    referred and updated at each step of DFS.

    Runtime: 28 ms, faster than 90.67% of Python3
    Memory Usage: 14.6 MB, less than 14.54% of Python3

    Time complexity: O(n) where n is the number of nodes in the tree.
                     We visit each node once during tree traversal. It's O(n)
                     Then for each odd-level node (starting from 0-th level) we apply .reverse() to a list which is O(n)
    Space complexity: O(n) to store all node values in result list (of lists).
    """

    def __init__(self):
        self.result = []

    def traverse(self, node: TreeNode, level: int):
        if node:
            if level == len(self.result):
                self.result.append([node.val])
            else:
                self.result[level].append(node.val)
            self.traverse(node.left, level + 1)
            self.traverse(node.right, level + 1)

    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        self.traverse(root, 0)
        for i, nodes in enumerate(self.result):
            if i % 2:  # odd indexed lists should be in right to left order
                nodes.reverse()
        return self.result
