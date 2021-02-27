"""
Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Constraints:
    1 <= nums.length <= 10
    -10 <= nums[i] <= 10
    All the numbers of nums are unique.
"""
import itertools
from typing import List


class Solution:
    """
    Itertools provides a convenient method to get combination of elements with given size.

    Runtime: 36 ms, faster than 58.03% of Python3
    Memory Usage: 14.5 MB, less than 54.22% of Python3
    """

    def subsets(self, nums: List[int]) -> List[List[int]]:
        return [
            list(comb)
            for size in range(len(nums) + 1)
            for comb in itertools.combinations(nums, size)
        ]


class Solution2:
    """
    Backtrack Cascading: starting with [] we adding a new element (combination) extending the source combinations list
    which using for the subsequent iterations:

    E.g., with nums = [1, 2, 3] iterations will be like below:
        cmb: [[], [1]] -> add [1] to [] and get [1], then extend source list with that value
        cmb: [[], [1], [2], [1, 2]] -> first add [2] to [] (result [2]), then add [2] to [1] (result [1, 2]), extend cmb
        cmb: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

    Runtime: 36 ms, faster than 58.03% of Python3
    Memory Usage: 14.6 MB, less than 22.16% of Python3

    Time complexity: O(N * 2^N) to generate all subsets and then copy them into output list.
    Space complexity: O(N * 2^N). This is exactly the number of solutions for subsets multiplied by the number N
    of elements to keep for each subset. For a given number, it could be present or absent (i.e. binary choice) in a
    subset solution. As as result, for N numbers, we would have in total 2^N choices (solutions).
    """

    def subsets(self, nums: List[int]) -> List[List[int]]:
        cmb = [[]]
        for n in nums:
            cmb += [c + [n] for c in cmb]
        return cmb


if __name__ == '__main__':
    tc = (
        ([1, 2, 3], [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]),
        ([0], [[], [0]]),
    )
    solutions = [Solution(), Solution2()]
    for s in solutions:
        for inp_nums, exp_comb in tc:
            res = sorted(s.subsets(inp_nums))
            assert res == sorted(exp_comb)
