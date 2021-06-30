"""
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure
and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants.
The tree tree could also be considered as a subtree of itself.

Example 1:
            3 (root)
           /\
         4   5             4 (subroot)
        / \               / \
       1   2             1   2

Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true

Example 2:
            3 (root)
           /\
         4   5             4 (subroot)
        / \               / \
       1   2             1   2
          /
         0
Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false

Constraints:
    The number of nodes in the root tree is in the range [1, 2000].
    The number of nodes in the subRoot tree is in the range [1, 1000].
    -104 <= root.val <= 104
    -104 <= subRoot.val <= 104
"""
from tools.binary_tree import TreeNode


class Solution:
    """
    Depth-first search (DFS) to compare all nodes from s (as a starting point) with t.

    Runtime: 152 ms, faster than 57.48% of Python3
    Memory Usage: 15.2 MB, less than 45.92% of Python3

    Time complexity: O(|s| * |t|) where s and t are number of nodes in the related trees.
    """

    def dfs_is_identical(self, root1: TreeNode, root2: TreeNode) -> bool:
        if root1 is None or root2 is None:
            return root1 == root2  # True if both are None, False otherwise
        return (root1.val == root2.val and
                self.dfs_is_identical(root1.left, root2.left) and
                self.dfs_is_identical(root1.right, root2.right))

    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if t is None:  # subtree completely traversed at this point and all nodes matches within s
            return True
        if s is None:  # either no match found or tree s has smaller size than subtree t
            return False

        if self.dfs_is_identical(s, t):
            return True

        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
