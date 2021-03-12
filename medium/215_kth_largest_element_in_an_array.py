"""
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.


Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

Constraints:
    1 <= k <= nums.length <= 104
    -104 <= nums[i] <= 104
"""
import heapq
import random
from typing import List


class Solution:
    """
    Sort array, then take k-th element (-1 because input starting from 1)

    Time complexity: O(n logN) because of sorting
    Space complexity: O(n) to store sorted array
    """

    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = sorted(nums, reverse=True)
        return nums[k - 1]


class Solution2:
    """
    Heap queue

    Runtime: 60 ms, faster than 88.37% of Python3
    Memory Usage: 15.2 MB, less than 18.76% of Python3

    Time complexity: O(N logK). The time complexity of adding an element in a heap of size K is O(logK), and we do it
    N times that means (N logK) time complexity for the algorithm.
    Space complexity: O(k) to store the heap elements.
    """

    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]


class Solution3:
    """
    Algorithm (Quickselect):
        1. Choose a random pivot.
        2. Use a partition algorithm to place the pivot into its perfect position pos in the sorted array,
        move smaller elements to the left of pivot, and larger or equal ones - to the right.
        3. Compare pos and N - k to choose the side of array to proceed recursively.

    Runtime: 64 ms, faster than 72.48% of Python3
    Memory Usage: 15.1 MB, less than 44.88% of Python3

    Time complexity: O(N) in the average case, O(N^2) in the worst case.
    Space complexity: O(1).
        The recursive implementation here can be implemented with a while loop, and thus reduce the space to O(1).
        Quick select modified the input array immediately, just like may in-place sorting algorithm.
    """

    def partition(self, left, right, pivot_index, nums):
        pivot = nums[pivot_index]
        # 1. move pivot to end
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]

        # 2. move all smaller elements to the left
        store_index = left
        for i in range(left, right):
            if nums[i] < pivot:
                nums[store_index], nums[i] = nums[i], nums[store_index]
                store_index += 1

        # 3. move pivot to its final place
        nums[right], nums[store_index] = nums[store_index], nums[right]
        return store_index

    def select(self, left, right, k_smallest, nums):
        """
        Returns the k-th smallest element of list within left..right
        """
        if left == right:  # If the list contains only one element,
            return nums[left]  # return that element

        # select a random pivot_index between
        pivot_index = random.randint(left, right)

        # find the pivot position in a sorted list
        pivot_index = self.partition(left, right, pivot_index, nums)

        if k_smallest == pivot_index:  # pivot in its final sorted position
            return nums[k_smallest]
        elif k_smallest < pivot_index:  # go left
            return self.select(left, pivot_index - 1, k_smallest, nums)
        else:  # go right
            return self.select(pivot_index + 1, right, k_smallest, nums)

    def findKthLargest(self, nums: List[int], k: int) -> int:
        # K-th largest is (n - k)th smallest
        return self.select(0, len(nums) - 1, len(nums) - k, nums)


if __name__ == '__main__':
    solutions = [Solution(), Solution2(), Solution3()]
    tc = (
        ([3, 2, 1, 5, 6, 4], 2, 5),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4)
    )
    for s in solutions:
        for inp_nums, inp_k, exp in tc:
            assert s.findKthLargest(inp_nums, inp_k) == exp
