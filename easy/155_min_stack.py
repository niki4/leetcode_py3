"""
Design a stack that supports push, pop, top, and retrieving
the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

"""


class MinStack:

    """
    Runtime: 456 ms, faster than 24.20% of Python3 online submissions for Min Stack.
    Memory Usage: 16.7 MB, less than 5.18% of Python3 online submissions for Min Stack.
    """

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_idx = ''

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.min_idx = self.stack.index(min(self.stack))

    def pop(self) -> None:
        ret_val = self.stack.pop() if self.stack else []
        self.min_idx = self.stack.index(min(self.stack)) if self.stack else ''

        return ret_val

    def top(self) -> int:
        return self.stack[-1] if self.stack else self.stack

    def getMin(self) -> int:
        return self.stack[self.min_idx] if self.min_idx != '' else self.stack

    def __str__(self):
        return str(self.stack)


if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    assert minStack.getMin() == -3   # --> Returns -3
    minStack.pop()
    assert minStack.top() == 0       # --> Returns 0
    assert minStack.getMin() == -2   # --> Returns -2
