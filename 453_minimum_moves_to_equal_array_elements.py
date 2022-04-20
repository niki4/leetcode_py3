"""
Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.

In one move, you can increment n - 1 elements of the array by 1.
E.g., having nums = [1,2,3] (so that number of elements 'n' == 3, we can increment 3-1 == 2 elements at a time).

Constraints:
    n == nums.length
    1 <= nums.length <= 10^5
    -10^9 <= nums[i] <= 10^9
    The answer is guaranteed to fit in a 32-bit integer.
"""

from typing import List


class Solution:
    """
    Time complexity: O(n)
    Space complexity: O(1)

    Algorithm idea: the number of moves is the number of iterations that need
    to perform over elements (increments) except those that are in final state.
      We will continue iterate the most moves for the element that was minimal in the initial array.
      The sum of all elements is some abstract maximum state (that we never going to achive/exceed though).
      Then we need calculate minimal number that will increase on iterations (=len(nums)), by 1 at a time,
      so that min_n * len_nums. Finally we need to substract that result minimal number from abstract max:
      min_moves = sum_nums - (min_nums * len_nums)


    E.g. for the following inputs:
    [2, 3, 6]                       [2, 4, 6]
     3  4  7	1st step             3  5  7
     4  5  7	2nd                  4  6  8
     5  6  7	3rd                  5  7  8
     6  6  7	4th                  6  8  8
    [7  7  7]	5th (result)         7  8  8
                                    [8  8  8]   6th (result)
    sum = 11
    len = 3
    min = 2

    11 - 3*2 = 5 steps need
    """
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums) - min(nums) * len(nums)


if __name__ == '__main__':
    solutions = [Solution()]
    tc = (
        ([1, 2, 3], 3),
        ([2, 3, 6], 5),
        ([2, 4, 6], 6),
        ([0, 0], 0),
        ([1, 1, 1], 0),
        ([-1,1], 2),
    )
    for sol in solutions:
        for inp_nums, exp_res in tc:
            res = sol.minMoves(inp_nums)
            assert res == exp_res, f"For input {inp_nums} result {res} != {exp_res}."
