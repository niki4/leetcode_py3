"""
Given a non-empty string s and a dictionary wordDict containing
a list of non-empty words, add spaces in s to construct a sentence
where each word is a valid dictionary word. Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]
Example 2:

Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]
"""

class Solution:
    """
    Runtime: 128 ms, faster than 7.01% of Python3.
    Memory Usage: 13.2 MB, less than 78.45% of Python3.
    """
    def wordBreak(self, s: str, wordDict: list) -> list:
        res = []
        self.dfs(s, wordDict, '', res)
        return res

    def dfs(self, s: str, mem: dict, path, res):
        if self.check(s, mem):  # prune
            if not s:
                res.append(path[:-1])
                return          # backtrack
            for i in range(1, len(s)+1):
                if s[:i] in mem:
                    self.dfs(s[i:], mem, path+s[:i] + ' ', res)

    def check(self, s: str, mem: dict):
        """ check if a string can be splitted by using provided dict """
        dp = [False for _ in range(len(s)+1)]
        dp[0] = True
        for i in range(1, len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in mem:
                    dp[i] = True
        return dp[-1]


if __name__ == "__main__":
    sol = Solution()
    s1 = "catsanddog"
    wordDict1 = ["cat", "cats", "and", "sand", "dog"]
    expected1 = ['cat sand dog', 'cats and dog']
    assert sorted(sol.wordBreak(s1, wordDict1)) == expected1

    s2 = "pineapplepenapple"
    wordDict2 = ["apple", "pen", "applepen", "pine", "pineapple"]
    expected2 = ['pine apple pen apple', 'pine applepen apple', 'pineapple pen apple']
    assert sorted(sol.wordBreak(s2, wordDict2)) == expected2

    s3 = "catsandog"
    wordDict3 = ["cats", "dog", "sand", "and", "cat"]
    assert sol.wordBreak(s3, wordDict3) == []
