"""
You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from
s and removing them, causing the left and the right side of the deleted substring to concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.

Example 1:
    Input: s = "abcd", k = 2
    Output: "abcd"
    Explanation: There's nothing to delete.
Example 2:
    Input: s = "deeedbbcccbdaa", k = 3
    Output: "aa"
    Explanation:
    First delete "eee" and "ccc", get "ddbbbdaa"
    Then delete "bbb", get "dddaa"
    Finally delete "ddd", get "aa"
Example 3:
    Input: s = "pbbcggttciiippooaais", k = 2
    Output: "ps"

Constraints:
    1 <= s.length <= 105
    2 <= k <= 104
    s only contains lower case English letters.
"""


class Solution:
    """
    Bruteforce. Working solution, but got TLE from LC.

    Time complexity:O(n^2 / k), where n is a string length. We scan the string no more than n/k times.
    Space complexity: O(1). A copy of a string may be created in some languages, however,
                      the algorithm itself only uses the current string.
    """

    def removeDuplicates(self, s: str, k: int) -> str:
        i = k
        while i <= len(s):
            substr = s[i - k:i]
            if len(substr) == k and len(set(substr)) == 1:
                s = s[:i - k] + s[i:]  # remove adjacent dups of size k
                if (i - k) < k:
                    i = k
                else:
                    i -= k
            else:
                i += 1
        return s


class Solution2:
    """
    Also got TLE, huh

    Time complexity: O(n^3) or so
    """

    def removeDuplicates(self, s: str, k: int) -> str:
        while any(ch * k in s for ch in set(s)):
            for char in set(s):
                s = s.replace(char * k, "")
        return s


if __name__ == '__main__':
    solutions = [Solution(), Solution2()]
    tc = (
        ("abcd", 2, "abcd"),
        ("deeedbbcccbdaa", 3, "aa"),
        ("pbbcggttciiippooaais", 2, "ps"),
        ("yfttttfbbbbnnnnffbgffffgbbbbgssssgthyyyy", 4, "ybth"),
    )
    for sol in solutions:
        for inp_s, inp_k, exp_str in tc:
            result = sol.removeDuplicates(inp_s, inp_k)
            assert result == exp_str, f"{sol.__class__.__name__}: for input s=`{inp_s}`, k=`{inp_k}` " \
                                      f"expected result `{exp_str}`, got `{result}`."
