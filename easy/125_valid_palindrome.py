"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.
"""


class Solution:
    """
    Python built-in features

    Runtime: 48 ms, faster than 61.82% of Python3
    Memory Usage: 14.8 MB, less than 36.38% of Python3

    Time complexity: O(n)
    Space complexity: O(n)
    """

    def isPalindrome(self, s: str) -> bool:
        cleaned_s = "".join(filter(lambda x: x.isalnum(), s)).lower()
        return cleaned_s == cleaned_s[::-1]


class Solution2:
    """
    2-pointer approach

    Runtime: 52 ms, faster than 42.66% of Python3
    Memory Usage: 14.3 MB, less than 87.35% of Python3

    Time complexity: O(n)
    Space complexity: O(1)
    """

    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1  # i - left ptr, j - right ptr; they'll move to center
        while i < j:
            while not s[i].isalnum() and i < j:
                i += 1
            while not s[j].isalnum() and i < j:
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True


if __name__ == '__main__':
    solutions = [Solution(), Solution2()]
    tc = [
        ("", True),
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        ("!@#$%^&*(", False),
    ]
    for sol in solutions:
        for s, expected in tc:
            assert sol.isPalindrome(s) == expected
