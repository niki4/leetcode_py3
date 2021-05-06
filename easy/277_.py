"""
Suppose you are at a party with n people (labeled from 0 to n - 1), and among them, there may exist one celebrity.
The definition of a celebrity is that all the other n - 1 people know him/her, but he/she does not know any of them.

Now you want to find out who the celebrity is or verify that there is not one. The only thing you are allowed to do is
to ask questions like: "Hi, A. Do you know B?" to get information about whether A knows B. You need to find out the
celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).

You are given a helper function bool knows(a, b) which tells you whether A knows B.
Implement a function int findCelebrity(n). There will be exactly one celebrity if he/she is in the party.
Return the celebrity's label if there is a celebrity in the party. If there is no celebrity, return -1.

Example 1:
            (2)->(0)->(1)   # (2) knows (0) (but not vice versa), and (0) knows (1)
            (0)->(1)<-(2)   # every one knows (1), but (1) itself knows no one
                 (2)        # no one knows (2)

Input: graph = [[1,1,0],[0,1,0],[1,1,1]]
Output: 1
Explanation: There are three persons labeled with 0, 1 and 2. graph[i][j] = 1 means person i knows person j, otherwise graph[i][j] = 0 means person i does not know person j. The celebrity is the person labeled as 1 because both 0 and 2 know him but 1 does not know anybody.
"""


# The knows API is already defined for you.
# return a bool, whether a knows b
def knows(a: int, b: int) -> bool:
    pass


class Solution:
    """
    @rozhkov solution (https://leetcode.com/problems/find-the-celebrity/solution/535824):
        If our candidate number after the first pass is C then we know that knows(C,x) == False for any x>C.
        We also know that there is one person (if C>0), let's call him prev, who knows C: knows(prev, C) == True

    Runtime: 1592 ms, faster than 94.37% of Python3
    Memory Usage: 14.6 MB, less than 14.77% of Python3
    """

    def findCelebrity(self, n: int) -> int:
        prev, candidate = 0, 0
        for i in range(1, n):
            if knows(candidate, i):  # our star shouldn't know anyone on the party, we need other candidate
                prev = candidate
                candidate = i
        return candidate if (
                all(not knows(candidate, x) for x in range(candidate)) and
                all(knows(x, candidate) for x in range(n) if x not in (prev, candidate))) else -1
