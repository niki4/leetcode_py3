"""
Given an integer array nums, design an algorithm to randomly shuffle the array.

Implement the Solution class:

Solution(int[] nums) Initializes the object with the integer array nums.
int[] reset() Resets the array to its original configuration and returns it.
int[] shuffle() Returns a random shuffling of the array.


Example 1:
Input: ["Solution", "shuffle", "reset", "shuffle"]
       [[[1, 2, 3]], [], [], []]
Output: [null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]
Explanation:
Solution solution = new Solution([1, 2, 3]);
solution.shuffle();    // Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3]
                            must be equally likely to be returned. Example: return [3, 1, 2]
solution.reset();      // Resets the array back to its original configuration [1,2,3]. Return [1, 2, 3]
solution.shuffle();    // Returns the random shuffling of array [1,2,3]. Example: return [1, 3, 2]
"""
from random import shuffle
from typing import List


class Solution:
    """
    Runtime: 268 ms, faster than 84.92% of Python3.
    Memory Usage: 19.3 MB, less than 75.51% of Python3.

    Maybe a bit cheating using std lib random module for shuffling the list.
    Time complexity: O(n)
    Space complexity: O(2*n) as we need to store two copy of list, this turns into O(n) as 2 is constant.
    """

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.original = nums[:]

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.nums[:] = self.original
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        shuffle(self.nums)
        return self.nums

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
