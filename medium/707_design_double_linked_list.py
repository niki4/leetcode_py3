# Definition of Double linked list Node
class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


# Double Linked List
class MyLinkedList:
    """
    Runtime: 372 ms, faster than 14.65% of Python3
    Memory Usage: 15.4 MB, less than 6.53% of Python3
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
        Add a node of value val before the first element of the linked list.
        After the insertion, the new node will be the first node of the linked list.
        """
        new_node = Node(val, next=self.head)
        if self.head:
            self.head.prev = new_node
        self.head = new_node
        self.length += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        new_node = Node(val)
        if not self.head:
            self.addAtHead(val)
        else:
            node = self.head
            while node and node.next is not None:
                node = node.next
            new_node.prev = node
            node.next = new_node
            self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list.
        If index equals to the length of linked list, the node will be appended to the end of linked list.
        If index is greater than the length, the node will not be inserted.
        """
        if index == 0:
            self.addAtHead(val)
        elif index == self.length:
            self.addAtTail(val)
        elif index < self.length:
            curr_idx = 0
            node = self.head
            while node and curr_idx != index:
                curr_idx += 1
                node = node.next
            new_node = Node(val, prev=node.prev, next=node)
            node.prev.next = new_node
            node.prev = new_node
            self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if self.head and (0 <= index < self.length):
            if index == 0:  # remove node from head
                next_node = self.head.next
                if next_node:
                    next_node.prev = None
                self.head = next_node
                self.length -= 1
            elif index == self.length - 1:  # remove from tail
                node = self.head
                while node and node.next:  # find last node
                    node = node.next
                node.prev.next = None
                self.length -= 1
            else:  # between head and tail
                node = self.head
                curr_idx = 0
                while node and node.next and curr_idx != index:  # node.next is node to del
                    curr_idx += 1
                    node = node.next
                node.prev.next = node.next
                if node.next:
                    node.next.prev = node.prev
                self.length -= 1


if __name__ == '__main__':
    doubleList = MyLinkedList()
    doubleList.addAtHead(1)
    doubleList.addAtTail(3)
    doubleList.addAtIndex(1, 2)  # linked list becomes 1->2->3
    doubleList.print_list()
    print(doubleList.get(1))  # return 2
    doubleList.deleteAtIndex(1)  # now the linked list is 1->3
    doubleList.print_list()
    print(doubleList.get(1))  # return 3
