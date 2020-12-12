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
from problems.tools.linked_list import ListNode as Node, make_linked_list_from_iterable, traverse


class Solution:
    """
    Bruteforce solution - collect and sort values in cycled list, then sort to keep the order, then rebuild the list.

    Runtime: 32 ms, faster than 89.87% of Python3
    Memory Usage: 15 MB, less than 16.77% of Python3
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


if __name__ == '__main__':
    def get_tc():
        return [
            ([3, 4, 1], 2, [3, 4, 1, 2]),
            ([], 1, [1]),
            ([1], 0, [1, 0]),
        ]


    solutions = [Solution()]

    for s in solutions:
        for inp_list, insert_val, output_list in get_tc():
            input_ll = make_linked_list_from_iterable(inp_list)
            result = s.insert(input_ll, insert_val)
            assert traverse(result) == output_list
