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
import collections
from typing import List

from tools.binary_tree import TreeNode


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


class Solution2:
    """
    BFS (breadth-first search) - level by level (from top to bottom)

    Time complexity : O(n). The whole tree is traversed at most once.
                            Here, n refers to the number of nodes in the given binary tree.
    Space complexity : O(m). The size of queue or temp can grow upto at most the maximum number of nodes at any level
    in the given binary tree. Here, mm refers to the maximum number of nodes at any level in the input tree.

    Runtime: 44 ms, faster than 91.77% of Python3
    Memory Usage: 16.6 MB, less than 70.57% of Python3
    """

    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return []
        level_nums = collections.defaultdict(list)
        level = 0
        queue = [(root, level)]

        while queue:
            node, level = queue.pop(0)  # pop leftmost (tree node) first
            level_nums[level].append(node.val)
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        return [sum(level_nums[i]) / len(level_nums[i]) for i in range(level + 1)]


if __name__ == '__main__':
    solutions = [Solution, Solution2]
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    expected = [3, 14.5, 11]
    for sol in solutions:
        res = sol().averageOfLevels(root)
        assert res == expected, f"{sol.__class__.__name__}: expected {expected}, got {res}"
