"""
Given a non-empty string s and a dictionary wordDict containing a list
of non-empty words, determine if s can be segmented into a space-separated
sequence of one or more dictionary words.

Note:
The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.

Example 1:
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
"""

class Solution:
    """
    Runtime: 44 ms, faster than 71.58% of Python3.
    Memory Usage: 13.1 MB, less than 85.95% of Python3.

    Dynamic programming approach.
    """
    def wordBreak(self, s: str, wordDict: list) -> bool:
        dp = [False] * (len(s)+1)
        dp[0] = True
        for i in range(1, len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
        return dp[-1]

class Solution2:
    """
    Runtime: 44 ms, faster than 71.58% of Python3.
    Memory Usage: 13.2 MB, less than 49.83% of Python3.

    Refactored version of the Solution 1. Has no any difference in terms of runtime complexity.
    """
    def wordBreak(self, s, wordDict):
        ok = [True]
        for i in range(1, len(s)+1):
            ok += any(ok[j] and s[j:i] in wordDict for j in range(i)),  # comma at the end creates tuple
        return ok[-1]


if __name__ == "__main__":
    sol1 = Solution()
    sol2 = Solution2()

    s1 = "leetcode"
    wordDict1 = ["leet", "code"]
    # assert sol1.wordBreak(s1, wordDict1)
    assert sol2.wordBreak(s1, wordDict1)

    # s2 = "applepenapple"
    # wordDict2 = ["apple", "pen"]
    # assert sol1.wordBreak(s2, wordDict2)
    # assert sol2.wordBreak(s2, wordDict2)

    # s3 = "catsandog"
    # wordDict3 = ["cats", "dog", "sand", "and", "cat"]
    # assert not sol1.wordBreak(s3, wordDict3)
    # assert not sol2.wordBreak(s3, wordDict3)
