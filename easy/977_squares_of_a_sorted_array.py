"""
Given an array of integers A sorted in non-decreasing order,
return an array of the squares of each number, also in sorted
non-decreasing order.

Example 1:
Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]

Example 2:
Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]

Note:
1.  1 <= A.length <= 10000
2.  -10000 <= A[i] <= 10000
3.  A is sorted in non-decreasing order.
"""


class Solution:
    """
    Runtime: 212 ms, faster than 77.96% of Python3
    Memory Usage: 16.2 MB, less than 48.59% of Python3

    Simplest and pythonic solution, but not too fast.
    Time complexity: O(N logN) because of sorting
    Space complexity: O(n) for implicitly creating new list by sorted() function
    """

    def sortedSquares(self, A: list) -> list:
        return sorted([x ** 2 for x in A])


class Solution2:
    """
    Runtime: 216 ms, faster than 71.54% of Python3
    Memory Usage: 15.6 MB, less than 96.52% of Python3

    Set new values and sort in place.
    Time complexity: O(N logN)
    Space complexity: O(1)
    """

    def sortedSquares(self, A: list) -> list:
        for i in range(len(A)):
            A[i] = A[i] * A[i]
        A.sort()
        return A


class Solution3:
    """
    2-pointer approach. Since square of negative number is a positive number, we using abs() to both nums before comp.

    Runtime: 232 ms, faster than 43.69% of Python3
    Memory Usage: 16.1 MB, less than 68.56% of Python3

    Time complexity: O(n/2) which turns to O(n) because 2 is constant.
    Space complexity: O(n) as we allocate memory for result list.
    """

    def sortedSquares(self, A: list) -> list:
        start, end = 0, len(A) - 1
        result = []
        while start <= end:
            x = abs(A[start])
            y = abs(A[end])
            if x < y:
                result.append(y ** 2)
                end -= 1
            elif x > y:
                result.append(x ** 2)
                start += 1
            else:  # x == y
                result.append(x ** 2)
                if start != end:
                    result.append(y ** 2)
                start += 1
                end -= 1
        return result[::-1]


if __name__ == "__main__":
    def get_tc():
        return (
            ([-4, -1, 0, 3, 10], [0, 1, 9, 16, 100]),
            ([-7, -3, 2, 3, 11], [4, 9, 9, 49, 121])
        )


    solutions = (Solution(), Solution2(), Solution3())

    for s in solutions:
        for inp, exp in get_tc():
            res = s.sortedSquares(inp)
            assert res == exp, f'{s.__class__.__name__}: Expected {exp}, got {res}'
