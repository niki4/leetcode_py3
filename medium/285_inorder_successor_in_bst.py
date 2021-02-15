"""
Given a binary search tree and a node in it, find the in-order successor of that node in the BST.

The successor of a node p is the node with the smallest key greater than p.val.

Example 1:
        2
      /   \
     1     3
Input: root = [2,1,3], p = 1
Output: 2
Explanation: 1's in-order successor node is 2. Note that both p and the return value is of TreeNode type.
"""
from problems.tools.binary_tree import TreeNode


class Solution:
    """
    Inorder DFS

    Runtime: 84 ms, faster than 25.41% of Python3
    Memory Usage: 18.4 MB, less than 27.68% of Python3

    Time / Space complexity: O(n)
    """

    def __init__(self):
        self.nodes = list()

    def inorderTraversal(self, node: TreeNode):
        if node:
            self.inorderTraversal(node.left)
            self.nodes.append(node)
            self.inorderTraversal(node.right)

    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        self.inorderTraversal(root)
        for i in range(len(self.nodes) - 1, 0, -1):
            if self.nodes[i - 1].val == p.val:
                return self.nodes[i]


class Solution2:
    """
    Runtime: 64 ms, faster than 93.82% of Python3
    Memory Usage: 18.3 MB, less than 27.68% of Python3

    Time complexity: O(H) where H is the height of the tree
    Space complexity: O(1)
    """

    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        candidate = None
        # We start from the root, utilizing the property of BST
        curr = root

        while curr:
            # If current node's value is greater than p's value, current node is a candidate.
            # Go to its left subtree to see if we can find a smaller one.
            if curr.val > p.val:
                candidate = curr
                curr = curr.left
            # If current node's value is less than or equal to p's value, we know our answer
            # must be in the right subtree.
            else:  # curr.val <= p.val
                curr = curr.right
        # If we reach "curr is None" condition, our search is over, just return the candidate.
        return candidate
