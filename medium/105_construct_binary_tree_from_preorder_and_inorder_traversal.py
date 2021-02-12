"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7

"""
from typing import List

from problems.tools.binary_tree import TreeNode


class Solution:
    """
    Algorithm idea:
        1. Pop first element from preorder list. It's a root node.
        2. Find that element in inorder list.
            All items left side from it will be left subtree,
            the same applies for right side (to right subtree).

    Runtime: 60 ms, faster than 78.74% of Python3
    Memory Usage: 19.1 MB, less than 70.02% of Python3

    Time complexity: O(N)
    Space complexity: O(N)
    """

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def helper(in_left=0, in_right=len(inorder)):
            # The nonlocal statement causes the listed identifiers to refer to
            # previously bound variables in the nearest enclosing scope excluding globals.
            nonlocal pre_idx
            # if there is no elements to construct subtrees
            if in_left == in_right:
                return None

            # pick up pre_idx element as a root
            root_val = preorder[pre_idx]
            root = TreeNode(root_val)

            # root splits inorder list
            # into left and right subtrees
            index = idx_map[root_val]

            # recursion
            pre_idx += 1
            # build left subtree
            root.left = helper(in_left, index)
            # build right subtree
            root.right = helper(index + 1, in_right)
            return root

        # start from first preorder element
        pre_idx = 0
        # build a hashmap value -> its index
        idx_map = {val: idx for (idx, val) in enumerate(inorder)}
        return helper()


class Solution2:
    """
    @StefanPochmann's solution:
leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/discuss/34543/Simple-O(n)-without-map
    Explanation/Discussion:

    Consider this input:
    preorder: [1, 2, 4, 5, 3, 6]
    inorder: [4, 2, 5, 1, 6, 3]

    The obvious way to build the tree is:
    1. Use the first element of preorder, the 1, as root.
    2. Search it in inorder.
    3. Split inorder by it, here into [4, 2, 5] and [6, 3].
    4. Split the rest of preorder into two parts as large as the inorder parts, here into [2, 4, 5] and [3, 6].
    5. Use preorder = [2, 4, 5] and inorder = [4, 2, 5] to add the left subtree.
    6. Use preorder = [3, 6] and inorder = [6, 3] to add the right subtree.


    Consider the example again. Instead of finding the 1 in inorder, splitting the arrays into parts and recursing on
    them, just recurse on the full remaining arrays and stop when you come across the 1 in inorder. That's what the
    solution does. Each recursive call gets told where to stop, and it tells its subcalls where to stop. It gives its
    own root value as stopper to its left subcall and its parent`s stopper as stopper to its right subcall.

    Runtime: 52 ms, faster than 95.15% of Python3
    Memory Usage: 18.2 MB, less than 94.35% of Python3

    Time complexity: O(N)
    Space complexity: O(N)
    """

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def build(stop=None):
            if inorder and inorder[-1] != stop:
                root = TreeNode(preorder.pop())
                root.left = build(root.val)
                inorder.pop()
                root.right = build(stop)
                return root

        preorder.reverse()
        inorder.reverse()
        return build()
