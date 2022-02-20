"""
Given a non-empty array of non-negative integers nums, the degree of this array is defined as
the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has
the same degree as nums.

Example 1:
Input: nums = [1,2,2,3,1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.

Example 2:
Input: nums = [1,2,2,3,1,4,2]
Output: 6
Explanation: 
The degree is 3 because the element 2 is repeated 3 times.
So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.

Constraints:
nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.
"""
from typing import List

class Solution:
    """
    Time/Space complexity: O(n)
    """
    def findShortestSubArray(self, nums: List[int]) -> int:
        left, right, count = {}, {}, {}
        for i, x in enumerate(nums):
            if x not in left:
                left[x] = i
            right[x] = i
            count[x] = count.get(x, 0) + 1

        ans = len(nums)
        degree = max(count.values())
        for x in count:
            if count[x] == degree:
                ans = min(ans, right[x] - left[x] + 1)

        return ans


if __name__ == '__main__':
    sol = Solution()
    test_cases = (
        ([1,2,2,3,1], 2),
        ([1,2,2,3,1,4,2], 6))
    for inp_nums, exp_res in test_cases:
        assert sol.findShortestSubArray(inp_nums) == exp_res

