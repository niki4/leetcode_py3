"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""
import itertools
from typing import List


class Solution:
    """
    Runtime: 32 ms, faster than 97.49% of Python3
    Memory Usage: 14.3 MB, less than 73.39% of Python3
    """

    def permute(self, nums: List[int]) -> List[List[int]]:
        # LC also accept "list(itertools.permutations(nums))", but it returns list of tuples rather than list of lists
        return [list(perm) for perm in itertools.permutations(nums)]


class Solution2:
    """
    Backtracking

    Explanation: https://media.geeksforgeeks.org/wp-content/cdn-uploads/NewPermutation.gif

    Runtime: 36 ms, faster than 89.98% of Python3
    Memory Usage: 14.4 MB, less than 46.67% of Python3

    Time complexity: at least O(n!) as we need to traverse all possible combinations;
    Space complexity: O(n!) since one has to keep N! solutions.
    """

    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first=0):
            # if all integers are used up
            if first == len(nums):
                result.append(nums[:])  # [:] makes a new list with copied vals
            for i in range(first, len(nums)):
                # place i-th integer first
                # in the current permutation
                nums[first], nums[i] = nums[i], nums[first]
                # use next integers to complete the permutations
                backtrack(first + 1)
                # backtrack
                nums[first], nums[i] = nums[i], nums[first]

        result = list()
        backtrack()
        return result


if __name__ == '__main__':
    solutions = [Solution()]  # Solution2 makes in place changes which are breaking tests
    tc = (
        ([1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
        ([0, 1], [[0, 1], [1, 0]]),
        ([1], [[1]]),
    )
    for s in solutions:
        for inp_nums, exp_perm in tc:
            res = s.permute(inp_nums)
            assert res == exp_perm
