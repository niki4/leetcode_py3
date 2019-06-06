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
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    Runtime: 44 ms, faster than 95.68% of Python3.
    Memory Usage: 15.3 MB, less than 77.99% of Python3.
    """
    def maxDepth(self, root: TreeNode) -> int:
        return 1 + max(
            self.maxDepth(root.left),
            self.maxDepth(root.right)
        ) if root else 0


if __name__ == "__main__":
    s = Solution()
    tn_left = TreeNode(9)
    tn_right = TreeNode(20)
    tn_root = TreeNode(3)
    tn_root.left = tn_left
    tn_root.right = tn_right
    tn_root.right.left = TreeNode(15)
    tn_root.right.right = TreeNode(7)

    assert s.maxDepth(tn_root) == 3
