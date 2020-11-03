"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively.
Could you implement both?
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """
    Runtime: 36 ms, faster than 96.32% of Python3.
    Memory Usage: 14.4 MB, less than 72.88% of Python3.

    Iterative approach.

    Runtime complexity: O(n)
    Space complexity: O(1)
    """
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return

        prev = None
        curr = head

        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev    # the last node is the new head


class Solution2:
    """
    Runtime: 28 ms, faster than 53.93% of Python.
    Memory Usage: 18.5 MB, less than 5.04% of Python.

    Recursive approach.
    """
    def reverseList(self, head):
        return self._reverse(head)

    def _reverse(self, node, prev = None):
        if node is None:
            return prev

        curr, node.next = node.next, prev
        return self._reverse(curr, node)



class Solution:
    """
    Recursive approach.
    
    The recursive version key is to work backwards. 
    Assume that the rest of the list had already been reversed, now how do I reverse the front part? 
    Let's assume the list is: n1 → … → nk-1 → nk → nk+1 → … → nm → Ø

    Assume from node nk+1 to nm had been reversed and you are at node nk.
    n1 → … → nk-1 → nk → nk+1 ← … ← nm

    We want nk+1’s next node to point to nk.

    So, nk.next.next = nk;
    
    Runtime: 32 ms, faster than 86.81% of Python3
    Memory Usage: 18.7 MB, less than 7.97% of Python3 
    """
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p
    

if __name__ == "__main__":
    def get_linked_list_representation(node):
        list_values = list()
        while node:
            list_values.append(str(node.val))
            node = node.next
        return ' -> '.join(list_values)

    ln1 = ListNode(1)
    ln2 = ListNode(2)
    ln3 = ListNode(3)
    ln1.next = ln2
    ln2.next = ln3

    s = Solution()
    s2 = Solution2()

    new_head = s.reverseList(ln1)
    assert get_linked_list_representation(new_head) == '3 -> 2 -> 1'

    new_head2 = s2.reverseList(new_head)
    assert get_linked_list_representation(new_head2) ==  '1 -> 2 -> 3'
