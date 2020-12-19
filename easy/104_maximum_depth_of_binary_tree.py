"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along
the longest path from the root node down to the
farthest leaf node.

Note: A leaf is a node with no children.

Example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
"""
from problems.tools.binary_tree import TreeNode


class Solution:
    """
    Runtime: 44 ms, faster than 95.68% of Python3.
    Memory Usage: 15.3 MB, less than 77.99% of Python3.

    Bottom-up approach (recursively go down, once base case (empty node) - rewind stack adding 1 at each level):
    https://leetcode.com/explore/learn/card/data-structure-tree/17/solve-problems-recursively/534/#bottom-up-solution
    """

    def maxDepth(self, root: TreeNode) -> int:
        return 1 + max(
            self.maxDepth(root.left),
            self.maxDepth(root.right)
        ) if root else 0


class Solution2:
    """
    Runtime: 36 ms, faster than 90.52% of Python3
    Memory Usage: 16 MB, less than 54.37% of Python3

    Top-down approach (pass level param as you go down, if not children (leaf) - update max_depth):
    https://leetcode.com/explore/learn/card/data-structure-tree/17/solve-problems-recursively/534/#top-down-solution
    """

    def __init__(self):
        self.max_depth = 0

    def _maxDepthHelper(self, node: TreeNode, level: int):
        if node:
            if node.left is None and node.right is None:  # leaf
                self.max_depth = max(self.max_depth, level)
            self._maxDepthHelper(node.left, level + 1)
            self._maxDepthHelper(node.right, level + 1)

    def maxDepth(self, root: TreeNode) -> int:
        self._maxDepthHelper(root, 1)
        return self.max_depth


if __name__ == "__main__":
    def make_binary_tree():
        tn_left = TreeNode(9)
        tn_right = TreeNode(20)
        tn_root = TreeNode(3)
        tn_root.left = tn_left
        tn_root.right = tn_right
        tn_root.right.left = TreeNode(15)
        tn_root.right.right = TreeNode(7)
        return tn_root


    solutions = [Solution(), Solution2()]

    for s in solutions:
        res = s.maxDepth(make_binary_tree())
        assert res == 3, f'Expected depth 3, got {res}'
