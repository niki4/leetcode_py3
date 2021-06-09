"""
A string s of lowercase English letters is given. We want to partition this string into as many parts as possible so
that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:
    Input: s = "ababcbacadefegdehijhklij"
    Output: [9,7,8]
Explanation:
    The partition is "ababcbaca", "defegde", "hijhklij".
    This is a partition so that each letter appears in at most one part.
    A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.

Note:
    s will have length in range [1, 500].
    s will consist of lowercase English letters ('a' to 'z') only.
"""
from typing import List


class Solution:
    """
    Two pointer approach:
        1. First define initial borders (indexes of first and last occurrence of the same character,
        first letter in the range), let's mark them as start and end.
        2. Then move left marker toward right one letter by letter and check if there is in the rest subarray (from
        right marker to end of the initial array) such letter - if it is, then move right marker accordingly.
        3. When left marker meet right one we can be sure no letters from this subarray left in the rest subarray.
        We can calculate the size by just subtracting right-start position, then move onto next starting point.

    Runtime: 32 ms, faster than 96.09% of Python3
    Memory Usage: 14.3 MB, less than 55.74% of Python3

    Time complexity: O(n)
    Space complexity: O(1). By definition, s consists of English alphabet letters which size is 26, so our partitions
                    table cannot exceed the size of 26 too.
    """

    def partitionLabels(self, s: str) -> List[int]:
        start, end = 0, len(s)
        partitions = []

        while start < end:
            j = s.rfind(s[start], start + 1)
            if j == -1:
                # minimum possible partition as no such char in the rest of the list
                partitions.append(1)
                start += 1
            else:
                end = j + 1  # range inclusive, so j+1 to jump over partition
                left, right = start, end
                while left < right:
                    char = s[left]
                    i = s.rfind(char, right)  # highest idx of char starting from end index in s
                    if i >= right:
                        right = i + 1
                    left += 1
                partitions.append(right - start)
                start = right
            end = len(s)
        return partitions


if __name__ == '__main__':
    solutions = [Solution()]
    tc = (
        ("ababcbacadefegdehijhklij", [9, 7, 8]),
        ("caedbdedda", [1, 9]),
        ("qiejxqfnqceocmy", [13, 1, 1]),
    )
    for sol in solutions:
        for inp_s, exp_partitions in tc:
            result = sol.partitionLabels(inp_s)
            assert result == exp_partitions, f"{sol.__class__.__name__}: for input `{inp_s}`\n" \
                                             f"expected {exp_partitions}, got {result}"
