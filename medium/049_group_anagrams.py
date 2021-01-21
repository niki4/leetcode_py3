"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.

"""
from collections import defaultdict


class Solution:
    """
    Runtime: 112 ms, faster than 94.43% of Python3.
    Memory Usage: 16 MB, less than 68.05% of Python3.

    The algorithm uses a sorted string as key for hashmap ('aba'->'aab' and 'baa'->'aab')
    """

    def groupAnagrams(self, strs: list) -> list:
        groups = dict()
        for word in strs:
            sorted_s = ''.join(sorted(word))
            if sorted_s in groups:
                groups[sorted_s].append(word)
            else:
                groups[sorted_s] = [word]
        return [group for group in groups.values()]  # or simply return groups.values()


class Solution2:
    """
    Runtime: 116 ms, faster than 83.20% of Python3.
    Memory Usage: 15.9 MB, less than 75.97% of Python3.

    The algorithm uses the idea that sum of hashes of chars for anagram strings is the same,
    so that 'aba' -> hash1+hash2+hash1 = hash_result and 'aab' -> hash1+hash1+hash2 = hash_result,
    the sum is key for hashmap.
    """

    def groupAnagrams(self, strs: list) -> list:
        groups = dict()
        for word in strs:
            str_sum = sum(hash(ltr) for ltr in word)
            if str_sum in groups:
                groups[str_sum].append(word)
            else:
                groups[str_sum] = [word]
        return [group for group in groups.values()]


class Solution3:
    """
    Shorter version of two solutions listed above

    Runtime: 96 ms, faster than 74.73% of Python3
    Memory Usage: 17.9 MB, less than 48.25% of Python3

    Time Complexity: O(N*K logK), where N is the length of strs, and K is the maximum length of a string in strs.
      The outer loop has complexity O(N) as we iterate through each string.
      Then, we sort each string in O(K logK) time.
    Space Complexity: O(N*K), the total information content stored in ans.
    """

    def groupAnagrams(self, strs: list) -> list:
        dd = defaultdict(list)
        for word in strs:
            dd[tuple(sorted(word))].append(word)
        return list(dd.values())


if __name__ == "__main__":
    solutions = [Solution(), Solution2(), Solution3()]
    tc = (
        ([""], [[""]]),
        (["a"], [["a"]]),
        (["eat", "tea", "tan", "ate", "nat", "bat"], [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]),
        (["ddddddddddg", "dgggggggggg"], [["dgggggggggg"], ["ddddddddddg"]]),
    )
    for s in solutions:
        for inp, exp in tc:
            res = s.groupAnagrams(inp)
            assert sorted([sorted(x) for x in res]) == sorted([sorted(x) for x in exp]), \
                f'{s.__class__.__name__}:\n' \
                f'for inp:\t\t{inp}\n' \
                f'expected result: {sorted(exp)},\n' \
                f'got\t\t\t\t{sorted(res)}'
