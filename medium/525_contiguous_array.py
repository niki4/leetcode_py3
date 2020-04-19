"""
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

Note: The length of the given binary array will not exceed 50,000.
"""


class Solution:
    """
    Works fine, but got TimeLimit from LeetCode
    Time complexity : O(n^2). Space complexity : O(1).
    """

    def findMaxLength(self, nums) -> int:
        max_len = 0
        for i in range(len(nums)):
            for j in range(len(nums), i, -1):
                subarr = nums[i:j]
                if subarr.count(0) == subarr.count(1):
                    max_len = max(max_len, len(subarr))
        return max_len


class Solution2:
    """
    Runtime: 944 ms, faster than 27.70% of Python3.
    Memory Usage: 18.4 MB, less than 16.67% of Python3.

    Time: O(n). The entire array is traversed only once.
    Space: O(n). Max size of the HashMap map will be n, if all the elements are either 1 or 0.
    """

    def findMaxLength(self, nums) -> int:
        map = {0: -1}
        max_len, count = 0, 0
        for i in range(len(nums)):
            count += 1 if (nums[i] == 1) else -1
            if count in map:
                max_len = max(max_len, i - map.get(count))
            else:
                map[count] = i
        return max_len


if __name__ == "__main__":
    s1, s2 = Solution(), Solution2()
    assert s1.findMaxLength([0, 1, 0]) == 2
    assert s2.findMaxLength([0, 1, 0]) == 2
