"""
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a
dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.
https://en.wikipedia.org/wiki/Trie

Implement the Trie class:
    Trie()                              Initializes the trie object.
    void insert(String word)            Inserts the string word into the trie.
    boolean search(String word)         Returns true if the string word is in the trie (i.e., was inserted before),
                                        and false otherwise.
    boolean startsWith(String prefix)   Returns true if there is a previously inserted string word that has the prefix
                                        prefix, and false otherwise.
Example 1:
    Input
    ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
    [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
    Output
    [null, null, true, false, true, null, true]
Explanation
    Trie trie = new Trie();
    trie.insert("apple");
    trie.search("apple");   // return True
    trie.search("app");     // return False
    trie.startsWith("app"); // return True
    trie.insert("app");
    trie.search("app");     // return True

Constraints:
    1 <= word.length, prefix.length <= 2000
    word and prefix consist only of lowercase English letters.
    At most 3 * 104 calls in total will be made to insert, search, and startsWith.
"""


class TrieNode:
    def __init__(self, value):
        self.val = value
        self.edges = {}  # char_string: TrieNode
        self.is_word_end = False


class Trie:
    """
    Runtime: 292 ms, faster than 8.83% of Python3
    Memory Usage: 32.7 MB, less than 30.61% of Python3

    Time complexity: O(m), where m is the key length.
    Space complexity: O(m) for insert, O(1) for search
    """

    def __init__(self):
        self.root = TrieNode(None)

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self.root
        for char in word:
            if char not in curr.edges:
                curr.edges[char] = TrieNode(char)
            curr = curr.edges[char]
        curr.is_word_end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr = self.root
        for char in word:
            if char not in curr.edges:
                return False
            curr = curr.edges[char]
        return curr.is_word_end

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr = self.root
        for char in prefix:
            if char not in curr.edges:
                return False
            curr = curr.edges[char]
        return True


if __name__ == '__main__':
    trie = Trie()
    trie.insert("apple")
    assert trie.search("apple")
    assert trie.search("app") is False
    assert trie.startsWith("app")
    trie.insert("app")
    assert trie.search("app")
