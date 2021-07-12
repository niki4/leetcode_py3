"""
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array.
The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:
    |a - x| < |b - x|, or
    |a - x| == |b - x| and a < b

Example 1:
    Input: arr = [1,2,3,4,5], k = 4, x = 3
    Output: [1,2,3,4]
Example 2:
    Input: arr = [1,2,3,4,5], k = 4, x = -1
    Output: [1,2,3,4]

Constraints:
    1 <= k <= arr.length
    1 <= arr.length <= 104
    arr is sorted in ascending order.
    -104 <= arr[i], x <= 104
"""
from typing import List


class Solution:
    """
    Sort With Custom Comparator

    Time complexity: O(N logN) + (K logK)
    Space complexity: O(n)
    """

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # sort using custom comparator, denoting closest numbers first
        sorted_arr = sorted(arr, key=lambda num: abs(x - num))

        # take only k closest numbers
        result = sorted_arr[:k]

        # return elements sorted in ascending order
        return sorted(result)


if __name__ == '__main__':
    solutions = [Solution()]
    tc = (
        ([1, 2, 3, 4, 5], 4, 3, [1, 2, 3, 4]),
        ([1, 2, 3, 4, 5], 4, -1, [1, 2, 3, 4]),
    )
    for sol in solutions:
        for inp_arr, inp_k, inp_x, exp_res in tc:
            assert sol.findClosestElements(inp_arr, inp_k, inp_x) == exp_res
