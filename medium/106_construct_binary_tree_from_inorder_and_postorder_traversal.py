"""
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7

"""
from typing import List

from problems.tools.binary_tree import TreeNode


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def build(bound=None):
            if not inorder or inorder[-1] == bound:
                return None
            root = TreeNode(postorder.pop())
            root.right = build(root.val)
            inorder.pop()
            root.left = build(bound)
            return root

        return build()
