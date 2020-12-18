"""
Given the root of a binary tree, return the postorder traversal of its nodes' values.

Input: root = [1,null,2,3]
Output: [3,2,1]

"""
from typing import List


# Definition for a binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    Simple recursive solution. Can be tuned for pre-, in-, and post-order solutions:

    Preorder
            self.result.append(root.val)
            self._order_helper(root.left)
            self._order_helper(root.right)

    Inorder
            self._order_helper(root.left)
            self.result.append(root.val)
            self._order_helper(root.right)

    Postorder
            self._order_helper(root.left)
            self._order_helper(root.right)
            self.result.append(root.val)
        Runtime: 28 ms, faster than 80.53% of Python3
        Memory Usage: 14.2 MB, less than 21.59% of Python3
    """

    def __init__(self):
        self.result = []

    def _order_helper(self, root):
        if root is not None:
            self._order_helper(root.left)
            self._order_helper(root.right)
            self.result.append(root.val)

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        self._order_helper(root)
        return self.result
