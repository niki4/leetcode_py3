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


if __name__ == "__main__":
    s = Solution()
    s2 = Solution2()
    print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(s2.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
