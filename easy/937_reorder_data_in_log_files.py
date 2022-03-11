"""
You are given an array of logs. Each log is a space-delimited string of words, where the first word is the identifier.

There are two types of logs:
    Letter-logs: All words (except the identifier) consist of lowercase English letters.
    Digit-logs: All words (except the identifier) consist of digits.

Reorder these logs so that:
    The letter-logs come before all digit-logs.
    The letter-logs are sorted lexicographically by their contents.
      If their contents are the same, then sort them lexicographically by their identifiers.
    The digit-logs maintain their relative ordering.
Return the final order of the logs.

Example 1:
    Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
    Output:       ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
Explanation:
    The letter-log contents are all different, so their ordering is "art can", "art zero", "own kit dig".
    The digit-logs have a relative order of "dig1 8 1 5 1", "dig2 3 6".

Example 2:
    Input: logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
    Output:       ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
"""

from typing import List


class Solution:
    """
    To ensure the order, we could define a tuple of 3 keys, (key_1, key_2, key_3), as follows:
        key_1: this key serves as a indicator for the type of logs. For the letter-logs, we could assign
            its key_1 with 0, and for the digit-logs, we assign its key_1 with 1. As we can see, thanks
            to the assigned values, the letter-logs would take the priority above the digit-logs.
        key_2: for this key, we use the content of the letter-logs as its value, so that among the
            letter-logs, they would be further ordered based on their content.
        key_3: similarly with the key_2, this key serves to further order the letter-logs. We will use
            the identifier of the letter-logs as its value, so that for the letter-logs with the same
            content, we could further sort the logs based on its identifier.

    Time Complexity: O(M⋅N⋅logN)
    Space Complexity: O(M⋅N)
    """
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def get_key(log):
            _id, rest = log.split(" ", maxsplit=1)
            return (0, rest, _id) if rest[0].isalpha() else (1, )

        return sorted(logs, key=get_key)


if __name__ == '__main__':
    sol = Solution()
