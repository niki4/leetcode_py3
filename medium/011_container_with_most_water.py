"""
Given n non-negative integers a1, a2, ..., an , where each represents
a point at coordinate (i, ai). n vertical lines are drawn such that
the two endpoints of line i is at (i, ai) and (i, 0). Find two lines,
which together with x-axis forms a container, such that the container
contains the most water.

Note: You may not slant the container and n is at least 2.

https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg
The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
In this case, the max area of water (blue section)
the container can contain is 49.
"""

class Solution:
    """
    Time limit exceeded for this solution on Leetcode.

    Bruteforce approach:
    In this case, we will simply consider the area for every possible pair
    of the lines and find out the maximum area out of those.

    Runtime complexity: O(N**2)
    Space complexity: O(1)
    """
    def maxArea(self, height: list) -> int:
        max_area = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                max_area = max(max_area, min(height[i], height[j]) * (j - i))
        return max_area


class Solution2:
    """
    Runtime: 68 ms, faster than 56.96% of Python3.
    Memory Usage: 14.5 MB, less than 59.22% of Python3.

    Two Pointer Approach:
    We take two pointers, one at the beginning and one at the end of the array
    constituting the length of the lines. Futher, we maintain a variable maxarea
    to store the maximum area obtained till now. At every step, we find out the
    area formed between them, update maxarea and move the pointer pointing to the
    shorter line towards the other end by one step.

    Runtime complexity: O(N)
    Space complexity: O(1)
    """
    def maxArea(self, height: list) -> int:
        max_area = 0
        l = 0
        r = len(height)-1
        while (l < r):
            max_area = max(max_area, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area


if __name__ == "__main__":
    s = Solution()
    s2 = Solution2()
    src_1 = [1,8,6,2,5,4,8,3,7]
    exp_1 = 49
    assert s.maxArea(src_1) == exp_1
    assert s2.maxArea(src_1) == exp_1
