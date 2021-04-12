"""
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

Example 1:
            (3)
         /      \
        1       (4)
       /       /  \
     (3)      1   (5)

Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in parentheses are good.
    Root Node (3) is always a good node.
    Node 4 -> (3,4) is the maximum value in the path starting from the root.
    Node 5 -> (3,4,5) is the maximum value in the path
    Node 3 -> (3,1,3) is the maximum value in the path.

Example 2:
          (3)
         /
       (3)
      /   \
     (4)   2

Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.

Example 3:
Input: root = [1]
Output: 1
Explanation: Root is considered as good.

Constraints:
    The number of nodes in the binary tree is in the range [1, 10^5].
    Each node's value is between [-10^4, 10^4].
"""
from tools.binary_tree import TreeNode


class Solution:
    """
    Use DFS (Depth First Search) to traverse the tree,
    and constantly keep track of the current path maximum.

    The solution below could give better performance metrics if use DFS helper in closure,
    but I personally prefer class-based approach here.

    Runtime: 256 ms, faster than 52.11% of Python3
    Memory Usage: 33.6 MB, less than 11.91% of Python3

    Time complexity: O(n) where n is the number of nodes in the tree
    Space complexity: O(h) where h is the height of the tree (num of levels) to keep recursion stack.
    """

    def __init__(self):
        self.good_nodes = 0

    def dfs(self, node: TreeNode, max_val: int):
        if node:
            if node.val >= max_val:
                self.good_nodes += 1
            max_val = max(max_val, node.val)
            self.dfs(node.left, max_val)
            self.dfs(node.right, max_val)

    def goodNodes(self, root: TreeNode) -> int:
        self.dfs(root, root.val)
        return self.good_nodes
