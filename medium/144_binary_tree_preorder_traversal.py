"""
Given the root of a binary tree, return the preorder traversal of its nodes' values.

Pre-order traversal is to visit the root first.
Then traverse the left subtree.
Finally, traverse the right subtree.

For example, for the following tree result will be [F, B, A, D, C, E, G, I, H]
            F
         /     \
       B        G
     /   \       \
    A     D       I
         /  \     /
        C    E    H

Example 1:
Input: root = [1,null,2,3]
Output: [1,2,3]
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Recursive solution.

    Runtime: 28 ms, faster than 80.84% of Python3
    Memory Usage: 14 MB, less than 81.63% of Python3
    Time and Space complexity both O(n)
    """

    def __init__(self):
        self.result = list()

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return self.result
        self.result.append(root.val)
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)
        return self.result


class Solution2:
    """
    Iterative solution.

    Runtime: 32 ms, faster than 53.09% of Python3
    Memory Usage: 14.3 MB, less than 22.61% of Python3
    Time and Space complexity both O(n)
    """

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack = [root, ]
        result = list()
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result
