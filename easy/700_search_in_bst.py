"""
Given the root node of a binary search tree (BST) and a value. You need to find the node in the BST that the node's value equals the given value. Return the subtree rooted with that node. If such node doesn't exist, you should return NULL.

For example, 

Given the tree:
        4
       / \
      2   7
     / \
    1   3

And the value to search: 2
You should return this subtree:

      2     
     / \   
    1   3
In the example above, if we want to search the value 5, since there is no node with value 5, we should return NULL.

Note that an empty tree is represented by NULL, therefore you would see the expected output (serialized tree format)
as [], not null. """

from typing import Optional

from tools.binary_tree import TreeNode


class Solution:
    """
    Recursive approach.
    Algorithm idea: BST is the ideal candidate for binary search - compare current node value with target, if the node
    value greater than target, then go in left subtree (we guaranteed all values in right subtree also greater than
    target and thus can be discarded). Accordingly, if the node value lower than target, then we go to right subtree.

    Runtime: 68 ms, faster than 92.94% of Python3
    Memory Usage: 16.1 MB, less than 99.50% of Python3
   
    Time complexity : O(H), where H is a tree height. That results in O(logN) in the average case, and O(N) worst case.
    Space complexity : O(H) to keep the recursion stack, i.e. O(logN) in the average case, and O(N) in the worst case.
    """

    def searchBST(self, root: TreeNode, val: int) -> Optional[TreeNode]:
        if root is None or root.val == val:
            return root

        if val < root.val:
            return self.searchBST(root.left, val)
        else:  # val > root.val
            return self.searchBST(root.right, val)


class Solution2:
    """
    Iterative approach.
    Runtime: 68 ms, faster than 92.94% of Python3
    Memory Usage: 16.1 MB, less than 99.50% of Python3
    
    Time complexity : O(H), where H is a tree height. That results in O(logN) in the average case, and O(N) worst case.
    Space complexity : O(1) since it's a constant space solution.
    """

    def searchBST(self, root: TreeNode, val: int) -> Optional[TreeNode]:
        while root is not None and root.val != val:
            root = root.left if val < root.val else root.right
        return root
