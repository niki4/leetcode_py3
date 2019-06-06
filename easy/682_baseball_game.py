"""
You're now a baseball game point recorder.

Given a list of strings, each string can be one of the 4 following types:

1. Integer (one round's score): Directly represents the number of points
you get in this round.
2. "+" (one round's score): Represents that the points you get in this
round are the sum of the last two valid round's points.
3. "D" (one round's score): Represents that the points you get in this
round are the doubled data of the last valid round's points.
4. "C" (an operation, which isn't a round's score): Represents the last
valid round's points you get were invalid and should be removed.
Each round's operation is permanent and could have an impact on
the round before and the round after.

You need to return the sum of the points you could get in all the rounds.

Example 1:
    Input: ["5","2","C","D","+"]
    Output: 30
Explanation:
    Round 1: You could get 5 points. The sum is: 5.
    Round 2: You could get 2 points. The sum is: 7.
    Operation 1: The round 2's data was invalid. The sum is: 5.
    Round 3: You could get 10 points (the round 2's data has been removed). The sum is: 15.
    Round 4: You could get 5 + 10 = 15 points. The sum is: 30.

Note:
    The size of the input list will be between 1 and 1000.
    Every integer represented in the list will be between -30000 and 30000.
"""

class Solution:
    """
    Runtime: 36 ms, faster than 92.73% of Python3.
    Memory Usage: 13.1 MB, less than 86.75% of Python3.

    Stack holds values of previos computations and perfectly fits to this kind of problems.
    """
    def calPoints(self, ops: list) -> int:
        stack = []
        for round in ops:
            if round.lstrip('-').isdigit():
                stack.append(int(round))
            elif round == "C":
                if stack:
                    stack.pop()
            elif round == "D":
                stack.append(int(stack[-1])*2 if stack else 0)
            elif round == "+":
                if len(stack) >= 2:
                    stack.append(int(stack[-2]) + int(stack[-1]))
                elif len(stack) == 1:
                    stack.append(int(stack[-1]))
        return sum(stack)


if __name__ == "__main__":
    s = Solution()
    assert s.calPoints(["5","2","C","D","+"]) == 30
    assert s.calPoints(["5","-2","4","C","D","9","+","+"]) == 27
