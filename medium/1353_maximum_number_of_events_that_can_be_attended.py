"""
Given an array of events where events[i] = [startDay-i, endDay-i].
Every event i starts at startDay-i and ends at endDay-i.

You can attend an event i at any day d where startTime-i <= d <= endTime-i.
Notice that you can only attend one event at any time d.

Return the maximum number of events you can attend.

Example 1:
    Input: events = [[1,2],[2,3],[3,4]]
    Output: 3
    Explanation: You can attend all the three events.  https://assets.leetcode.com/uploads/2020/02/05/e1.png
        One way to attend them all is as shown.
        Attend the first event on day 1.
        Attend the second event on day 2.
        Attend the third event on day 3.

Constraints:
    1 <= events.length <= 105
    events[i].length == 2
    1 <= startDayi <= endDayi <= 105
"""
import heapq
from typing import List


class Solution:
    """
    Heap Queue (aka Priority Queue)

    Runtime: 1008 ms, faster than 98.61% of Python3
    Memory Usage: 62.2 MB, less than 75.76% of Python3

    Time complexity: O(N logN)
    Space complexity: O(N)
    """

    def maxEvents(self, events: List[List[int]]) -> int:
        events = sorted(events, key=lambda e: e[0])  # by start date asc
        hq = list()  # store end times of opened events

        i, n = 0, len(events)
        events_attended, curr_day = 0, 0

        while i < n or hq:
            if not hq:
                curr_day = events[i][0]  # pick day as starting
            while i < n and events[i][0] == curr_day:
                # push end times of all events starting the same day as curr_day
                heapq.heappush(hq, events[i][1])
                i += 1

            # "attend an event" by discarding earliest end time
            heapq.heappop(hq)
            events_attended += 1

            curr_day += 1

            # discard all events that ends before new day starts
            if hq and curr_day > hq[0]:
                heapq.heappop(hq)
        return events_attended


if __name__ == '__main__':
    solutions = [Solution()]
    tc = (
        ([[1, 2], [2, 3], [3, 4]], 3),
        ([[1, 2], [2, 3], [3, 4], [1, 2]], 4),
        ([[1, 4], [4, 4], [2, 2], [3, 4], [1, 1]], 4),
        ([[1, 100000]], 1),
        ([[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7]], 7)
    )
    for sol in solutions:
        for inp_events, exp_attended_count in tc:
            result = sol.maxEvents(inp_events)
            assert result == exp_attended_count, f"{sol.__class__.__name__}: result {result} != {exp_attended_count}"
