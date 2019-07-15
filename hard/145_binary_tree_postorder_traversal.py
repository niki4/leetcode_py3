"""
Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    Runtime: 32 ms, faster than 89.81% of Python3.
    Memory Usage: 13.2 MB, less than 57.51% of Python3.

    Recursive approach.
    """
    def __init__(self):
        self.result = []

    def _postorder_helper(self, node):
        if node is not None:
            self._postorder_helper(node.left)
            self._postorder_helper(node.right)
            self.result.append(node.val)

    def postorderTraversal(self, root: TreeNode) -> list:
        self._postorder_helper(root)
        return self.result


class Solution2:
    """
    Runtime: 32 ms, faster than 89.27% of Python3.
    Memory Usage: 13.3 MB, less than 17.00% of Python3.

    Iterative approach.
    """
    def postorderTraversal(self, root: TreeNode) -> list:
        result, stack = [], [(root, False)]
        while stack:
            node, visited = stack.pop()
            if node is not None:
                if visited:
                    result.append(node.val)
                else:
                    # post order
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))
        return result


if __name__ == "__main__":
    s = Solution()
    s2 = Solution2()
    btn1 = TreeNode(1)
    btn2 = TreeNode(2)
    btn3 = TreeNode(3)
    btn1.right = btn2
    btn2.left = btn3

    assert s.postorderTraversal(btn1) == [3, 2, 1]
    assert s2.postorderTraversal(btn1) == [3, 2, 1]
