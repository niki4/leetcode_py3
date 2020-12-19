"""
Given the root of a binary tree, return the postorder traversal of its nodes' values.

Input: root = [1,null,2,3]
Output: [3,2,1]

Post-order traversal is to traverse the left subtree first. Then traverse the right subtree. Finally, visit the root.
For example, for the following tree result will be [A, C, E, D, B, H, I, G, F]
            F
         /     \
       B        G
     /   \       \
    A     D       I
         /  \     /
        C    E    H
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


class Solution2:
    """
    Iterative solution with stack for holding result.

    Runtime: 24 ms, faster than 94.67% of Python3
    Memory Usage: 14.4 MB, less than 5.58% of Python3
    """

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        stack, result = [root, ], []
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return result[::-1]


if __name__ == "__main__":
    def make_binary_tree():
        root = TreeNode(1)
        btn2 = TreeNode(2)
        btn3 = TreeNode(3)
        root.right = btn2
        btn2.left = btn3
        return root


    solutions = [Solution(), Solution2()]
    exp = [3, 2, 1]
    for s in solutions:
        res = s.postorderTraversal(make_binary_tree())
        assert res == exp, f'{s.__class__.__name__}: want {exp}, got {res}'
