"""
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].

Note: The range of node's value is in the range of 32-bit signed integer.
"""
from typing import List

from problems.tools.binary_tree import TreeNode


class Solution:
    """
    Combination of Preorder DFS (traverse nodes) and BFS (insert values on each level)

    Runtime: 52 ms, faster than 55.44% of Python3
    Memory Usage: 17.1 MB, less than 19.43% of Python3

    Time & Space complexity: O(n)
    """

    def __init__(self):
        self.node_vals = list()

    def traverse(self, node: TreeNode, level: int):
        if node:
            if level >= len(self.node_vals):
                self.node_vals.append([node.val])
            else:
                self.node_vals[level].append(node.val)
            self.traverse(node.left, level + 1)
            self.traverse(node.right, level + 1)

    def averageOfLevels(self, root: TreeNode) -> List[float]:
        self.traverse(root, 0)
        return [sum(lvl) / len(lvl) for lvl in self.node_vals]
