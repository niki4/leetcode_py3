"""
Design a stack that supports push, pop, top, and retrieving
the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

"""
import heapq


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


class MinStack2:
    """
    Using heap queue (a.k.a. priority queue, aka binary heap).
    The interesting property of a heap is that a[0] is always its smallest element.

    Runtime: 76 ms, faster than 28.80% of Python3
    Memory Usage: 18 MB, less than 62.65% of Python3
    """

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)  # O(1)
        heapq.heappush(self.min_stack, val)  # O(log n)

    def pop(self) -> None:
        del_num = self.stack.pop()  # O(1)
        for i, num in enumerate(self.min_stack):  # up to O(n)
            if num == del_num:
                # faster than just "del self.min_stack[i]"
                self.min_stack[i], self.min_stack[-1] = self.min_stack[-1], self.min_stack[i]  # O(1)
                self.min_stack.pop()  # O(1)
                heapq.heapify(self.min_stack)  # takes O(n)
                return

    def top(self) -> int:
        return self.stack[-1]  # O(1)

    def getMin(self) -> int:
        return self.min_stack[0]  # O(log n)


class MinStack3:
    """
    Using an array "stack" to store the elements placed in the stack, and an additional array "min_stack" tracking the
    minimum element seen so far. It can be proven that this approach always works, although it uses O(N) extra space.

    Time complexity for each operation: O(1)

    Runtime: 64 ms, faster than 47.65% of Python3
    Memory Usage: 18.2 MB, less than 46.74% of Python3
    """

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_stack.append(
            val if not self.min_stack else min(val, self.min_stack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


if __name__ == "__main__":
    solutions = [MinStack, MinStack2, MinStack3]
    for min_stack_impl in solutions:
        minStack = min_stack_impl()
        minStack.push(-2)
        minStack.push(0)
        minStack.push(-3)
        assert minStack.getMin() == -3  # --> Returns -3
        minStack.pop()
        assert minStack.top() == 0  # --> Returns 0
        assert minStack.getMin() == -2  # --> Returns -2
