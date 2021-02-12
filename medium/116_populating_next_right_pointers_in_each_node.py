"""
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children.
The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer
should be set to NULL.

Initially, all next pointers are set to NULL.

Follow up:
You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.

Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
             1                       1 -> None
          /    \                  /    \
        2       3               2   ->  3 -> None
      /  \     /  \           /  \     /  \
    4     5   6    7        4 ->  5-> 6 -> 7 -> None

Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to
point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next
pointers, with '#' signifying the end of each level.
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
    Algorithm: Preorder DFS (depth-first search) for traversing, BFS-like insert to nodes list thanks to level tracking.

    Runtime: 68 ms, faster than 40.45% of Python3
    Memory Usage: 15.8 MB, less than 8.69% of Python3

    Time / Space complexity: O(N)
    """

    def __init__(self):
        self.nodes = list()

    def bfs(self, node: 'Node', level=0):
        if node:
            if level == len(self.nodes):
                self.nodes.append([node])
            else:
                self.nodes[level].append(node)

            self.bfs(node.left, level + 1)
            self.bfs(node.right, level + 1)

    def connect(self, root: 'Node') -> 'Node':
        self.bfs(root)
        for nodes in self.nodes:
            for i in range(1, len(nodes)):
                nodes[i - 1].next = nodes[i]
        return root


class Solution2:
    """
    Algorithm: BFS (breadth-first-search) - upside down and left to right.

    Runtime: 52 ms, faster than 98.35% of Python3
    Memory Usage: 15.8 MB, less than 36.80% of Python3

    Time Complexity:    O(N) since we process each node exactly once.
    Space Complexity:   O(1) since we don't make use of any additional data structure for traversing nodes on a
                        particular level like the previous approach does.
    """

    def connect(self, root: 'Node') -> 'Node':
        # Start with the root node. There are no next pointers
        # that need to be set up on the first level.
        leftmost = root

        # Once we reach the final level, we are done
        while leftmost and leftmost.left:
            # Iterate the "linked list" starting from the head
            # node and using the next pointers, establish the
            # corresponding links for the next level.
            head = leftmost
            while head:
                # Connection 1 (left child to right child)
                head.left.next = head.right
                # Connection 2 (between subtrees on the same level)
                if head.next:
                    head.right.next = head.next.left
                # move to next node on the same level
                head = head.next

            # move onto next level
            leftmost = leftmost.left

        return root
