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


"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution2:
    """
    LC Recursive approach.

    Runtime: 56 ms, faster than 26.41% of Python3
    Memory Usage: 15.5 MB, less than 54.27% of Python3

    Time Complexity: O(N) since we process each node exactly once.
    Space Complexity: O(1) since we don't make use of any additional data structure for traversing nodes on a
                        particular level like the previous approach does.
    """

    def process_child(self, child: 'Node', prev, leftmost):
        if child:
            # If the "prev" pointer is alread set i.e. if we
            # already found atleast one node on the next level,
            # setup its next pointer
            if prev:
                prev.next = child
            else:
                # child node is the first node
                # we have encountered on the next level, so, we
                # set the leftmost pointer
                leftmost = child
            prev = child
        return prev, leftmost

    def connect(self, root: 'Node') -> 'Node':
        leftmost = root

        # We have no idea about the structure of the tree,
        # so, we keep going until we do find the last level.
        # The nodes on the last level won't have any children
        while leftmost:
            # "next_lvl_prev" tracks the latest node on the "next" level
            # while "curr" tracks the latest node on the current level.
            next_lvl_prev, curr = None, leftmost

            # We reset this so that we can re-assign it to the leftmost
            # node of the next level. Also, if there isn't one, this
            # would help break us out of the outermost loop.
            leftmost = None

            # Iterate on the nodes in the current level using
            # the next pointers already established.
            while curr:
                # Process both the children and update the prev
                # and leftmost pointers as necessary.
                next_lvl_prev, leftmost = self.process_child(curr.left, next_lvl_prev, leftmost)
                next_lvl_prev, leftmost = self.process_child(curr.right, next_lvl_prev, leftmost)

                # move to next node the same level
                curr = curr.next
        return root


class Solution3:
    """
    Iterative approach

    Runtime: 48 ms, faster than 76.59% of Python3
    Memory Usage: 15.4 MB, less than 83.61% of Python3

    Time complexity: O(n)
    Space complexity: O(1)
    """

    def connect(self, root: 'Node') -> 'Node':
        # prev is the prev child node to link from
        # tail is the first child node on the next level
        prev = tail = None
        node = root

        while node:
            if node.left:
                if prev:
                    prev.next = node.left
                prev = node.left
                if not tail:
                    tail = node.left

            if node.right:
                if prev:
                    prev.next = node.right
                prev = node.right
                if not tail:
                    tail = node.right

            # go to next node the same level
            node = node.next
            # go to first child node on the next level
            if not node:
                node = tail
                prev = tail = None
        return root
