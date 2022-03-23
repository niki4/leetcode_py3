"""
Given an array of integers temperatures represents the daily temperatures, return an array answer such that
answer[i] is the number of days you have to wait after the ith day to get a warmer temperature.
If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Constraints:
    1 <= temperatures.length <= 105
    30 <= temperatures[i] <= 100
"""
from typing import List


class Solution:
    """
    Time complexity: O(n^2). TLE.
    """
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = []

        for i, curr_temp in enumerate(temperatures):
            j = i + 1

            while j < len(temperatures) and curr_temp >= temperatures[j]:
                j += 1

            if j < len(temperatures):
                answer.append(j - i)
            else:
                # there's no future days to wait for
                answer.append(0)

        return answer


class Solution2:
    """
    Monotonic stack approach.

    Time complexity: O(n)
    Space complexity: O(n)
    """
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []

        for curr_day, curr_temp in enumerate(temperatures):
            # pop from stack until the current day's temp is not warmer
            # than on the top of the stack.
            while stack and temperatures[stack[-1]] < curr_temp:
                prev_day = stack.pop()
                answer[prev_day] = curr_day - prev_day
            stack.append(curr_day)

        return answer


if __name__ == '__main__':
    solutions = (
        Solution(),
        Solution2(),
    )
    tc = [
        (
            [73,74,75,71,69,72,76,73],
            [1,1,4,2,1,1,0,0],
        ),
        (
            [30,40,50,60],
            [1,1,1,0],
        ),
        (
            [30,60,90],
            [1,1,0],
        ),
    ]

    for sol in solutions:
        for inp, expected in tc:
            result = sol.dailyTemperatures(inp)
            assert result == expected, f'{result} != {expected}'
