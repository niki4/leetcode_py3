"""
Design a max stack data structure that supports the stack operations and supports finding the stack's maximum element.

Implement the MaxStack class:

MaxStack() Initializes the stack object.
void push(int x) Pushes element x onto the stack.
int pop() Removes the element on top of the stack and returns it.
int top() Gets the element on the top of the stack without removing it.
int peekMax() Retrieves the maximum element in the stack without removing it.
int popMax() Retrieves the maximum element in the stack and removes it. If there is more than one maximum element, only remove the top-most one.

Example 1:

Input
["MaxStack", "push", "push", "push", "top", "popMax", "top", "peekMax", "pop", "top"]
[[], [5], [1], [5], [], [], [], [], [], []]
Output
[null, null, null, null, 5, 5, 1, 5, 1, 5]

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

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_n = float('-inf')
        self.store = list()

    def push(self, x: int) -> None:
        """ Time complexity: O(1) """
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


if __name__ == '__main__':
    stk = MaxStack()
    stk.push(5)
    stk.push(1)
    stk.push(5)
    assert stk.store == [5, 1, 5]
    assert stk.max_n == 5

    assert stk.top() == 5
    assert stk.store == [5, 1, 5]

    assert stk.popMax() == 5
    assert stk.store == [5, 1]

    assert stk.top() == 1
    assert stk.store == [5, 1]

    assert stk.peekMax() == 5
    assert stk.store == [5, 1]

    assert stk.pop() == 1
    assert stk.store == [5]

    assert stk.top() == 5
    assert stk.store == [5]
