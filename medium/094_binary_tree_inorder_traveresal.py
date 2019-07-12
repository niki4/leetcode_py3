"""
Given a binary tree, return the inorder traversal of its nodes' values.

Example:
Input: [1,null,2,3]
   1
    \
     2
    /
   3
Output: [1,3,2]

Follow up: Recursive solution is trivial, could you do it iteratively?
"""

# Definition for a binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    Runtime: 40 ms, faster than 16.15% of Python3.
    Memory Usage: 13.2 MB, less than 36.39% of Python3.

    Recursive approach. Algorithm idea:
        1. We first traverse left as much as possible.
        2. Once there are no nodes at left branch, take the value.
        3. Then proceed right at possible depth.
        4. If there are no nodes at right, switch to left traversal.
           If there are no nodes both at left and right, stop recursion and exit.
    """
    def __init__(self):
        self.result = []

    def _inorder_helper(self, root):
        if root is not None:
            self._inorder_helper(root.left)
            self.result.append(root.val)
            self._inorder_helper(root.right)

    def inorderTraversal(self, root: TreeNode) -> list:
        self._inorder_helper(root)
        return self.result


class Solution2:
    """
    Runtime: 32 ms, faster than 89.70% of Python3.
    Memory Usage: 13.3 MB, less than 14.12% of Python3.

    Iterative approach
    """
    def inorderTraversal(self, root: TreeNode) -> list:
        result, stack = [], []
        while True:
            while root is not None:
                stack.append(root)
                root = root.left
            if not stack:
                return result
            node = stack.pop()
            result.append(node.val)
            root = node.right
        return result


if __name__ == "__main__":
    s = Solution()
    s2 = Solution2()
    btn1 = TreeNode(1)
    btn2 = TreeNode(2)
    btn3 = TreeNode(3)
    btn1.right = btn2
    btn2.left = btn3

    assert s.inorderTraversal(btn1) == [1, 3, 2]
    assert s2.inorderTraversal(btn1) == [1, 3, 2]
