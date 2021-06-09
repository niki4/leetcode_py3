"""
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
Return the array in the form [x1,y1,x2,y2,...,xn,yn].

Example 1:
    Input: nums = [2,5,1,3,4,7], n = 3
    Output: [2,3,5,4,1,7]
    Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].

Constraints:
    1 <= n <= 500
    nums.length == 2n
    1 <= nums[i] <= 10^3
"""
from typing import List


class Solution:
    """
    Runtime: 64 ms, faster than 30.99% of Python3
    Memory Usage: 14.3 MB, less than 75.22% of Python3
    """

    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        for i in range(n):
            result += [nums[i], nums[n + i]]
        return result


if __name__ == '__main__':
    solutions = [Solution()]
    tc = (
        ([2, 5, 1, 3, 4, 7], 3, [2, 3, 5, 4, 1, 7]),
        ([1, 2, 3, 4, 4, 3, 2, 1], 4, [1, 4, 2, 3, 3, 2, 4, 1]),
        ([1, 1, 2, 2], 2, [1, 2, 1, 2]),
        ([1, 2], 1, [1, 2]),
    )
    for sol in solutions:
        for inp_nums, inp_n, exp_result in tc:
            assert sol.shuffle(inp_nums, inp_n) == exp_result
