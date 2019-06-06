"""
Given a binary search tree and the lowest and highest boundaries as L and R,
trim the tree so that all its elements lies in [L, R] (R >= L).
You might need to change the root of the tree, so the result should
return the new root of the trimmed binary search tree.

Example 1:
Input:
    1
   / \
  0   2

  L = 1
  R = 2

Output:
    1
      \
       2

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    Runtime: 52 ms, faster than 97.09% of Python3.
    Memory Usage: 17.3 MB, less than 37.78% of Python3.

    Algorithm:
        When node.val > R, we know that the trimmed binary tree must occur
        to the left of the node. Similarly, when node.val < L, the trimmed
        binary tree occurs to the right of the node. Otherwise, we will trim
        both sides of the tree.

    Time Complexity: O(N), where N is the total number of nodes in the given tree.
    Space Complexity: O(N). Call stack of our recursion as large as the number of nodes.
    """
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        def trim(node):
            if not node:
                return None
            elif node.val > R:
                return trim(node.left)
            elif node.val < L:
                return trim(node.right)
            else:
                node.left = trim(node.left)
                node.right = trim(node.right)
                return node
        return trim(root)

class Solution2:
    """
    Runtime: 56 ms, faster than 90.50% of Python3.
    Memory Usage: 17.3 MB, less than 45.37% of Python3.

    Recursive approach.
    """
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        if root is None:
            return None
        left = self.trimBST(root.left, L, R)
        right = self.trimBST(root.right, L, R)
        if L <= root.val <= R:
            root.left, root.right = left, right
            return root
        return left if left is not None else right


if __name__ == "__main__":
    s = Solution()
    s2 = Solution2()

    tn_L = TreeNode(0)
    tn_R = TreeNode(2)
    tn_root = TreeNode(1)
    tn_root.left = tn_L
    tn_root.right = tn_R

    root = s.trimBST(tn_root, 1, 2)
    assert root.val == 1
    assert root.left is None
    assert root.right.val == 2

    root = s2.trimBST(tn_root, 1, 2)
    assert root.val == 1
    assert root.left is None
    assert root.right.val == 2
