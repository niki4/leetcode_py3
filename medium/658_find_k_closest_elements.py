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


class Solution2:
    """
    Binary Search To Find The Left Bound
        Algorithm idea: "If the element at arr[mid] is closer to x than arr[mid + k], then that means arr[mid + k], as
        well as every element to the right of it can never be in the answer. This means we should move our right pointer
        to avoid considering them. The logic is the same vice-versa - if arr[mid + k] is closer to x, then move the left
        pointer."

    Runtime: 272 ms, faster than 96.24% of Python3
    Memory Usage: 15.4 MB, less than 90.19% of Python3

    Time complexity: O(log(N-k) + k)
    Space complexity: O(1)
    """

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # init binary search bounds
        left, right = 0, len(arr) - k

        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] > arr[mid + k] - x:
                # left distance greater than right one
                left = mid + 1
            else:
                right = mid

        return arr[left:left + k]


if __name__ == '__main__':
    solutions = [Solution(), Solution2()]
    tc = (
        ([1, 2, 3, 4, 5], 4, 3, [1, 2, 3, 4]),
        ([1, 2, 3, 4, 5], 4, -1, [1, 2, 3, 4]),
    )
    for sol in solutions:
        for inp_arr, inp_k, inp_x, exp_res in tc:
            assert sol.findClosestElements(inp_arr, inp_k, inp_x) == exp_res
