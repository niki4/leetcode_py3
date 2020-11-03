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

Note that an empty tree is represented by NULL, therefore you would see the expected output (serialized tree format) as [], not null.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Recursive approach.
    Runtime: 68 ms, faster than 92.94% of Python3
    Memory Usage: 16.1 MB, less than 99.50% of Python3
   
    Time complexity : O(H), where H is a tree height. That results in O(logN) in the average case, and O(N) in the worst case.
    Space complexity : O(H) to keep the recursion stack, i.e. O(logN) in the average case, and O(N) in the worst case.
    """
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None or root.val == val:
            return root
        
        if val < root.val:
            return self.searchBST(root.left, val)
        else: #  val > root.val
            return self.searchBST(root.right, val)


class Solution2:
    """
    Iterative approach.
    Runtime: 68 ms, faster than 92.94% of Python3
    Memory Usage: 16.1 MB, less than 99.50% of Python3
    
    Time complexity : O(H), where H is a tree height. That results in O(logN) in the average case, and O(N) in the worst case.
    Space complexity : O(1) since it's a constant space solution.
    """
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        while root is None or root.val != val:
            root = root.left if val < root.val else root.right
        return root
