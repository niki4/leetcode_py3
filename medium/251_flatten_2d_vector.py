"""
Design an iterator to flatten a 2D vector. It should support the next and hasNext operations.

Implement the Vector2D class:
    Vector2D(int[][] vec) initializes the object with the 2D vector vec.
    next() returns the next element from the 2D vector and moves the pointer one step forward.
    You may assume that all the calls to next are valid.
    hasNext() returns true if there are still some elements in the vector, and false otherwise.

Example 1:
Input
["Vector2D", "next", "next", "next", "hasNext", "hasNext", "next", "hasNext"]
[[[[1, 2], [3], [4]]], [], [], [], [], [], [], []]
Output
[null, 1, 2, 3, true, true, 4, false]

Explanation
    Vector2D vector2D = new Vector2D([[1, 2], [3], [4]]);
    vector2D.next();    // return 1
    vector2D.next();    // return 2
    vector2D.next();    // return 3
    vector2D.hasNext(); // return True
    vector2D.hasNext(); // return True
    vector2D.next();    // return 4
    vector2D.hasNext(); // return False


Constraints:
    0 <= vec.length <= 200
    0 <= vec[i].length <= 500
    -500 <= vec[i][j] <= 500
    At most 105 calls will be made to next and hasNext.
"""
from typing import List


class Vector2D:
    """
    Runtime: 88 ms, faster than 22.09% of Python3
    Memory Usage: 19.3 MB, less than 63.29% of Python3
    """

    def __init__(self, v: List[List[int]]):
        self.vector = v
        self.inner = 0
        self.outer = 0

    # If the current outer and inner point to an integer, this method does nothing.
    # Otherwise, inner and outer are advanced until they point to an integer.
    # If there are no more integers, then outer will be equal to vector.length
    # when this method terminates.
    def advance_to_next(self):
        # While outer is still within the vector, but inner is over the
        # end of the inner list pointed to by outer, we want to move
        # forward to the start of the next inner vector.
        while self.outer < len(self.vector) and self.inner == len(self.vector[self.outer]):
            self.outer += 1
            self.inner = 0

    def next(self) -> int:
        # Ensure the position pointers are moved such they point to an integer,
        # or put outer = vector.length.
        self.advance_to_next()
        # Return current element and move inner so that is after the current
        # element.
        result = self.vector[self.outer][self.inner]
        self.inner += 1
        return result

    def hasNext(self) -> bool:
        # Ensure the position pointers are moved such they point to an integer,
        # or put outer = vector.length.
        self.advance_to_next()
        # If outer = vector.length then there are no integers left, otherwise
        # we've stopped at an integer and so there's an integer left.
        return self.outer < len(self.vector)


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()


if __name__ == '__main__':
    v2d_1 = Vector2D([[1, 2], [3], [4]])
    assert v2d_1.next() == 1
    assert v2d_1.next() == 2
    assert v2d_1.next() == 3
    assert v2d_1.hasNext() is True
    assert v2d_1.hasNext() is True
    assert v2d_1.next() == 4
    assert v2d_1.hasNext() is False

    v2d_2 = Vector2D([[[]]])
    assert v2d_2.hasNext() is False
