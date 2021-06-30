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
from typing import Iterator

from tools.binary_tree import TreeNode


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


class Solution4:
    """
    Using Python's generators

    Runtime: 52 ms, faster than 59.86% of Python3
    Memory Usage: 18 MB, less than 80.85% of Python3

    Time complexity: O(n)
    Space complexity: O(1) as generator object returns one item at a time
    """

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def dfs_inorder(node: TreeNode) -> Iterator[int]:
            if node:
                yield from dfs_inorder(node.left)
                yield node.val
                yield from dfs_inorder(node.right)

        smallest = dfs_inorder(root)
        for _ in range(k):
            result = next(smallest)
        return result


class Solution5:
    """
    Morris Traversal. In this traversal, we first create links to Inorder successor and print
    the data using these links, and finally revert the changes to restore original tree.
        https://en.wikipedia.org/wiki/Tree_traversal#Morris_in-order_traversal_using_threading
        https://www.youtube.com/watch?v=wGXB9OWhPTg

    Runtime: 44 ms, faster than 92.55% of Python3
    Memory Usage: 18 MB, less than 54.23% of Python3

    Time complexity: O(n)
    Space complexity: O(1)
    """

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        curr = root
        while curr:
            if curr.left:
                prev = curr.left
                while prev.right and prev.right != curr:
                    prev = prev.right
                if not prev.right:  # link to Inorder Successor (IS)
                    prev.right = curr
                    curr = curr.left
                else:
                    k -= 1
                    if not k:
                        return curr.val
                    curr = prev.right
                    prev.right = None  # break link to IS
                    curr = curr.right
            else:
                k -= 1
                if not k:
                    return curr.val
                curr = curr.right
