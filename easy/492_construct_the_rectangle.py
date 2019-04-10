"""
For a web developer, it is very important to know how to design a web page's size.
So, given a specific rectangular web page’s area, your job by now is to design a rectangular web page,
whose length L and width W satisfy the following requirements:

1. The area of the rectangular web page you designed must equal to the given target area.

2. The width W should not be larger than the length L, which means L >= W.

3. The difference between length L and width W should be as small as possible.
You need to output the length L and the width W of the web page you designed in sequence.

Example:
Input: 4
Output: [2, 2]
Explanation: The target area is 4, and all the possible ways to construct it are [1,4], [2,2], [4,1].
But according to requirement 2, [1,4] is illegal; according to requirement 3,  [4,1] is not optimal compared to [2,2].
So the length L is 2, and the width W is 2.
"""

import math


class Solution:
    """
    Runtime: 36 ms, faster than 94.23% of Python3.
    Memory Usage: 13.1 MB, less than 11.11% of Python3.
    """

    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        width = int(math.sqrt(area))
        while area % width != 0:
            width -= 1
        return [area // width, width]


if __name__ == '__main__':
    sol = Solution()
    assert sol.constructRectangle(1) == [1, 1]
    assert sol.constructRectangle(2) == [2, 1]
    assert sol.constructRectangle(4) == [2, 2]
    assert sol.constructRectangle(5) == [5, 1]
    assert sol.constructRectangle(6) == [3, 2]
    assert sol.constructRectangle(9) == [3, 3]
