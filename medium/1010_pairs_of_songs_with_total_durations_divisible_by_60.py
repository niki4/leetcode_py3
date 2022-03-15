"""
You are given a list of songs where the ith song has a duration of time[i] seconds.

Return the number of pairs of songs for which their total duration in seconds is divisible by 60.
Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.

Example 1:
    Input: time = [30,20,150,100,40]
    Output: 3
    Explanation: Three pairs have a total duration divisible by 60:
    (time[0] = 30, time[2] = 150): total duration 180
    (time[1] = 20, time[3] = 100): total duration 120
    (time[1] = 20, time[4] = 40): total duration 60

Example 2:
    Input: time = [60,60,60]
    Output: 3
    Explanation: All three pairs have a total duration of 120, which is divisible by 60.

Constraints:
    1 <= time.length <= 6 * 104
    1 <= time[i] <= 500
"""

from typing import List


class Solution:
    """
    Bruteforce solution - two loops

    Time complexity: O(n^2). TLE.
    Space complexity: O(1)
    """
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        pairs = 0
        for i in range(len(time)):
            for j in range(i+1, len(time)):
                if i != j and (time[i]+time[j]) % 60 == 0:
                    pairs += 1
        return pairs


class Solution2:
    """
    Time complexity: O(n). Accepted.
    Space complexity: O(1) - size of the count array is fixed.
    """
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        answer = 0
        count = [0] * 60  # each cell represent counter (for nummber 1-60 incl.)

        for t in time:
            rem = t % 60
            answer += count[(60 - rem) % 60]
            count[rem] += 1

        return answer


if __name__ == '__main__':
    solutions = (
        Solution(),
        Solution2(),
    )
    tc = (
        ([30,20,150,100,40], 3),
        ([60,60,60], 3),
        ([60,60,60,60], 6),
    )
    for sol in solutions:
        for inp_time, exp_pairs in tc:
            assert sol.numPairsDivisibleBy60(inp_time) == exp_pairs
