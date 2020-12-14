"""
A linked list is given such that each node contains an additional random pointer
which could point to any node in the list or null.

Return a deep copy of the list.

The Linked List is represented in the input/output as a list of n nodes.
Each node is represented as a pair of [val, random_index] where:
* val: an integer representing Node.val
* random_index: the index of the node (range from 0 to n-1) where random pointer points to,
or null if it does not point to any node.

Example 1:
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
"""


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    """
    2-pass approach.
    On first pass we creating shallow copies of nodes (without links, just values),
    on second pass we link (new nodes) as they are in the original list.

    Runtime: 36 ms, faster than 59.90% of Python3
    Memory Usage: 14.9 MB, less than 32.19% of Python3

    Time and space complexity: O(n)
    """

    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return

        copies = dict()
        node = head
        while node:
            copies[node] = Node(node.val)
            node = node.next

        node = head
        while node:
            copies[node].next = copies[node.next] if node.next else None
            copies[node].random = copies[node.random] if node.random else None
            node = node.next
        return copies[head]
