"""
Given a sorted array nums, remove the duplicates in-place such that
each element appear only once and return the new length.

Do not allocate extra space for another array,
you must do this by modifying the input array in-place with O(1) extra memory.
"""


class Solution:
    """
    Runtime: 60 ms (Your runtime beats 99.65 % of python3 submissions.)src
    Note. An idiom nums[:] do not creates a new list and uses existing ones instead, so no extra memory overhead
    """
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # MEMORY ERROR :(
        # nums.sort()
        # for i in (x for x in nums if nums.count(x) > 1):
        #     while nums.count(i) > 1:
        #         nums.remove(i)
        # return nums

        nums[:] = set(nums) # set actually requires extra memory space, so Space Complexity is O(N)
        nums.sort()
        return len(nums)


class Solution2:
    """
    We using Two Pointer approach.
    Since the array is already sorted, we can keep two pointers ii and jj, where ii is the slow-runner while jj is the fast-runner. 
    As long as nums[i] = nums[j], we increment j to skip the duplicate.
    
    
    When we encounter nums[j] != nums[i], the duplicate run has ended so we must copy its value to nums[i+1]. 
    i is then incremented and we repeat the same process again until j reaches the end of array.
    
    Time: O(N)      - Runtime: 76 ms, faster than 89.83% of Python3
    Space: O(1)     - Memory Usage: 15.7 MB, less than 92.30% of Python3
    """
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i+1


if __name__ == '__main__':
    sol = Solution()
    print(sol.removeDuplicates([1, 1, 2, 1, 3, 1, 2, 4]))
