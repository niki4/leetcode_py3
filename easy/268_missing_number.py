"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n,
find the one that is missing from the array.

Example 1:
Input: [3,0,1]
Output: 2

Example 2:
Input: [9,6,4,2,3,5,7,0,1]
Output: 8

Note:
Your algorithm should run in linear runtime complexity.
Could you implement it using only constant extra space complexity?
"""

class Solution:
    """
    Runtime: 36 ms, faster than 99.10% of Python3.
    Memory Usage: 15.4 MB, less than 5.15% of Python3.
    """
    def missingNumber(self, nums: list) -> int:
        return set(range(len(nums)+1)).difference(nums).pop()

class Solution2:
    """
    Runtime: 40 ms, faster than 97.18%.
    Memory Usage: 14.2 MB, less than 41.46%.

    Variation on Gauss formula (closed-form expression for the sum).
    This approach expects monotonic range of nums started from 0 with single missed num.
    """
    def missingNumber(self, nums: list) -> int:
        difference = 0
        for idx, val in enumerate(nums):
            difference += (val - idx)
        return len(nums) - difference


if __name__ == "__main__":
    s = Solution()
    s2 = Solution2()
    assert s.missingNumber([3,0,1]) == 2
    assert s.missingNumber([9,6,4,2,3,5,7,0,1]) == 8
    assert s.missingNumber([0]) == 1

    assert s2.missingNumber([3,0,1]) == 2
    assert s2.missingNumber([9,6,4,2,3,5,7,0,1]) == 8
    assert s2.missingNumber([0]) == 1
