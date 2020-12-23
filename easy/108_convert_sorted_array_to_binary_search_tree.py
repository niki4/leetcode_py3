"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees
of every node never differ by more than 1.

Example:
Given the sorted array: [-10,-3,0,5,9],
One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:
      0
     / \
   -3   9
   /   /
 -10  5
"""
from typing import List

from problems.tools.binary_tree import TreeNode


class Solution:
    """
    Algorithm (Preorder Traversal: Always Choose Left Middle Node as a Root):
        * Implement helper function helper(left, right), which constructs BST from nums elements between
            indexes left and right:
            **  If left > right, then there is no elements available for that subtree. Return None.
            ** Pick left middle element: p = (left + right) // 2.
            ** Initiate the root: root = TreeNode(nums[p]).
            ** Compute recursively left and right subtrees:
                root.left = helper(left, p - 1), root.right = helper(p + 1, right).
        * Return helper(0, len(nums) - 1).

    Runtime: 72 ms, faster than 63.15% of Python3
    Memory Usage: 16.5 MB, less than 38.62% of Python3

    Time complexity: O(N) since we visit each node exactly once.
    Space complexity: O(N). O(N) to keep the output, and O(logN) for the recursion stack.
    """

    def helper(self, left, right):
        if left > right:
            return None

        # always choose left middle node as a root
        p = (left + right) // 2

        # preorder traversal: node -> left -> right
        root = TreeNode(self.nums[p])
        root.left = self.helper(left, p - 1)
        root.right = self.helper(p + 1, right)
        return root

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        self.nums = nums
        return self.helper(0, len(nums) - 1)


class Solution2:
    """
    Preorder Traversal: Always Choose Right Middle Node as a Root

    Runtime: 72 ms, faster than 63.15% of Python3
    Memory Usage: 16.5 MB, less than 17.41% of Python3
    Time and Space complexity the same as in first Solution.
    """

    def helper(self, left, right):
        if left > right:
            return None

        # always choose right middle node as a root
        p = (left + right) // 2
        # if left + right is odd, add 1 to p-index.
        if (left + right) % 2:
            p += 1

        # preorder traversal: node -> left -> right
        root = TreeNode(self.nums[p])
        root.left = self.helper(left, p - 1)
        root.right = self.helper(p + 1, right)
        return root

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        self.nums = nums
        return self.helper(0, len(nums) - 1)
