"""
You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer,
which may or may not point to a separate doubly linked list.

These child lists may have one or more children of their own,
and so on, to produce a multilevel data structure, as shown in the example below.

Flatten the list so that all the nodes appear in a single-level, doubly linked list.
You are given the head of the first level of the list.

Example 2:
Input: head = [1,2,null,3]
Output: [1,3,2]
Explanation:
The input multilevel linked list is as follows (node '1' has child list '3'):
  1---2---NULL
  |
  3---NULL
"""

# Definition for a Node.
from problems.tools.linked_list import traverse


class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    """
    Algorithm idea: while traversing the list, if we encounter node with children
     - embed child list as next (seq) to traverse. So literally we flat the list as we go.

     Runtime: 32 ms, faster than 82.44% of Python3
     Memory Usage: 14.6 MB, less than 84.78% of Python3
    """

    def getTail(self, head):
        node = head
        while node and node.next:
            node = node.next
        return node

    def flatten(self, head: 'Node') -> 'Node':
        node = head
        while node:
            if node.child:
                # put child list between current and next node
                tail = self.getTail(node.child)
                tail.next = node.next
                if tail.next:
                    node.next.prev = tail
                node.next = node.child
                node.child.prev = node
                node.child = None
            # go next node (if was node.child, we proceed with them)
            node = node.next
        return head


if __name__ == '__main__':
    ln1 = Node(val=1, prev=None, next=None, child=None)
    ln2 = Node(val=2, prev=None, next=None, child=None)
    ln3 = Node(val=3, prev=None, next=None, child=None)
    ln1.next = ln2
    ln2.prev = ln1
    ln1.child = ln3
    sol = Solution()
    assert traverse(sol.flatten(ln1)) == [1, 3, 2]
