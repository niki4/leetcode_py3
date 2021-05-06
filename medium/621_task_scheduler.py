"""
Given a characters array tasks, representing the tasks a CPU needs to do,
where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time.
For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter
in the array), that is that there must be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks.

Example 1:
    Input: tasks = ["A","A","A","B","B","B"], n = 2
    Output: 8
    Explanation:
    A -> B -> idle -> A -> B -> idle -> A -> B
    There is at least 2 units of time between any two same tasks.
"""
from typing import List


class Solution:
    """
    Greedy approach:
         The total number of CPU intervals we need consists of busy and idle slots.
         Number of busy slots is defined by the number of tasks to execute: len(tasks).
         The problem is to compute a number of idle slots.

         Maximum possible number of idle slots is defined by the frequency of the
         most frequent task: idle_time <= (f_max - 1) * n.

         A B A A B C A A
         A (idle)(idle) A (idle)(idle) A (idle)(idle) A (idle)(idle) A

    Runtime: 412 ms, faster than 50.56% of Python3
    Memory Usage: 14.8 MB, less than 48.44% of Python3

    Time complexity: O(n) as we need to traverse tasks list
    Space complexity: O(1) because frequencies list has constant space
    """

    def leastInterval(self, tasks: List[str], n: int) -> int:
        # frequencies of the tasks
        frequencies = [0] * 26
        for t in tasks:
            frequencies[ord(t) - ord('A')] += 1

        frequencies.sort()
        freq_max = frequencies.pop()  # max frequency
        idle_time = (freq_max - 1) * n

        while frequencies and idle_time > 0:
            idle_time -= min(freq_max - 1, frequencies.pop())
        idle_time = max(idle_time, 0)

        return idle_time + len(tasks)


class Solution2:
    """
    Math approach

    There are two possible situations:
    1. The most frequent task is not frequent enough to force the presence of idle slots.
        A B C D E A F A
        A(BC)A(DE)A(F)
    2. The most frequent task is frequent enough to force some idle slots.
        A B A A B C A A
        A(BC)A(B)(idle)A(idle idle)A(idle idle)A
    The answer is the maximum between these two.
        (Fmax - 1) * (n + 1) + Nmax

    Runtime: 396 ms, faster than 67.39% of Python3
    Memory Usage: 14.8 MB, less than 69.92% of Python3

    Time complexity: O(n) as we need to traverse tasks list
    Space complexity: O(1) because frequencies list has constant space
    """

    def leastInterval(self, tasks: List[str], n: int) -> int:
        # frequencies of the tasks
        frequencies = [0] * 26
        for t in tasks:
            frequencies[ord(t) - ord('A')] += 1

        freq_max = max(frequencies)
        n_freq_max = frequencies.count(freq_max)  # count tasks that most frequent

        return max(len(tasks), (freq_max - 1) * (n + 1) + n_freq_max)


if __name__ == '__main__':
    solutions = [Solution(), Solution2()]
    tc = (
        (["A", "A", "A", "B", "B", "B"], 2, 8),
        (["A", "A", "A", "B", "B", "B"], 0, 6),
        (["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2, 16),
    )
    for sol in solutions:
        for inp_tasks, inp_n, exp_units in tc:
            result = sol.leastInterval(inp_tasks, inp_n)
            assert result == exp_units, f"{result} != {exp_units}"
