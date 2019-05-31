"""
We are given two sentences A and B.
(A sentence is a string of space separated words.
Each word consists only of lowercase letters.)

A word is uncommon if it appears exactly once in one
of the sentences, and does not appear in the other sentence.

Return a list of all uncommon words.

You may return the list in any order.
"""

from collections import Counter

class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> list:
        """
        Runtime: 36 ms, faster than 91.68% of Python3.
        Memory Usage: 13.2 MB, less than 57.93% of Python3.
        """
        count = Counter(A.split())
        count += Counter(B.split())
        return [w for w in count if count[w] == 1]

    def uncommonFromSentences2(self, A: str, B: str) -> list:
        """
        Runtime: 36 ms, faster than 91.68% of Python3.
        Memory Usage: 13.1 MB, less than 67.25% of Python3.

        Actually, the same approach as with collections.Counter, but without it.
        """
        a_words = A.split()
        b_words = B.split()

        count = {w: a_words.count(w) for w in a_words}

        for w in b_words:
            if w in count:
                count[w] += b_words.count(w)
            else:
                count[w] = b_words.count(w)
        return [w for w in count if count[w] == 1]


if __name__ == "__main__":
    s1 = Solution().uncommonFromSentences
    s2 = Solution().uncommonFromSentences2

    a1 = "this apple is sweet"
    b1 = "this apple is sour"
    expected1 = ["sweet","sour"]

    a2 = "apple apple"
    b2 = "banana"
    expected2 = ["banana"]

    a3 = "s z z z s"
    b3 = "s z ejt"
    expected3 = ["ejt"]

    a4 = "op vu kux dn jsenj hbdez hbdez nbenh z op dxmqd op"
    b4 = "kux wnx wnx wbi jsenj nlgfn vu f vu fvxas dn op tb"
    expected4 = ["nbenh","dxmqd","z","nlgfn","fvxas","f","tb","wbi"]

    assert sorted(s1(a1, b1)) == sorted(expected1)
    assert s1(a2, b2) == expected2
    assert sorted(s1(a3, b3)) == expected3
    assert sorted(s1(a4, b4)) == sorted(expected4)

    assert sorted(s2(a1, b1)) == sorted(expected1)
    assert s2(a2, b2) == expected2
    assert sorted(s2(a3, b3)) == expected3
    assert sorted(s2(a4, b4)) == sorted(expected4)
