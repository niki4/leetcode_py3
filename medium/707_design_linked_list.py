"""
Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the current node,
and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in
the linked list. Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:

MyLinkedList() Initializes the MyLinkedList object.
int get(int index) Get the value of the index-th node in the linked list. If the index is invalid, return -1.
void addAtHead(int val) Add a node of value val before the first element of the linked list.
    After the insertion, the new node will be the first node of the linked list.
void addAtTail(int val) Append a node of value val as the last element of the linked list.
void addAtIndex(int index, int val) Add a node of value val before the index-th node in the linked list.
    If index equals the length of the linked list, the node will be appended to the end of the linked list.
    If index is greater than the length, the node will not be inserted.
void deleteAtIndex(int index) Delete the index-th node in the linked list, if the index is valid.
"""


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class MyLinkedList:
    """
    Implemented as single-linked list

    Runtime: 376 ms, faster than 13.87% of Python3
    Memory Usage: 15.2 MB, less than 20.07% of Python3
    Time complexity:
        O(1) for addAtHead
        O(k) for get, addAtIndex, and deleteAtIndex, where k is an index of the element to get, add or delete.
        O(N) for addAtTail
    Space complexity: O(1) for all operations
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.length = 0

    def print_list(self):
        values = []
        node = self.head
        while node:
            values.append(str(node.val))
            node = node.next
        print("->".join(values))

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index > self.length - 1:
            return -1
        curr_idx = 0
        node = self.head
        while node and curr_idx != index:
            node = node.next
            curr_idx += 1
        return node.val if node else -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            node = self.head
            while node and node.next is not None:
                node = node.next
            node.next = new_node
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index == self.length:
            self.addAtTail(val)
        elif index < self.length:
            curr_idx = 0
            node = self.head
            while node and curr_idx != index:
                curr_idx += 1
                node = node.next
            before_node = Node(node.val, node.next)
            node.val = val
            node.next = before_node
            self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if self.head and (0 <= index < self.length):
            if index == 0:
                self.head = self.head.next
                self.length -= 1
            elif index == self.length - 1:  # tail
                node = self.head
                while node and node.next and node.next.next:  # prev and curr
                    node = node.next
                node.next = None
                self.length -= 1
            else:  # not head and not tail
                node = self.head
                curr_idx = 0
                while node and node.next and curr_idx + 1 != index:  # node.next is node to del
                    curr_idx += 1
                    node = node.next
                node.next = node.next.next
                self.length -= 1


if __name__ == '__main__':
    myLinkedList = MyLinkedList()
    myLinkedList.addAtHead(1)
    myLinkedList.addAtTail(3)
    myLinkedList.addAtIndex(1, 2)  # linked list becomes 1->2->3
    myLinkedList.print_list()
    print(myLinkedList.get(1))  # return 2
    myLinkedList.deleteAtIndex(1)  # now the linked list is 1->3
    myLinkedList.print_list()
    print(myLinkedList.get(1))  # return 3
