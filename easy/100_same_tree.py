"""
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    Runtime: 36 ms, faster than 71.97% of Python3.
    Memory Usage: 13.2 MB, less than 5.74% of Python3.
    """
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        elif p and q:
            return all([
                p.val == q.val,
                self.isSameTree(p.left, q.left),
                self.isSameTree(p.right, q.right)])
        return False
