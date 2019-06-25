"""
Given an array of integers that is already sorted in ascending order,
find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that
they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you
may not use the same element twice.

Example:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
"""


class Solution:
    """
    Runtime: 36 ms, faster than 93.30% of Python3.
    Memory Usage: 13.4 MB, less than 90.99% of Python3.

    Two-pointers algorithm
    """
    def twoSum(self, numbers: list, target: int) -> list:
        l, r = 0, len(numbers)-1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l+1, r+1]
            elif s < target:
                l += 1
            else:
                r -= 1


class Solution2:
    """
    Runtime: 32 ms, faster than 98.74% of Python3.
    Memory Usage: 13.6 MB, less than 47.15% of Python3.

    Using hashmap to store/get num indexes in O(1) time.
    """
    def twoSum(self, numbers: list, target: int) -> list:
        seen = dict()
        for i, num in enumerate(numbers):
            diff = target - num
            if diff in seen:
                return sorted([i+1, seen[diff]+1])
            seen[num] = i


class Solution3:
    """
    Runtime: 28 ms, faster than 99.81% of Python3.
    Memory Usage: 13.5 MB, less than 73.85% of Python3.

    Binary search with some optimizations (e.g. do not recalculate for already
    processed num, stop iteration once we reached the num>target)
    """
    def twoSum(self, numbers: list, target: int) -> list:
        processed = set()
        for i, n in enumerate(numbers):
            if n in processed:
                continue
            if n > target:
                break

            left, right = i+1, len(numbers)-1
            diff = target - n
            while left <= right:
                mid = left + (right-left) // 2
                if numbers[mid] == diff:
                    return [i+1, mid+1]
                elif numbers[mid] < diff:
                    left = mid + 1
                else:
                    right = mid - 1
            processed.add(n)


if __name__ == "__main__":
    s1 = Solution().twoSum
    s2 = Solution2().twoSum
    s3 = Solution3().twoSum
    src1 = [0,0,3,4]
    exp1 = [1,2]
    src2 = [2,7,11,15]
    exp2 = [1,2]
    src3 = [3,24,50,79,88,150,345]
    exp3 = [3,6]
    assert s1(src1, 0) == s2(src1, 0) == s3(src1, 0) == exp1
    assert s1(src2, 9) == s2(src2, 9) == s3(src2, 9) == exp2
    assert s1(src3, 200) == s2(src3, 200) == s3(src3, 200) == exp3
