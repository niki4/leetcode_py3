"""
Given an array of meeting time intervals where intervals[i] = [start(i), end(i)],
determine if a person could attend all meetings.

Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: false

Example 2:
Input: intervals = [[7,10],[2,4]]
Output: true

Constraints:
    0 <= intervals.length <= 104
    intervals[i].length == 2
    0 <= starti < endi <= 106
"""
from typing import List


class Solution:
    """
    Runtime: 72 ms, faster than 79.36% of Python3
    Memory Usage: 17.4 MB, less than 53.15% of Python3

    Time complexity: O(n logN)+O(k) because of sorting O(n logN) intervals prior traversing which takes O(n), slice O(k)
    Space complexity: O(n) to store sorted intervals. Could be reduced to O(1) if sort in place (aware of side-effect).
    """

    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True

        intervals = sorted(intervals, key=lambda x: x[0])  # sort by start time
        prev = intervals[0]
        for i in intervals[1:]:  # this line can be easily optimized it to avoid slicing altogether
            if i[0] < prev[1]:  # overlap: new meeting starts before previous ends
                return False
            prev = i
        return True


if __name__ == '__main__':
    sol = Solution()
    tc = (
        ([[0, 30], [5, 10], [15, 20]], False),
        ([[7, 10], [2, 4]], True),
        ([[13, 15], [1, 13]], True),
        ([], True),
    )
    for inp_intervals, exp_res in tc:
        res = sol.canAttendMeetings(inp_intervals)
        assert res is exp_res, f"For input {inp_intervals} - Expected {exp_res}, got {res}"
