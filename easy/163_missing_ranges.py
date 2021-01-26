"""
You are given an inclusive range [lower, upper] and a sorted unique integer array nums, where all elements are
in the inclusive range.

A number x is considered missing if x is in the range [lower, upper] and x is not in nums.

Return the smallest sorted list of ranges that cover every missing number exactly.
That is, no element of nums is in any of the ranges, and each missing number is in one of the ranges.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b

Example 1:

Input: nums = [0,1,3,50,75], lower = 0, upper = 99
Output: ["2","4->49","51->74","76->99"]
Explanation: The ranges are:
[2,2] --> "2"
[4,49] --> "4->49"
[51,74] --> "51->74"
[76,99] --> "76->99"
"""
from typing import List


class Solution:
    """
    TLE (Time Limit Exceeded)
    """

    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        nums = set(nums)
        ranges = []
        start, end = None, None
        for i in range(lower, upper + 1):
            if i not in nums:
                if start is None:
                    start = i
                    end = i
                else:
                    end = i
            elif start is not None:
                ranges.append(
                    f"{start}->{end}" if start != end else str(start))
                start, end = None, None
        if start is not None and end is not None:
            ranges.append(
                f"{start}->{end}" if start != end else str(start))
        return ranges


class Solution2:
    """
    Runtime: 20 ms, faster than 99.14% of Python3
    Memory Usage: 14.1 MB, less than 85.66% of Python3

    Time complexity : O(N), where N is the length of the input array. We are only iterating over the array once.
    Space complexity : O(N) if we take the output into account and O(1) otherwise, where N is the length of the
    input array. This is because we could have a missing range between each of the consecutive element
    of the input array. Hence, our output list that we need to return will be of size N.
    """

    def __init__(self):
        self.result = list()

    def add_range(self, low, high):
        if low + 2 == high:  # one num missed, e.g. low=1, high=3, missed=2
            self.result.append(str(low + 1))
        else:  # several nums missed, e.g. low=3, high=50, missed 4 to 49 so append "4->49"
            self.result.append(f"{low + 1}->{high - 1}")

    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        nums = [lower - 1] + nums + [upper + 1]
        for i in range(1, len(nums)):
            prev, curr = nums[i - 1], nums[i]
            if curr - prev > 1:
                self.add_range(prev, curr)
        return self.result


if __name__ == '__main__':
    solutions = [Solution, Solution2]
    tc = (
        ([0, 1, 3, 50, 75], 0, 99, ["2", "4->49", "51->74", "76->99"]),
        ([], 1, 1, ["1"]),  # The only missing range is [1,1], which becomes "1".
        ([], -3, -1, ["-3->-1"]),  # The only missing range is [-3,-1], which becomes "-3->-1".
        ([-1], -1, -1, []),  # There are no missing ranges since there are no missing numbers.
        ([-1], -2, -1, ["-2"]),
    )
    for s in solutions:
        for n, l, r, exp in tc:
            res = s().findMissingRanges(n, l, r)
            assert res == exp, f"{s.__class__.__name__}: input {(n, l, r)}\nexpected:\t{exp}\ngot:\t\t{res}"
