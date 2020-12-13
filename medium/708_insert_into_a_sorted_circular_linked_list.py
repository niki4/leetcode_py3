"""
Given a node from a Circular Linked List which is sorted in ascending order, write a function to insert
a value insertVal into the list such that it remains a sorted circular list. The given node can be a reference to
any single node in the list, and may not be necessarily the smallest value in the circular list.

If there are multiple suitable places for insertion, you may choose any place to insert the new value.
After the insertion, the circular list should remain sorted.

If the list is empty (i.e., given node is null), you should create a new single circular list and return
the reference to that single node. Otherwise, you should return the original given node.

Example 1:
Input: head = [3,4,1], insertVal = 2
Output: [3,4,1,2]
Explanation: In the figure above, there is a sorted circular list of three elements. You are given a reference to
the node with value 3, and we need to insert 2 into the list. The new node should be inserted between node 1 and node 3.
 After the insertion, the list should look like this, and we should still return node 3.

Example 2:
Input: head = [], insertVal = 1
Output: [1]
Explanation: The list is empty (given head is null).
 We create a new single circular list and return the reference to that single node.

Example 3:
Input: head = [1], insertVal = 0
Output: [1,0]

Constraints:
0 <= Number of Nodes <= 5 * 10^4
-10^6 <= Node.val <= 10^6
-10^6 <= insertVal <= 10^6
"""
from problems.tools.linked_list import ListNode as Node, make_circulated_linked_list, traverse


class Solution:
    """
    Bruteforce solution - collect and sort values in cycled list, then sort to keep the order, then rebuild the list.

    Runtime: 32 ms, faster than 89.87% of Python3
    Memory Usage: 15 MB, less than 16.77% of Python3

    Time complexity: O(NlogN) because of sorting collected values
    Space complexity: O(n)
    """

    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        node = head
        seen = dict()
        while node is not None and not (node in seen):
            seen[node] = node.val
            node = node.next

        new_node = Node(insertVal)
        seen[new_node] = insertVal
        if head is None:
            head = new_node

        sorted_nodes = sorted(seen, key=lambda k: seen[k])

        for i in range(len(sorted_nodes)):
            if i == len(sorted_nodes) - 1:
                sorted_nodes[i].next = sorted_nodes[0]
            else:
                sorted_nodes[i].next = sorted_nodes[i + 1]
        return head


class Solution2:
    """
    Algorithm idea: having list sorted we can be sure while traversing list we returned back to the head
    if the head value lower than its previous node value. Basically during this traversing we only need
    to find suitable place to insert new node, so we check in following priority:
    1. If target node fits between to neighbour, so that prev node smaller and next node has greater val than insertVal
    2. If we have insertVal lower than head (smallest value in list) or greater than tail (greatest value in list) we
    just put new node between tail and head.
    3. Finally, if all values in the list are the same, we can also just put new node between tail and head.

    Runtime: 36 ms, faster than 70.30% of Python3
    Memory Usage: 15 MB, less than 17.54% of Python3

    Time complexity: O(n) we need to traverse entire list at worst case
    Space complexity: O(1)
    """

    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if not head:
            head = Node(insertVal)
            head.next = head
            return head

        curr = head

        while True:
            # found place to insert, e.g. 9 between 8 and 10
            if curr.val <= insertVal <= curr.next.val:
                break

            # last element
            if curr.val > curr.next.val:
                # greater than tail (max num)
                if curr.val <= insertVal >= curr.next.val:
                    break
                # lower than head (min num)
                elif curr.val >= insertVal <= curr.next.val:
                    break

            # all elements are equal
            if curr.next == head:
                break
            curr = curr.next

        new_node = Node(insertVal)
        next_node = curr.next
        curr.next = new_node
        new_node.next = next_node
        return head


if __name__ == '__main__':
    def get_tc():
        return [
            ([3, 4, 1], 2, [3, 4, 1, 2]),
            ([], 1, [1]),
            ([1], 0, [1, 0]),
            ([1, 3, 5], 2, [1, 2, 3, 5]),
            ([3, 3, 3], 0, [3, 3, 3, 0]),
            ([1, 3, 5], 1, [1, 1, 3, 5]),
        ]


    solutions = [Solution(), Solution2()]

    for s in solutions:
        for inp_list, insert_val, output_list in get_tc():
            input_ll = make_circulated_linked_list(inp_list)
            result = s.insert(input_ll, insert_val)
            assert traverse(result) == output_list
