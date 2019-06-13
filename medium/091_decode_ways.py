"""
A message containing letters from A-Z is being encoded to numbers
using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total
number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as
"BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
"""

class Solution:
    """
    Runtime: 36 ms, faster than 93.08% of Python3.
    Memory Usage: 13 MB, less than 94.46% of Python3.

    Dynamic programming approach.
    Runtime complexity: O(n)
    Space complexity: O(1)
    """
    def numDecodings(self, s: str) -> int:
        dp = [0] * 3
        dp[0] = 1
        for i in range(1, len(s)+1):
            dp[i%3] = 0
            if s[i-1] != '0':
                dp[i%3] += dp[(i-1)%3]
            if i > 1 and 10 <= int(s[i-2: i]) <= 26:
                dp[i%3] += dp[(i-2)%3]
        return dp[len(s)%3] if s else 0


if __name__ == "__main__":
    s = Solution()
    assert s.numDecodings("12") == 2
    assert s.numDecodings("226") == 3
