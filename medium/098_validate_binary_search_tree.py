"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Example 1:
     2
    / \
   1   3
Input: root = [2,1,3]
Output: true
"""
import math

from problems.tools.binary_tree import TreeNode


class Solution:
    """
    Algorithm idea (Recursive Traversal with Valid Range):
    Let's traverse the tree and check at each step if node.right.val > node.val and node.left.val < node.val;
    To guarantee that left subtrees values are less than the right subtrees, compare node val with low and high limits.

    Runtime: 40 ms, faster than 88.51% of Python3
    Memory Usage: 16.4 MB, less than 64.75% of Python3
    Time and Space complexity: O(n)
    """

    def validate(self, node: TreeNode, low=-math.inf, high=math.inf):
        # empty trees are valid BSTs
        if not node:
            return True
        # the current node's value must be between low and high
        if node.val <= low or node.val >= high:
            return False
        # the left and right subtree must also be valid
        return (self.validate(node.right, node.val, high) and
                self.validate(node.left, low, node.val))

    def isValidBST(self, root: TreeNode) -> bool:
        return self.validate(root)


if __name__ == '__main__':
    n1 = TreeNode(2)
    n0 = TreeNode(1)
    n2 = TreeNode(3)
    n1.left, n1.right = n0, n2

    solutions = [Solution()]
    for s in solutions:
        assert s.isValidBST(n1) is True
