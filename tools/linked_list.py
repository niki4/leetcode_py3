# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def get_linked_list_representation(node: ListNode) -> str:
    list_values = list()
    while node:
        list_values.append(str(node.val))
        node = node.next
    return ' -> '.join(list_values)


def make_linked_list_from_iterable(seq):
    head = prev = None
    for v in seq:
        n = ListNode(v)
        if not head:
            head = prev = n
        else:
            prev.next = n
            prev = n
    return head


def traverse(head: ListNode):
    values = []
    node = head
    while node:
        values.append(node.val)
        node = node.next
    return values
