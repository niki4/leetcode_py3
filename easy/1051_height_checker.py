"""
Students are asked to stand in non-decreasing order of heights for
an annual photo.

Return the minimum number of students not standing in the right positions.
(This is the number of students that must move in order for all students
to be standing in non-decreasing order of height.)

Example 1:
Input: [1,1,4,2,1,3]
Output: 3
Explanation:
Students with heights 4, 3 and the last 1 are not standing in the right
positions.

Note:
1 <= heights.length <= 100
1 <= heights[i] <= 100
"""

class Solution:
    """
    Runtime: 36 ms, faster than 59.83% of Python3.
    Memory Usage: 13.2 MB, less than 100.00% of Python3.
    """
    def heightChecker(self, heights: list) -> int:
        counter = 0
        for idx, h in enumerate(sorted(heights)):
            if heights[idx] != h:
                counter += 1
        return counter


if __name__ == "__main__":
    s = Solution()
    assert s.heightChecker([1, 1, 4, 2, 1, 3]) == 3
