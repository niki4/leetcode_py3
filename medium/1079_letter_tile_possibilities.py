"""
You have n  tiles, where each tile has one letter tiles[i] printed on it.

Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.

Example 1:
Input: tiles = "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".

Example 2:
Input: tiles = "AAABBC"
Output: 188

Example 3:
Input: tiles = "V"
Output: 1

Constraints:
    1 <= tiles.length <= 7
    tiles consists of uppercase English letters.
"""

import itertools


class Solution:
    """
    Lazy approach :-)
    Calculate and store all possible permutations from tiles[:1] to tiles[:len(titles)]

    Runtime: 72 ms, faster than 78.39% of Python3
    Memory Usage: 15.5 MB, less than 57.73% of Python3
    """

    def numTilePossibilities(self, tiles: str) -> int:
        possibilities = set()
        for i in range(1, len(tiles) + 1):
            possibilities.update("".join(perm) for perm in itertools.permutations(tiles, i))
        return len(possibilities)


if __name__ == '__main__':
    solutions = [Solution()]
    tc = (
        ("AAB", 8),
        ("AAABBC", 188),
        ("V", 1),
    )
    for sol in solutions:
        for inp_tiles, exp_num_possibilities in tc:
            result = sol.numTilePossibilities(inp_tiles)
            assert result == exp_num_possibilities, f"{sol.__class__.__name__}: {result} != {exp_num_possibilities}"
