"""
Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
             1                       1 -> None
          /    \                  /    \
        2       3               2   ->  3 -> None
      /  \        \           /  \        \
    4     5        7        4 ->  5   ->   7 -> None
Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its
next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers,
with '#' signifying the end of each level.

Follow up:
    You may only use constant extra space.
    Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.
"""


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    """
    Algorithm: Preorder DFS (depth-first search) on traversal and BFS (breadth-first search) on insert nodes to list.

    Runtime: 48 ms, faster than 76.59% of Python3
    Memory Usage: 15.5 MB, less than 10.42% of Python3

    Time/Space complexity: O(n)
    """

    def __init__(self):
        self.nodes = list()

    def inorder_traversal(self, node: 'Node', level: int):
        if node:
            if level >= len(self.nodes):
                self.nodes.append([node])
            else:
                self.nodes[level].append(node)
            self.inorder_traversal(node.left, level + 1)
            self.inorder_traversal(node.right, level + 1)

    def connect(self, root: 'Node') -> 'Node':
        self.inorder_traversal(root, 0)
        for nodes in self.nodes:
            for i in range(1, len(nodes)):
                nodes[i - 1].next = nodes[i]
        return root
