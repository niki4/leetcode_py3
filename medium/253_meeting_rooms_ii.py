"""
Given an array of meeting time intervals intervals where intervals[i] = [STARTi, ENDi],
return the minimum number of conference rooms required.

Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2

Example 2:
Input: intervals = [[7,10],[2,4]]
Output: 1

Constraints:
    1 <= intervals.length <= 104
    0 <= STARTi < ENDi <= 106
"""
import heapq
from typing import List


class Solution:
    """
    Algorithm (heapq):
        1. Sort intervals by their start time
        2. Use heapq (priority queue) which keeps their asc order after each insert/pop, so that min element is always
        first (and pop will return and discard that first element).
        3. We init heapq with first interval (end time)
        4. Iterate over the rest intervals, on each iteration check if start time of the new interval is greater than
        peak of heapq (min val) -> then we have room to free.
        5. Also on each iteration add to the heapq end time of the meeting.

        In other words, earliest ended rooms are released for next non overlapped meetings.
        E.g., we have some meeting started at 15:00 and ended at 17:00, we remember that its ended at 17:00 (in heapq).
        When next meeting coming at 18:00 (ending 20:00) we see that 18:00 is greater than 17:00 and pop() that old
        meeting from heapq and thus releasing our room. Straight after that we occupying room setting end time in heapq.

        Runtime: 76 ms, faster than 75.12% of Python3
        Memory Usage: 17.5 MB, less than 24.68% of Python3

        Time Complexity: O(NlogN).
                        Sorting takes O(NlogN).
                        heapq extract-min aka pop() takes O(log N) per operation and we could have N of them so O(NlogN)
        Space complexity: O(N). We need to store up to N elements in both heapq and copy of sorted intervals.
    """

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        rooms = []
        intervals = sorted(intervals, key=lambda x: x[0])  # 1
        heapq.heappush(rooms, intervals[0][1])  # 3

        for i in intervals[1:]:
            if i[0] >= rooms[0]:  # 4
                heapq.heappop(rooms)
            heapq.heappush(rooms, i[1])  # 5
        return len(rooms)


if __name__ == '__main__':
    solutions = [Solution()]
    tc = (
        ([[0, 30], [5, 10], [15, 20]], 2),
        ([[7, 10], [2, 4]], 1)
    )
    for s in solutions:
        for inp_intervals, exp_rooms in tc:
            assert s.minMeetingRooms(inp_intervals) == exp_rooms
