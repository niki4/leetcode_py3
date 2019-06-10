"""
Merge k sorted linked lists and return it as one sorted list.
Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""

class ListNode:
    """ Definition for singly-linked node """
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkedList:
    """ Definition for list of singly-list nodes """
    def __init__(self):
        self.head = None

    def __str__(self):
        node = self.head
        list_values = list()
        while node:
            list_values.append(str(node.val))
            node = node.next
        return '->'.join(list_values)

    def append(self, data):
        new_node = ListNode(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node


class Solution:
    """
    Runtime: 72 ms, faster than 92.39% of Python3 online submissions for Merge k Sorted Lists.
    Memory Usage: 17.3 MB, less than 20.69% of Python3 online submissions for Merge k Sorted Lists.

    Brute force approach:
        1. Traverse all the linked lists and collect the values of the nodes into an array.
        2. Sort and iterate over this array to get the proper value of nodes.
        3. Create a new sorted linked list and extend it with the new nodes.

    Time complexity : O(N logN) where N is the total number of nodes.
    Space complexity : O(N)
    """
    def mergeKLists(self, lists) -> ListNode:
        self.nodes = []
        head = point = ListNode(0)
        for l in lists:
            while l:
                self.nodes.append(l.val)
                l = l.next
        for x in sorted(self.nodes):
            point.next = ListNode(x)
            point = point.next
        return head.next


from queue import PriorityQueue

class Solution2:
    """
    Runtime: 212 ms, faster than 19.54% of Python3.
    Memory Usage: 17.5 MB, less than 14.70% of Python3.

    Using priority queue to keep total list of nodes sorted whilst
    traversing K lists. Alternatively, heapq can be used which also
    stored its data sorted.

    Time complexity: O(NlogK) where K is the number of linked lists
    Space complexity: O(N) for creating a new linked list + O(k)
    for priority queue. K is less than N.
    """
    def mergeKLists(self, lists) -> ListNode:
        class Wrapper:
            def __init__(self, node):
                self.node = node
            def __lt__(self, other):
                return self.node.val < other.node.val

        head = point = ListNode(0)
        q = PriorityQueue()
        for l in lists:
            if l:
                q.put(Wrapper(l))
        while not q.empty():
            node = q.get().node
            point.next = node
            point = point.next
            node = node.next
            if node:
                q.put(Wrapper(node))
        return head.next


class Solution3:
    """
    Runtime: 92 ms, faster than 59.47% of Python3.
    Memory Usage: 16.3 MB, less than 86.64% of Python3.

    Time complexity : O(Nlogk) where k is the number of linked lists.
    Space complexity : O(1)
    """
    def mergeKLists(self, lists) -> ListNode:
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.merge_two_lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else lists

    def merge_two_lists(self, l1, l2):
        head = point = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l1
                l1 = point.next.next
            point = point.next
        if not l1:
            point.next = l2
        else:
            point.next = l1
        return head.next


if __name__ == "__main__":
    s = Solution()
    s2 = Solution2()
    s3 = Solution3()

    lst1 = LinkedList()
    lst1.append(1)
    lst1.append(4)
    lst1.append(5)

    lst2 = LinkedList()
    lst2.append(1)
    lst2.append(3)
    lst2.append(4)

    lst3 = LinkedList()
    lst3.append(2)
    lst3.append(6)

    result0 = s.mergeKLists([lst1.head, lst2.head, lst3.head])
    result0_list = LinkedList()
    result0_list.head = result0
    assert result0_list.__str__() == '1->1->2->3->4->4->5->6'

    result2 = s2.mergeKLists([lst1.head, lst2.head, lst3.head])
    result2_list = LinkedList()
    result2_list.head = result2
    assert result2_list.__str__() == '1->1->2->3->4->4->5->6'
