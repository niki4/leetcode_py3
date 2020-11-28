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
        for idx in range(len(nums) - 1, -1, -1):
            if nums[idx] == val:
                del nums[idx]
        return len(nums)


class Solution3:
    def removeElement(self, nums, val):
        """
        Some sort of functional approach (requires space to hold temporary list though).

        Runtime: 36 ms, faster than 26.16% of Python3
        Memory Usage: 14 MB, less than 95.95% of Python3
        """
        nums[:] = list(filter(lambda n: n != val, nums))
        return len(nums)


class Solution4:
    """
    Two pointer approach.

    Runtime: 40 ms, faster than 26.16% of Python3
    Memory Usage: 14.1 MB, less than 38.02% of Python3
    """

    def removeElement(self, nums, val):
        k = 0  # idx where to insert next v non eq to val
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        for _ in range(len(nums) - k):
            nums.pop()
        return len(nums)


if __name__ == '__main__':
    def get_tc():
        return [
            ([3, 2, 2, 3], 3, 2),
            ([0, 1, 2, 2, 3, 0, 4, 2], 2, 5),
            ([3, 2, 2, 3], 3, 2),
            ([0, 1, 2, 2, 3, 0, 4, 2], 2, 5),
        ]


    solutions = [Solution(), Solution2(), Solution3(), Solution4()]

    for s in solutions:
        for inp_nums, inp_val, expected in get_tc():
            assert s.removeElement(inp_nums, inp_val) == expected
