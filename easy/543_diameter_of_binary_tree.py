"""
Given a binary tree, you need to compute the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
This path may or may not pass through the root.

Runtime: 72 ms, faster than 21.15% of Python3.
Memory Usage: 16 MB, less than 48.28% of Python3.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.count = 1

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        """ Depth-First Search """
        def walk(node: TreeNode):
            if node:
                L = walk(node.left)
                R = walk(node.right)
                self.count = max(self.count, L + R + 1)
                return max(L, R) + 1
            else:
                return 0

        walk(root)
        return self.count - 1


if __name__ == '__main__':
    n1 = TreeNode(x=1)
    n2 = TreeNode(x=2)
    n3 = TreeNode(x=3)
    n4 = TreeNode(x=4)
    n5 = TreeNode(x=5)
    r"""
          1
         / \
        2   3
       / \     
      4   5   
    max length is 3 steps - the path [4,2,1,3] or [5,2,1,3].
    """
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    s = Solution()
    diameter = s.diameterOfBinaryTree(n1)
    assert diameter == 3, f'Expected 3, got {diameter}'
