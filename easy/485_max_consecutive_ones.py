"""
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
"""
from typing import List


class Solution:
    """
    Compare seq len as you go

    Runtime: 352 ms, faster than 39.75% of Python3
    Memory Usage: 14.4 MB, less than 23.81% of Python3
    """

    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_seq = 0
        curr_seq = 0
        for n in nums:
            if n == 1:
                curr_seq += 1
            else:
                curr_seq = 0
            max_seq = max(max_seq, curr_seq)
        return max_seq


class Solution2:
    """
    Some python circus ;)

    Runtime: 388 ms, faster than 6.20% of Python3
    Memory Usage: 15.1 MB, less than 6.90% of Python3
    """

    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        one_seq_list = "".join([str(x) for x in nums]).split("0")
        return len(max(one_seq_list, key=len))


if __name__ == '__main__':
    solutions = [Solution(), Solution2()]
    tc = [
        ([1, 1, 0, 1, 1, 1], 3)
    ]
    for s in solutions:
        for inp, exp in tc:
            assert s.findMaxConsecutiveOnes(inp) == exp
