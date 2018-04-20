"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Runtime: 32ms  (Your runtime beats 100.00 % of python3 submissions)
Status: Accepted  (https://leetcode.com/submissions/detail/150398490/)
"""


class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :return: int
        """
        s_list = s.split()
        return 0 if len(s_list) == 0 else len(s_list.pop())


if __name__ == '__main__':
    sol = Solution()
    print(sol.lengthOfLastWord("Hello World"))  # expected: 5 (for World)
    print(sol.lengthOfLastWord(" "))  # expected 0
