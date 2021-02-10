"""
The abbreviation of a word is a concatenation of its first letter, the number of characters between the first and last
letter, and its last letter. If a word has only two characters, then it is an abbreviation of itself.

For example:

dog --> d1g                     because there is one letter between the first letter 'd' and the last letter 'g'.
internationalization --> i18n   because there are 18 letters between the first letter 'i' and the last letter 'n'.
it --> it                       because any word with only two characters is an abbreviation of itself.

Implement the ValidWordAbbr class:
    ValidWordAbbr(String[] dictionary) Initializes the object with a dictionary of words.
    boolean isUnique(string word) Returns true if either of the following conditions are met (otherwise returns false):
        There is no word in dictionary whose abbreviation is equal to word's abbreviation.
        For any word in dictionary whose abbreviation is equal to word's abbreviation, that word and word are the same
"""

import collections
from typing import List


class ValidWordAbbr:
    """
    Runtime: 204 ms, faster than 93.35% of Python3
    Memory Usage: 27.6 MB, less than 45.84% of Python3

    Note: actually, pretty confusing description on LC. There's need to ensure that for given word that already been
    in our dictionary there are no words that share the same abbreviation (so the word is unique in term of its
    abbreviation). E.g., if dict has {"d2r": {"deer", "door"}, "c2e": {"cake"}} for word "deer" we'll return False
    because there are more than 1 value on "d2r" despite the value present; and True for word "cake" because one value.
    """

    def __init__(self, dictionary: List[str]):
        self.words = self.init_abbreviations(dictionary)

    def init_abbreviations(self, words: List[str]) -> collections.defaultdict[str, set]:
        res = collections.defaultdict(set)
        for word in words:
            abbr = self.abbreviate(word)
            res[abbr].add(word)
        return res

    def abbreviate(self, word: str) -> str:
        return f"{word[0]}{len(word) - 2}{word[-1]}" if len(word) > 2 else word

    def isUnique(self, word: str) -> bool:
        word_abbr = self.abbreviate(word)
        if word_abbr not in self.words:
            return True
        if word in self.words[word_abbr] and len(self.words[word_abbr]) == 1:
            return True
        return False


if __name__ == '__main__':
    case1 = ValidWordAbbr(["deer", "door", "cake", "card"])
    # dictionary word "deer" and word "dear" have the same abbreviation "d2r" but are not the same.
    assert case1.isUnique("dear") is False
    # no words in the dictionary have the abbreviation "c2t".
    assert case1.isUnique("cart")
    # dictionary word "cake" and word "cane" have the same abbreviation "c2e" but are not the same.
    assert case1.isUnique("cane") is False
    # no words in the dictionary have the abbreviation "m2e".
    assert case1.isUnique("make") is True
    # because "cake" is already in the dictionary and no other word in the dictionary has "c2e" abbreviation.
    assert case1.isUnique("cake") is True

    case2 = ValidWordAbbr(["deer", "door", "cake", "card"])  # d2r, c2e, c2d
    assert case2.isUnique("dear") is False
    assert case2.isUnique("door") is False
    assert case2.isUnique("cart")
    assert case2.isUnique("cake")

    case3 = ValidWordAbbr(["deer", "door", "cake", "card"])
    assert case3.isUnique("dear") is False
    assert case3.isUnique("cart")
    assert case3.isUnique("cane") is False
    assert case3.isUnique("make")
    assert case3.isUnique("cake")
