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


class Solution2:
    """
    Iterative Traversal with Valid Range

    Runtime: 48 ms, faster than 42.15% of Python3
    Memory Usage: 16.2 MB, less than 81.86% of Python3
    Time and Space complexity: O(n)
    """

    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True

        stack = [(root, -math.inf, math.inf)]
        while stack:
            node, low, high = stack.pop()
            if not node:
                continue
            if node.val <= low or node.val >= high:
                return False
            stack.append((node.right, node.val, high))
            stack.append((node.left, low, node.val))
        return True


class Solution3:
    """
    Algorithm (Recursive Inorder Traversal):
    Left -> Node -> Right order of inorder traversal means for BST that each element should be smaller
    than the next one. Thus we need to keep track of prev visited node value. Inorder traversal for valid BST will visit
    nodes in ascending order.

    Runtime: 48 ms, faster than 42.15% of Python3
    Memory Usage: 16.9 MB, less than 16.63% of Python3
    """

    def __init__(self):
        self.prev = -math.inf

    def inorder(self, node: TreeNode) -> bool:
        # Inorder DFS: traverse left subtree first, then visit the root, then traverse right subtree
        if not node:
            return True
        if not self.inorder(node.left):
            return False
        if node.val <= self.prev:
            return False
        self.prev = node.val
        return self.inorder(node.right)

    def isValidBST(self, root: TreeNode) -> bool:
        return self.inorder(root)


if __name__ == '__main__':
    def make_valid_bst():
        n1 = TreeNode(2)
        n0 = TreeNode(1)
        n2 = TreeNode(3)
        n1.left, n1.right = n0, n2
        return n1


    def make_invalid_bst():
        n1 = TreeNode(1)
        n0 = TreeNode(2)
        n2 = TreeNode(3)
        n1.left, n1.right = n0, n2
        return n1


    solutions = [Solution(), Solution2(), Solution3()]
    for s in solutions:
        assert s.isValidBST(make_valid_bst()) is True
        assert s.isValidBST(make_invalid_bst()) is False
