"""
Design a max stack data structure that supports the stack operations and supports finding the stack's maximum element.

Implement the MaxStack class:
    MaxStack() Initializes the stack object.
    void push(int x) Pushes element x onto the stack.
    int pop() Removes the element on top of the stack and returns it.
    int top() Gets the element on the top of the stack without removing it.
    int peekMax() Retrieves the maximum element in the stack without removing it.
    int popMax() Retrieves the maximum element in the stack and removes it.
                 If there is more than one maximum element, only remove the top-most one.

Example 1:
Input   ["MaxStack", "push", "push", "push", "top", "popMax", "top", "peekMax", "pop", "top"]
        [[], [5], [1], [5], [], [], [], [], [], []]
Output  [null, null, null, null, 5, 5, 1, 5, 1, 5]

Explanation
    MaxStack stk = new MaxStack();
    stk.push(5);   // [5] the top of the stack and the maximum number is 5.
    stk.push(1);   // [5, 1] the top of the stack is 1, but the maximum is 5.
    stk.push(5);   // [5, 1, 5] the top of the stack is 5, which is also the maximum, because it is the top most one.
    stk.top();     // return 5, [5, 1, 5] the stack did not change.
    stk.popMax();  // return 5, [5, 1] the stack is changed now, and the top is different from the max.
    stk.top();     // return 1, [5, 1] the stack did not change.
    stk.peekMax(); // return 5, [5, 1] the stack did not change.
    stk.pop();     // return 1, [5] the top of the stack and the max element is now 5.
    stk.top();     // return 5, [5] the stack did not change.

Constraints:
    -107 <= x <= 107
    At most 104 calls will be made to push, pop, top, peekMax, and popMax.
    There will be at least one element in the stack when pop, top, peekMax, or popMax is called.

Follow up: Could you come up with a solution that supports O(1) for each top call and O(logn) for each other call?
"""


class MaxStack:
    """
    Intuitive approach using Python's built-in list structure (dynamic array)

    Runtime: 144 ms, faster than 79.47% of Python3
    Memory Usage: 16.5 MB, less than 93.03% of Python3
    """

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_n = float('-inf')
        self.store = list()

    def push(self, x: int) -> None:
        """ Time complexity: O(n) because in amortized worst case we have to allocate a new array with greater size,
        than previous one, then copy all the elements from old array to new one, then finally push our new value at the
        end of the array."""
        self.store.append(x)
        if x > self.max_n:
            self.max_n = x

    def pop(self) -> int:
        """ Time complexity: O(n) for search new max, O(1) for list pop() """
        pop_num = self.store.pop()
        if pop_num == self.max_n:
            self.max_n = max(self.store) if self.store else float('-inf')
        return pop_num

    def top(self) -> int:
        """ Time complexity: O(1) """
        return self.store[-1]

    def peekMax(self) -> int:
        """ Time complexity: O(1) """
        return self.max_n

    def popMax(self) -> int:
        """ Time complexity: O(n) because of iterating over array, Also del() item from list takes O(n) """
        for i in range(len(self.store) - 1, -1, -1):
            if self.store[i] == self.max_n:
                del (self.store[i])
                popped_max = self.max_n
                self.max_n = max(self.store) if self.store else float('-inf')
                return popped_max


# Definition of Double linked list Node
class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class MaxStack2:
    """
    A more efficient(?) approach using Double-Linked List structure

    Generally push/pop/delete operations takes O(1) time,
    But to update link if new/deleted node is max_node we need find new max and
    it takes O(n) time.

    Runtime: 752 ms, faster than 5.04% of Python3
    Memory Usage: 17.1 MB, less than 14.97% of Python3
    """

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_node: (Node or None) = None
        self.last_node: (Node or None) = None

    def find_max_node_from_tail(self, tail: Node) -> Node:
        node = tail
        max_node = None
        while node:
            if max_node is None or node.val > max_node.val:
                max_node = node
            node = node.prev
        return max_node

    def find_max_node_from_head(self, head: Node) -> Node:
        node = head
        max_node = None
        while node:
            if max_node is None or node.val > max_node.val:
                max_node = node
            node = node.next
        return max_node

    def push(self, x: int) -> None:
        node = Node(val=x)
        if self.last_node:
            # insert after current tail
            self.last_node.next = node
            node.prev = self.last_node
            self.last_node = node
            self.max_node = self.find_max_node_from_tail(self.last_node)
        else:  # new list
            self.last_node = node
            self.max_node = node

    def pop(self) -> int:
        if self.last_node:
            pop_num = self.last_node.val
            prev = self.last_node.prev
            if prev:  # update tail
                prev.next = None
                if self.last_node == self.max_node:
                    self.max_node = self.find_max_node_from_tail(prev)
                self.last_node = prev
            else:  # pop from head, no elements left in list
                self.last_node = None
                self.max_node = None
            return pop_num

    def top(self) -> int:
        if self.last_node:
            return self.last_node.val

    def peekMax(self) -> int:
        if self.max_node:
            return self.max_node.val

    def popMax(self) -> int:
        if self.max_node:
            pop_max = self.max_node.val
            prev = self.max_node.prev
            next_ = self.max_node.next
            if prev:
                if self.max_node == self.last_node:
                    prev.next = None
                    self.last_node = prev
                else:
                    prev.next = self.max_node.next
                    self.max_node.next.prev = prev
                self.max_node = self.find_max_node_from_tail(self.last_node)
            elif next_:  # pop max from head
                next_.prev = None
                self.max_node = self.find_max_node_from_head(next_)
            else:  # the only element in the list
                self.last_node = None
                self.max_node = None

            return pop_max


if __name__ == '__main__':
    def tc_1(max_stack: MaxStack) -> bool:
        max_stack.push(5)
        max_stack.push(1)
        max_stack.push(5)
        assert max_stack.top() == 5
        assert max_stack.popMax() == 5
        assert max_stack.top() == 1
        assert max_stack.peekMax() == 5
        assert max_stack.pop() == 1
        assert max_stack.top() == 5
        return True


    def tc_2(max_stack: MaxStack) -> bool:
        max_stack.push(79)
        max_stack.pop()
        # []
        max_stack.push(14)
        max_stack.push(67)
        max_stack.push(19)
        max_stack.push(-92)
        # [14, 67, 19, -92]
        max_stack.popMax()
        # [14, 19, -92]
        max_stack.push(77)
        max_stack.pop()
        # [14, 19, -92]
        max_stack.push(53)
        max_stack.push(5)
        # [14, 19, -92, 53, 5]
        assert max_stack.peekMax() == 53
        assert max_stack.popMax() == 53
        max_stack.push(12)
        return True


    def tc_3(max_stack: MaxStack) -> bool:
        max_stack.push(-23)
        assert max_stack.peekMax() == -23

        max_stack.push(-74)
        assert max_stack.popMax() == -23
        # [-74]

        max_stack.push(-4)
        max_stack.push(20)
        max_stack.push(68)
        # [-74, -4, 20, 68]

        assert max_stack.top() == 68
        max_stack.push(83)
        # [-74, -4, 20, 68, 83]

        assert max_stack.peekMax() == 83
        max_stack.push(73)
        # [-74, -4, 20, 68, 83, 73]

        assert max_stack.popMax() == 83
        assert max_stack.peekMax() == 73
        return True


    def tc_4(max_stack: MaxStack) -> bool:
        max_stack.push(5)
        assert max_stack.peekMax() == 5
        assert max_stack.popMax() == 5
        return True


    solutions = [MaxStack, MaxStack2]
    test_cases = [tc_1, tc_2, tc_3, tc_4]
    for sol in solutions:
        for tc in test_cases:
            assert tc(sol())
