"""
Write a function that reverses a string.
The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying
the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.
"""
from typing import List


class Solution:
    """
    2-pointers Recursive approach

    Runtime: 196 ms, faster than 67.49% of Python3
    Memory Usage: 45.3 MB, less than 5.01% of Python3

    Time complexity: O(N) to swap N/2 elements
    Space complexity: O(1) for array storage, but here we also need O(N) for recursive stack
    """

    def reverseString(self, s: List[str]) -> None:
        def helper(left, right):
            if left < right:
                s[left], s[right] = s[right], s[left]
                helper(left + 1, right - 1)

        helper(0, len(s) - 1)


class Solution2:
    """
    2-pointers Iterative

    Runtime: 196 ms, faster than 67.49% of Python3
    Memory Usage: 18.4 MB, less than 44.76% of Python3
    """

    def reverseString(self, s: List[str]) -> None:
        i = 0
        j = len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1


class Solution3:
    """
    Python built-in method

    Runtime: 188 ms, faster than 91.57% of Python3
    Memory Usage: 18.5 MB, less than 44.76% of Python3
    """

    def reverseString(self, s: List[str]) -> None:
        s.reverse()


if __name__ == '__main__':
    def get_tc():
        return [
            (["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"]),
            (["H", "a", "n", "n", "a", "h"], ["h", "a", "n", "n", "a", "H"]),
        ]


    solutions = [Solution(), Solution2(), Solution3()]

    for s in solutions:
        for case, expected in get_tc():
            s.reverseString(case)
            assert case == expected
