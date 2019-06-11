"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""

class Solution:
    """
    Runtime: 40 ms, faster than 99.31% of Python3.
    Memory Usage: 14.4 MB, less than 84.18% of Python3.
    """
    def merge(self, intervals: list) -> list:
        if len(intervals) <= 1:
            return intervals

        merged = []
        sorted_by_lower_bound = sorted(intervals, key=lambda i: i[0])

        for higher in sorted_by_lower_bound:
            if not merged:
                merged.append(higher)
            else:
                lower = merged[-1]
                if higher[0] <= lower[1]:
                    upper_bound = max(lower[1], higher[1])
                    merged[-1] = [lower[0], upper_bound]
                else:
                    merged.append(higher)
        return merged


if __name__ == "__main__":
    s = Solution()
    assert s.merge([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
