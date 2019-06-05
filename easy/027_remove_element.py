"""
Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array,
you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.
"""


class Solution:
    """
    Runtime: 40 ms, faster than 66.17% of Python3.
    Memory Usage: 13 MB, less than 91.97% of Python3.
    """
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        while val in nums:
            nums.remove(val)
        return len(nums)


class Solution2:
    """
    Runtime: 32 ms, faster than 97.14% of Python3.
    Memory Usage: 13.1 MB, less than 77.67% of Python3.

    Removing elements from end of array is more efficient
    as fewer rebuilds required after removing items.
    """
    def removeElement(self, nums: list, val: int) -> int:
        for idx in range(len(nums)-1, -1, -1):
            if nums[idx] == val:
                del nums[idx]
        return len(nums)


if __name__ == '__main__':
    s = Solution()
    s2 = Solution2()
    assert s.removeElement([3, 2, 2, 3], 3) == 2
    assert s.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2) == 5
    assert s2.removeElement([3, 2, 2, 3], 3) == 2
    assert s2.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2) == 5
