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
from typing import List


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


class Solution4:
    """
    The same idea as Solution3, but using sorted string as a key

    Runtime: 88 ms, faster than 95.89% of Python3
    Memory Usage: 17.1 MB, less than 92.47% of Python3
    """

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            groups[key].append(s)
        return list(groups.values())


class Solution5:
    """
    We can transform each string s into a character count, count, consisting of 26 non-negative integers representing
    the number of a's, b's, c's, etc. We use these counts as the basis for our hash map.

    In python, the representation will be a tuple of the counts.
    For example, abbccc will be (1, 2, 3, 0, 0, ..., 0), where again there are 26 entries total.

    Runtime: 116 ms, faster than 32.55% of Python3
    Memory Usage: 19.8 MB, less than 9.81% of Python3

    Time and Space complexity: O(N*K)
    """

    def groupAnagrams(self, strs: list) -> list:
        ans = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return list(ans.values())


if __name__ == "__main__":
    solutions = [Solution(), Solution2(), Solution3(), Solution4(), Solution5()]
    tc = (
        ([""], [[""]]),
        (["a"], [["a"]]),
        (["eat", "tea", "tan", "ate", "nat", "bat"], [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]),
        (["ddddddddddg", "dgggggggggg"], [["dgggggggggg"], ["ddddddddddg"]]),
        (["ac", "c"], [["c"], ["ac"]]),
        (["ac", "d"], [["d"], ["ac"]]),
        (["cab", "tin", "pew", "duh", "may", "ill", "buy", "bar", "max", "doc"],
         [["doc"], ["bar"], ["buy"], ["ill"], ["tin"], ["cab"], ["pew"], ["may"], ["max"], ["duh"]]),
    )
    for s in solutions:
        for inp, exp in tc:
            res = s.groupAnagrams(inp)
            assert sorted([sorted(x) for x in res]) == sorted([sorted(x) for x in exp]), \
                f'{s.__class__.__name__}:\n' \
                f'for inp:\t\t{inp}\n' \
                f'expected result: {sorted(exp)},\n' \
                f'got\t\t\t\t{sorted(res)}'
