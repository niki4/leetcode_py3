"""
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or
vertically neighboring. The same letter cell may not be used more than once in a word.

Example 1:
Input: board = [
        ["o","a","a","n"],
        ["e","t","a","e"],
        ["i","h","k","r"],
        ["i","f","l","v"]],
      words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]

Example 2:
Input: board = [
        ["a","b"],
        ["c","d"]],
       words = ["abcb"]
Output: []

Constraints:
    m == board.length
    n == board[i].length
    1 <= m, n <= 12
    board[i][j] is a lowercase English letter.
    1 <= words.length <= 3 * 104
    1 <= words[i].length <= 10
    words[i] consists of lowercase English letters.
    All the strings of words are unique.
"""
from typing import List


class Solution:
    """
    Runtime: 260 ms, faster than 94.70% of Python3
    Memory Usage: 14.4 MB, less than 95.34% of Python3

    Time complexity: O(M(4*(3**(L−1))), where M is the number of cells in the board and L is the max length of words.
    Space Complexity: O(N), where N is the total number of letters in the dictionary.
    """

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        # build a prefix tree (trie) that shares common prefixes of words
        for word in words:
            node = trie
            for letter_ in word:
                # retrieve the next node; if not found - create an empty one
                node = node.setdefault(letter_, {})
            # mark the existence of word in the tree node (word end marker)
            node["$"] = word

        row_len, col_len = len(board), len(board[0])
        matched_words = []

        def backtracking(row: int, col: int, parent: trie):
            letter = board[row][col]
            curr_node = parent[letter]

            # check if we found a match of word
            word_match = curr_node.pop("$", False)
            if word_match:
                # also we removed the matched word to avoid duplicates,
                # as well as avoiding using set() fir results.
                matched_words.append(word_match)

            # Before exploration - mark cell as visited
            board[row][col] = "#"

            # DFS exploration
            for new_row, new_col in (row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1):
                if (0 <= new_row < row_len and
                        0 <= new_col < col_len and
                        board[new_row][new_col] in curr_node):
                    backtracking(new_row, new_col, curr_node)

            # After exploration - clear visited mark and restore letter (backtracking)
            board[row][col] = letter

            # Optimization: incrementally remove the matched leaf node in Trie
            if not curr_node:
                parent.pop(letter)

        for r in range(row_len):
            for c in range(col_len):
                if board[r][c] in trie:
                    backtracking(r, c, trie)

        return matched_words


if __name__ == '__main__':
    sol = Solution()
    tc = (([["o", "a", "a", "n"],
            ["e", "t", "a", "e"],
            ["i", "h", "k", "r"],
            ["i", "f", "l", "v"]], ["oath", "pea", "eat", "rain"], ["eat", "oath"]),
          ([["a", "b"],
            ["c", "d"]], ["abcb"], []),
          )
    for inp_board, inp_words, out_matches in tc:
        result = sol.findWords(inp_board, inp_words)
        assert sorted(result) == sorted(out_matches), f"{sorted(result)} != {sorted(out_matches)}"
