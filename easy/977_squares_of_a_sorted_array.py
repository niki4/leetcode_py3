"""
Given an array of integers A sorted in non-decreasing order,
return an array of the squares of each number, also in sorted
non-decreasing order.

Example 1:
Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]

Example 2:
Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]

Note:
1.  1 <= A.length <= 10000
2.  -10000 <= A[i] <= 10000
3.  A is sorted in non-decreasing order.
"""

class Solution:
    def sortedSquares(self, A: list) -> list:
        """
        Runtime: 172 ms, faster than 67.29% of Python3.
        Memory Usage: 15.1 MB, less than 53.36% of Python3.

        Simplest and pythonic solution, but not too fast.
        Runtime complexity: O(N logN)
        """
        return sorted([x**2 for x in A])


if __name__ == "__main__":
    s = Solution()
    assert s.sortedSquares([-4,-1,0,3,10]) == [0,1,9,16,100]
    assert s.sortedSquares([-7,-3,2,3,11]) == [4,9,9,49,121]
