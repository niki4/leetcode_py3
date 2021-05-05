"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element
always exists in the array.

Constraints:
    n == nums.length
    1 <= n <= 5 * 104
    -231 <= nums[i] <= 231 - 1

Follow-up: Could you solve the problem in linear time and in O(1) space?
"""

import collections
from typing import List


class Solution:
    """
    Runtime: 164 ms, faster than 69.01% of Python3
    Memory Usage: 15.4 MB, less than 95.44% of Python

    Time complexity: O(n log N) because of sorting
    Space complexity: O(n) for counter
    """

    def majorityElement(self, nums: List[int]) -> int:
        ctr = collections.Counter(nums)
        return sorted(ctr, key=ctr.get, reverse=True)[0]


class Solution2:
    """
    Runtime: 152 ms, faster than 97.49% of Python3
    Memory Usage: 15.6 MB, less than 48.80% of Python3

    Time complexity: O(n)
    Space complexity: O(n) for counter
    """

    def majorityElement(self, nums: List[int]) -> int:
        ctr = collections.Counter(nums)
        return max(ctr, key=ctr.get)


class Solution3:
    """
    Boyer-Moore Voting Algorithm (https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm)

    "maintain a count, which is incremented whenever we see an instance of our current candidate for majority element
    and decremented whenever we see anything else. Whenever count equals 0, we effectively forget about everything
    in nums up to the current index and consider the current number as the candidate for majority element.
    It is not immediately obvious why we can get away with forgetting prefixes of nums - consider the following
    examples (pipes are inserted to separate runs of nonzero count).
    [|7, 7, 5, 7, 5, 1 | 5, 7 | 5, 5, 7, 7 | 7, 7, 7, 7]
    (7)                 (5)    (5)          (7)             <- candidates
    on begin of each pipe we take the element as a candidate and count votes until we get counter=0 or reach the end.
    [+1 +1 -1 +1 -1 -1| +1 -1 |+1 +1 -1 -1 |+1 +1 +1 +1]
                   (0)     (0)          (0)          (4)    <- result of votes
    "

    Runtime: 160 ms, faster than 82.65% of Python3
    Memory Usage: 15.5 MB, less than 79.49% of Python3

    Time complexity: O(n)
    Space complexity: O(1)
    """

    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:  # start new vote
                candidate = num
            count += (1 if num == candidate else -1)
        return candidate


if __name__ == '__main__':
    solutions = [Solution(), Solution2(), Solution3()]
    tc = (
        ([3, 2, 3], 3),
        ([2, 2, 1, 1, 1, 2, 2], 2),
    )
    for sol in solutions:
        for inp_nums, exp_majority in tc:
            assert sol.majorityElement(inp_nums) == exp_majority
