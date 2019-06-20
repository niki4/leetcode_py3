"""
Given an array nums of n integers and an integer target,
are there elements a, b, c, and d in nums such that a + b + c + d = target?
Find all unique quadruplets in the array which gives the sum of target.

Note:
The solution set must not contain duplicate quadruplets.

Example:
Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""

class Solution:
    """
    Bruteforce solution aka 'We need to go deeper' :-)
    Doesn't accepted by LeetCode with Time Limit Exceeded

    Time complexity: O(n**4) because of nested for loops, O(n) for list comprehension and O(n logN) for sorted
    Space complexity: O(2*n) for additional storage in unique_sums set and result list
    """
    def fourSum(self, nums: list, target: int) -> list:
        unique_sums = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    for l in range(k+1, len(nums)):
                        elements = (nums[i], nums[j], nums[k], nums[l])
                        if sum(elements) == target:
                            unique_sums.add(tuple(sorted(elements)))

        return [list(s) for s in unique_sums]


class Solution2:
    """
    Runtime: 1244 ms, faster than 16.65% of Python3.
    Memory Usage: 13.4 MB, less than 30.93% of Python3.

    Universal algorithm that works for specified ksum, so we specified 4 when initially invoking ksum()
    """
    def fourSum(self, nums: list, target: int) -> list:
        nums.sort()
        def ksum(num, k, target):
            i = 0
            if k == 2:
                j = len(num) - 1
                while i < j:
                    if num[i] + num[j] == target:
                        yield (num[i], num[j])
                        i += 1
                    elif num[i] + num[j] > target:
                        j -= 1
                    else:
                        i += 1
            else:
                while i < len(num) - k + 1:
                    new_target = target - num[i]
                    for sub in ksum(num[i+1:], k-1, new_target):
                        yield (num[i],) + sub
                    i += 1

        return [list(s) for s in set(ksum(nums, 4, target))]


if __name__ == "__main__":
    s1 = Solution()
    s2 = Solution2()

    src1 = [1, 0, -1, 0, -2, 2]
    src2 = [-5,5,4,-3,0,0,4,-2]
    exp1 = [[-1, 0, 0, 1], [-2, -1, 1, 2], [-2,  0, 0, 2]]
    exp2 =[[-5,0,4,5], [-3,-2,4,5]]

    assert sorted(s1.fourSum(src1, 0)) == sorted(exp1)
    assert sorted(s1.fourSum(src2, 4)) == sorted(exp2)
    assert sorted(s2.fourSum(src1, 0)) == sorted(exp1)
    assert sorted(s2.fourSum(src2, 4)) == sorted(exp2)
