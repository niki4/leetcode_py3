"""
You're given strings J representing the types of stones that are jewels, and S representing the stones you have.
Each character in S is a type of stone you have.
You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters.
Letters are case sensitive, so "a" is considered a different type of stone from "A".
"""


class Solution:
    """
    Time Complexity: O(J.length∗S.length))
    Space Complexity: O(1) additional space complexity in Python.
    """

    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum((stones.count(ltr) for ltr in jewels))


if __name__ == '__main__':
    solutions = [Solution()]
    tc = (
        ("aA", "aAAbbbb", 3),
        ("z", "ZZ", 0),
    )
    for s in solutions:
        for inp_jewels, inp_stones, exp in tc:
            assert s.numJewelsInStones(inp_jewels, inp_stones) == exp
