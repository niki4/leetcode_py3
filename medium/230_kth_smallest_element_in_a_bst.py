"""
Given the root of a binary search tree, and an integer k, return the kth (1-indexed) smallest element in the tree.

Example 1:
        3
      /   \
    1      4
     \
      2

Input: root = [3,1,4,null,2], k = 1
Output: 1
"""

import heapq

from problems.tools.binary_tree import TreeNode


class Solution:
    """
    Using heap queue (priority queue) that keeps its sorted state on each insert.

    Runtime: 64 ms, faster than 17.28% of Python3
    Memory Usage: 18 MB, less than 58.03% of Python3

    Time / Space complexity: O(n)
    """

    def __init__(self):
        self.heap = []

    def helper(self, node: TreeNode):
        if node:
            self.helper(node.left)
            heapq.heappush(self.heap, node.val)
            self.helper(node.right)

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.helper(root)
        return self.heap[k - 1]


class Solution2:
    """ To solve the problem, one could use the property of BST :
    inorder traversal of BST is an array sorted in the ascending order.

    With inorder (DFS) traversal we first reach left subtree (lowest value),
    then root/parent node (next after lowest),
    then right subtree (greatest value)

    Imagine the subtree:
                     4
                   /   \
                  2     5
                /  \
               1    3
    After the inorder traversal we get values: [1, 2, 3, 4, 5]

    Runtime: 64 ms, faster than 17.28% of Python3
    Memory Usage: 18.4 MB, less than 16.60% of Python3

    Time / Space complexity: O(n)
    """

    def inorder(self, node: TreeNode):
        return self.inorder(node.left) + [node.val] + self.inorder(node.right) if node else []

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        return self.inorder(root)[k - 1]


class Solution3:
    """
    Inorder (DFS) iterative approach.

    Runtime: 64 ms, faster than 17.28% of Python3
    Memory Usage: 17.9 MB, less than 95.72% of Python3

    Time complexity: O(H+k), where H is a tree height. This complexity is defined by the stack, which contains at least
    H+k elements, since before starting to pop out one has to go down to a leaf. This results in O(logN+k) for the
    balanced tree and O(N+k) for completely unbalanced tree with all the nodes in the left subtree.
    Space complexity: O(H) to keep the stack, where H is a tree height. That makes O(N) in the worst case of the skewed
    tree, and O(logN) in the average case of the balanced tree.
    """

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []

        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right