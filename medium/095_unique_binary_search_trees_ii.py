"""
Given an integer n, generate all structurally unique BST's (binary search trees)
that store values 1 ... n.

Example:
Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation: The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

Constraints: 0 <= n <= 8
"""
import functools


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    The number of possible BST is actually a Catalan number (https://en.wikipedia.org/wiki/Catalan_number).
    Algorithm: Let's pick up number i out of the sequence 1 ..n and use it as the root
    of the current tree. Then there are i - 1 elements available for the construction
    of the left subtree and n - i elements available for the right subtree.

    Runtime: 56 ms, faster than 79.27% of Python3
    Memory Usage: 15.7 MB, less than 53.44% of Python3
    """

    def generateTrees(self, n: int):  # -> List[TreeNode]
        def generate_trees(start, end):
            if start > end:
                return [None, ]

            all_trees = []
            for i in range(start, end + 1):  # i is the root for subtrees
                left_trees = generate_trees(start, i - 1)  # all possible left subtrees
                right_trees = generate_trees(i + 1, end)  # ...and right ones

                # connect subtrees with their root (i)
                for l in left_trees:
                    for r in right_trees:
                        current_tree = TreeNode(i)
                        current_tree.left, current_tree.right = l, r
                        all_trees.append(current_tree)
            return all_trees

        return generate_trees(1, n) if n else []


class Solution2:
    """
    StefanPochmann's adopted version
    (https://leetcode.com/problems/unique-binary-search-trees-ii/discuss/31495/Should-be-6-Liner)

    Runtime: 56 ms (44 ms), faster than 79.27% (99.32 %) of Python3.
    Memory Usage: 14.6 MB, less than 53.44% of Python3.

    lru_cache should help to avoid duplicated calculations
    """

    def node(self, val, left, right):
        node = TreeNode(val)
        node.left = left
        node.right = right
        return node

    def generateTrees(self, n: int):  # -> List[TreeNode]
        if n == 0:
            return []

        @functools.lru_cache()
        def gen_subtrees(first, last):
            return [self.node(root, left, right)
                    for root in range(first, last + 1)
                    for left in gen_subtrees(first, root - 1)
                    for right in gen_subtrees(root + 1, last)] or [None]

        return gen_subtrees(1, n)
