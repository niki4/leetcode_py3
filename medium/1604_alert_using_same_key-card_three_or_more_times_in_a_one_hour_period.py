"""
LeetCode company workers use key-cards to unlock office doors. Each time a worker uses their key-card,
the security system saves the worker's name and the time when it was used. The system emits an alert if
any worker uses the key-card three or more times in a one-hour period.

You are given a list of strings keyName and keyTime where [keyName[i], keyTime[i]] corresponds to a person's
name and the time when their key-card was used in a single day.

Access times are given in the 24-hour time format "HH:MM", such as "23:51" and "09:49".

Return a list of unique worker names who received an alert for frequent keycard use. Sort the names in
ascending order alphabetically.

Notice that "10:00" - "11:00" is considered to be within a one-hour period, while "22:51" - "23:52" is not
considered to be within a one-hour period.

Example:
Input:
    keyName = ["daniel","daniel","daniel","luis","luis","luis","luis"],
    keyTime = ["10:00","10:40","11:00","09:00","11:00","13:00","15:00"]
Output: ["daniel"]
Explanation: "daniel" used the keycard 3 times in a one-hour period ("10:00","10:40", "11:00").
"""

import collections
from typing import List

class Solution:
    """
    Time complexity: O(m*KlogK)
    Not sure if I calculated complexity correctly. The overall algorithm is about splitting first unique names
    and find related times for each name. m in big O represents that set of unique names.

    Then for each name we sort related times in asc order (having K in big O denoting subset of times related
    to that particular name, we need KlogK to sort each times subset).

    Finally, use sliding window to find adjacent triples which makes an alert (hint: we can easily make
    timestamp by eliminating ":" symbol, then converting result value to int).
    """
    def parse_time(self, time_: str) -> int:
        """ Makes int representation of time, e.g. 12:30 -> 1230 """
        return int(time_[:2] + time_[3:])

    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        alerted = []
        visits = collections.defaultdict(list)

        for i in range(len(keyName)):
            visits[keyName[i]].append(keyTime[i])

        for name in visits:
            visits[name].sort()
            for i in range(2, len(visits[name])):
                p2_ts, p1_ts, curr_ts = [self.parse_time(t) for t in visits[name][i-2:i+1]]

                if curr_ts-100 <= p2_ts <= p1_ts <= curr_ts:
                    alerted.append(name)
                    break

        return sorted(alerted)


if __name__ == '__main__':
    solutions = [Solution()]
    tc = (
        (["daniel","daniel","daniel","luis","luis","luis","luis"], ["10:00","10:40","11:00","09:00","11:00","13:00","15:00"], ["daniel"]),
        (["alice","alice","alice","bob","bob","bob","bob"], ["12:01","12:00","18:00","21:00","21:20","21:30","23:00"], ["bob"]),
    )
    for sol in solutions:
        for key_names, key_times, exp_result in tc:
            assert sol.alertNames(key_names, key_times) == exp_result
