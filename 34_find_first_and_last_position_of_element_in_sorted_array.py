"""
Given an array of integers nums sorted in ascending order, 
find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1].

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Runtime: 40 ms, faster than 81.34% of Python3.
Memory Usage: 13.9 MB, less than 5.06% of Python3.
"""

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                L, R = mid, mid
                while L >= low and nums[L] == target:
                    L -= 1
                while R <= high and nums[R] == target:
                    R += 1
                return [L+1, R-1]
            if nums[low] <= target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return [-1, -1]
        
if __name__ == '__main__':
    inp1 = [5, 7, 7, 8, 8, 10]
    inp2 = [1]
    inp3 = [1, 2, 3]
    
    sol = Solution()
    assert sol.searchRange(inp1, 8) == [3, 4]
    assert sol.searchRange(inp1, 6) == [-1, -1]
    assert sol.searchRange(inp2, 1) == [0, 0]
    assert sol.searchRange(inp3, 3) == [2, 2]
    
