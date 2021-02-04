"""
Design a HashSet without using any built-in hash table libraries.

Implement MyHashSet class:

void add(key) Inserts the value key into the HashSet.
bool contains(key) Returns whether the value key exists in the HashSet or not.
void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.


Example 1:
Input
["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]
Output
[null, null, null, true, false, null, true, null, false]

Explanation
MyHashSet myHashSet = new MyHashSet();
myHashSet.add(1);      // set = [1]
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(1); // return True
myHashSet.contains(3); // return False, (not found)
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(2); // return True
myHashSet.remove(2);   // set = [1]
myHashSet.contains(2); // return False, (already removed)
"""


class MyHashSet1:
    """
    Using "set" built-in type

    Runtime: 148 ms, faster than 89.10% of Python3
    Memory Usage: 18.9 MB, less than 64.09% of Python3
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.store = set()

    def add(self, key: int) -> None:
        self.store.add(key)

    def remove(self, key: int) -> None:
        if key in self.store:
            self.store.remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return key in self.store


###########################################################################################

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        res = []
        node = self.head
        while node:
            res.append(node.val)
            node = node.next
        return "->".join(str(n) for n in res)

    def insert(self, key):
        new_node = ListNode(key, self.head)
        self.head = new_node

    def remove(self, key):
        """ removes all nodes with given key """
        prev = None
        curr = self.head
        while curr:
            if curr.val == key:
                if prev:
                    prev.next = curr.next
                    curr = curr.next
                elif curr == self.head:
                    self.head = curr.next
                    curr = self.head
            else:
                prev = curr
                curr = curr.next

    def contains(self, key):
        if self.head is None:
            return False
        node = self.head
        while node:
            if node.val == key:
                return True
            node = node.next
        return False


class ListNode:
    """ Single Linked List node"""

    def __init__(self, val, next_=None):
        self.val = val
        self.next = next_


class MyHashSet2:
    """
    Since for any update operation, we would need to scan the entire bucket first to avoid any duplicate,
    a better choice for the implementation of bucket would be the LinkedList, which has a constant time complexity
    for the insertion as well as deletion, once we locate the position to update.

    Runtime: 192 ms, faster than 67.28% of Python3
    Memory Usage: 19.6 MB, less than 37.00% of Python3

    Time complexity: O(n) for scan through the list,
    O(1) for insert key,
    O(1) for remove key (we use whole list scan though to find nodes to be deleted)
    """

    def __init__(self):
        # it is generally advisable to use a prime number as the base of modulo,
        # e.g. 769, in order to reduce the potential collisions.
        self.store = [LinkedList() for _ in range(769)]

    def get_bucket(self, key):
        """ retrieves a Linked List instance representing the bucket """
        return self.store[key % 769]

    def add(self, key: int) -> None:
        bucket = self.get_bucket(key)
        bucket.insert(key)

    def remove(self, key: int) -> None:
        bucket = self.get_bucket(key)
        bucket.remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        bucket = self.get_bucket(key)
        return bucket.contains(key)


if __name__ == '__main__':
    solutions = [MyHashSet1, MyHashSet2]
    for HashSet in solutions:
        obj = HashSet()
        obj.add(1)
        obj.add(1)
        obj.add(2)
        obj.add(3)
        obj.remove(3)
        assert obj.contains(3) is False
        assert obj.contains(1) is True
