"""
Given an array of integers arr, return true if the number of occurrences of each value in the array 
is unique, or false otherwise.


Example 1:
Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1.
             No two values have the same number of occurrences.

Constraints:
1 <= arr.length <= 1000
-1000 <= arr[i] <= 1000
"""

import collections
from typing import List

class Solution:
    """
    Runtime: 40 ms, faster than 71.91% of Python3
    Memory Usage: 14.1 MB, less than 69.98% of Python3

    Time/Space complexity: O(n)
    """
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        ctr = collections.Counter(arr)
        freq = ctr.values()
        # if there're non-unique counters, they will be omitted by set
        return len(freq) == len(set(freq))

if __name__ == '__main__':
    sol = Solution()
    test_cases = (
        ([1,2,2,1,1,3], True),
        ([1,2], False),
        ([-3,0,1,-3,1,1,1,-3,10,0], True))
    for inp_arr, exp_res in test_cases:
        assert sol.uniqueOccurrences(inp_arr) is exp_res

