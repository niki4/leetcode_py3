"""
Given a collection of intervals, find the minimum number of intervals you need
to remove to make the rest of the intervals non-overlapping.

Note:

You may assume the interval's end point is always bigger than its start point.
Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.

Example 1:
Input: [ [1,2], [2,3], [3,4], [1,3] ] -> sort -> [[1, 2], [1, 3], [2, 3], [3, 4]]
Output: 1
Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
"""

class Solution:
    """
    Runtime: 740 ms, faster than 11.63% of Python3.
    Memory Usage: 15.1 MB, less than 85.54% of Python3.

    Brute force approach.
    Overhead on corner cases checks, pre-sorting intervals and mutating sorted_intervals.
    """
    def eraseOverlapIntervals(self, intervals: list) -> int:
        if len(intervals) <= 1:
            return 0

        sorted_intervals = sorted(intervals, key=lambda i: i[0])
        merges = 0
        idx = 1

        while idx < len(sorted_intervals):
            lower = sorted_intervals[idx-1]
            higher = sorted_intervals[idx]
            if lower[1] > higher[0]:
                merges += 1
                if lower[1] > higher[1]:
                    del sorted_intervals[idx-1]
                else:
                    del sorted_intervals[idx]
                idx = 1
                continue
            idx += 1
        return merges


class Solution2:
    """
    Runtime: 40 ms, faster than 89.06% of Python3.
    Memory Usage: 15 MB, less than 86.78% of Python3.

    Algorithm idea:
        Take interval with smallest end, remove all the bad ones overlapping it,
        and repeat (taking the one with smallest end of the remaining ones).
        For the overlap test, just keep track of the current end,
        initialized with negative infinity.
    """
    def eraseOverlapIntervals(self, intervals: list) -> int:
        intervals = sorted(intervals)
        end = float('-inf')
        count = 0
        for i in intervals:
            if i[0] >= end:
                end = i[1]
            elif i[1] <= end:
                count += 1
                end = i[1]
            else:
                count += 1
        return count


if __name__ == "__main__":
    s1 = Solution().eraseOverlapIntervals
    s2 = Solution2().eraseOverlapIntervals
    src1 = [[1,2], [2,3], [3,4], [1,3]]
    src2 = [[1,2], [1,2], [1,2]]
    src3 = [[1,2], [2,3]]
    src4 = [[1,2],]
    assert s1(src1) == s2(src1) == 1
    assert s1(src2) == s2(src2) == 2
    assert s1(src3) == s2(src3) == 0
    assert s1(src4) == s2(src4) == 0
