"""
Given an array A of strings made only from lowercase letters,
return a list of all characters that show up in all strings within
the list (including duplicates).  For example, if a character occurs 3 times
in all strings but not 4 times, you need to include that character three times
in the final answer.

You may return the answer in any order.

Example 1:

Input: ["bella","label","roller"]
Output: ["e","l","l"]

Example 2:
Input: ["cool","lock","cook"]
Output: ["c","o"]

Note:
1 <= A.length <= 100
1 <= A[i].length <= 100
A[i][j] is a lowercase letter
"""

class Solution:
    """
    Runtime: 40 ms, faster than 99.37% of Python3.
    Memory Usage: 13.2 MB, less than 58.30% of Python3.

    Casting to 'set' is the best way to find unique items in Python.
    """
    def commonChars(self, A: list) -> list:
        if len(A) == 1:
            return list(A[0])

        init_word = A[0]
        letters = set(init_word)
        for idx in range(1, len(A)):
            letters.intersection_update(A[idx])

        result = []
        for ltr in letters:
            result += [ltr] * min(word.count(ltr) for word in A)
        return result


if __name__ == "__main__":
    s = Solution()
    assert sorted(s.commonChars(["bella","label","roller"])) == sorted(["e","l","l"])
    assert sorted(s.commonChars(["cool","lock","cook"])) == sorted(["c","o"])
