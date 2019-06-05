"""
Given a string S of lowercase letters, a duplicate removal consists
of choosing two adjacent and equal letters, and removing them.

We repeatedly make duplicate removals on S until we no longer can.

Return the final string after all such duplicate removals have been made.
It is guaranteed the answer is unique.

Example 1:
Input: "abbaca"
Output: "ca"

Explanation:
For example, in "abbaca" we could remove "bb" since the letters are
adjacent and equal, and this is the only possible move.  The result
of this move is that the string is "aaca", of which only "aa" is possible,
so the final string is "ca".

Note:
1 <= S.length <= 20000
S consists only of English lowercase letters.
"""

class Solution:
    """
    This is working solution, but got "Time Limit Exceeded" error on Leetcode
    """
    def removeDuplicates(self, S: str) -> str:
        dup_flag = True
        while dup_flag:
            for i in range(1, len(S)):
                if S[i-1] == S[i]:
                    S = S[:i-1] + S[i+1:]
                    break
            else:
                dup_flag = False
        return S


class Solution2:
    """
    This solution is also got "Time Limit Exceeded" error on Leetcode :-(
    """
    def removeDuplicates(self, S: str) -> str:
        if not S:
            return ''

        for i in range(1, len(S)):
            if S[i-1] == S[i]:
                if i == len(S)-1:
                    S = S[:i-1]
                else:
                    S = S[:i-1] + S[i+1:]
                return self.removeDuplicates(S)
        return S

class Solution3:
    """
    Runtime: 76 ms, faster than 82.87% of Python3.
    Memory Usage: 13.7 MB, less than 100.00% of Python3.
    """
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for char in S:
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)


if __name__ == "__main__":
    s = Solution()
    s2 = Solution2()
    s3 = Solution2()
    assert s.removeDuplicates("abbaca") == "ca"
    assert s2.removeDuplicates("abbaca") == "ca"
    assert s3.removeDuplicates("abbaca") == "ca"
