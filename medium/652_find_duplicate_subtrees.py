"""
Given the root of a binary tree, return all duplicate subtrees.

For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with the same node values.

Example 1:
         1
       /  \
    (2)    3
    /    /  \
(4)    (2)   4
       /
     (4)
Input: root = [1,2,3,4,null,2,4,null,null,4]
Output: [[2,4],[4]]

Example 2:

Input
[0,0,0,0,null,null,0,null,null,0]
Output
[[0]]
Expected
[[0,0],[0]]
        0
      /   \
     0	   0
    /       \
   0		 0
            /
           0
"""

from collections import defaultdict
from typing import List

from problems.tools.binary_tree import TreeNode


class Solution:
    """
    Algorithm (leetcode.com/problems/find-duplicate-subtrees/discuss/106016/O(n)-time-and-space-lots-of-analysis):
        Convert the entire tree of nested TreeNodes to a tree of nested tuples.
        Those have the advantage that they already support hashing and deep comparison (for the very unlikely cases of
        hash collisions). Then just use each subtree's tuple version as a key in the dictionary "trees".
        And equal subtrees have the same key and thus get collected in the same list (
        thus then we filter out all keys that has only one record in the list).

    Runtime: 92 ms, faster than 22.66% of Python3
    Memory Usage: 18.4 MB, less than 77.78% of Python3

    Runtime complexity: O(n**2)
    Space complexity: O(n) where n is the number of nodes in the given tree

    Note: tuples don't cache their own hash value. So if use a tuple as key and thus it gets
    asked for its hash value, it will compute it again. Which entails asking its content elements for their hashes.
    And if they're tuples, then they'll do the same and ask their elements for their hashes. And so on.
    So asking a tuple tree root for its hash traverses the entire tree. Which makes the above solution only O(n^2) time
    """

    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        def tuplify(node: TreeNode):
            if node:
                tuple_ = node.val, tuplify(node.left), tuplify(node.right)
                trees[tuple_].append(node)
                return tuple_

        trees = defaultdict(list)
        tuplify(root)
        return [roots[0] for roots in trees.values() if roots[1:]]


class Solution2:
    """
    To optimize Solution1 we simply wrap each tuple in a frozenset, which does cache its hash value.
    Yet "frozenset" is hashable (may apply hash() func) while regular "set" is not.

    Runtime: 64 ms, faster than 58.24% of Python3
    Memory Usage: 20.5 MB, less than 73.65% of Python3

    Runtime complexity: O(n) on average and O(n**2) on worst case (caching hashes doesn't work in all cases, e.g. if
    we have hash collisions, complexity grows on with height of the tree).
    Space complexity: O(n)
    """

    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        def traverse(node: TreeNode):
            if node:
                res = frozenset([(
                    node.val,
                    traverse(node.left),
                    traverse(node.right),
                )])
                trees[res].append(node)
                return res

        trees = defaultdict(list)
        traverse(root)
        return [nodes[0] for nodes in trees.values() if nodes[1:]]


class Solution3:
    """
    Algorithm idea: Identify trees by numbering them.
    The first unique subtree gets id 0, the next unique subtree gets id 1, the next gets 2, etc.
    Now the dictionary keys aren't deep nested structures anymore but just ints and triples of ints.

    Runtime: 60 ms, faster than 76.51% of Python3
    Memory Usage: 18.9 MB, less than 75.17% of Python3

    Runtime and Space complexity: O(n)
    """

    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        def traverse(node: TreeNode):
            if node:
                id_ = tree_id[node.val, traverse(node.left), traverse(node.right)]
                trees[id_].append(node)
                return id_

        trees = defaultdict(list)
        tree_id = defaultdict()
        tree_id.default_factory = tree_id.__len__

        traverse(root)
        """
        For Example1 tree:
        tree_id: defaultdict(<method-wrapper '__len__' of collections.defaultdict object at 0x7f9271b54770>, 
        {(4, None, None): 0, (2, 0, None): 1, (3, 1, 0): 2, (1, 1, 2): 3})
        """
        return [nodes[0] for nodes in trees.values() if nodes[1:]]
