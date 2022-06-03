"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:
Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

"""


class Solution:
    """
    Bruteforce solution. TLE.

    Time complexity: O(n**3)
    Space complexity: O(k) where k is the size for slice
    """

    def lengthOfLongestSubstring(self, s: str) -> int:
        max_substr = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if len(s[i:j]) == len(set(s[i:j])):  # no duplicates
                    max_substr = max(max_substr, len(s[i:j]))
        return max_substr


class Solution2:
    """
    Runtime: 948 ms, faster than 7.40% of Python3 online submissions.
    Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions.
    """

    def lengthOfLongestSubstring(self, s: 'str') -> 'int':
        word = str()
        max_word = int()

        len_s = len(s)
        if len_s <= 1:
            return len_s

        idx = 1
        while idx <= len(s) - 1:
            prev_ltr, curr_ltr = s[idx - 1], s[idx]

            if not word:
                word = prev_ltr

            if curr_ltr != prev_ltr:
                if curr_ltr not in word:
                    word += curr_ltr
                else:
                    dup_idx = word.index(curr_ltr) + 1

                    s = s[s.index(word) + dup_idx:]  # truncate left to exclude dup ltr in old word
                    if s:
                        idx = 0
                        word = s[idx]
            else:
                word = curr_ltr

            len_word = len(word)
            if len_word > max_word:
                max_word = len_word

            idx += 1

        return max_word


class Solution3:
    """
    Runtime:  476 ms, faster than 15.36% of Python3 online submissions.
    Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions.

    Using sliding window
    """

    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_sstr_len = 0
        visited = set()
        end = 0

        for i in range(len(s)):
            for j in range(i, len(s)):
                ltr = s[j]
                if ltr in visited:
                    visited.clear()
                    break
                end = j
                visited.add(ltr)
            longest_sstr_len = max(longest_sstr_len, len(s[i:end + 1]))

        return longest_sstr_len


class Solution3_1:
    """
    Greedy approach. More concise than previous ('Solution3') solution.

    Runtime: 780 ms, faster than 9.83% of Python3
    Memory Usage: 14.1 MB, less than 49.55% of Python3
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_substr = 0
        for i, ch in enumerate(s):
            seen = set([ch])
            for j in range(i+1, len(s)):
                if s[j] in seen:
                    break
                seen.add(s[j])
            max_substr = max(max_substr, len(seen))

        return max_substr


class Solution4:
    """
    Sliding window.
        Expand substr (right end) while there's no duplicates, evaluate max_substr on each iteration; then
        Shrink substr (left end) until no duplicates are left.

    Runtime: 84 ms, faster than 36.60% of Python3
    Memory Usage: 14.1 MB, less than 99.33% of Python3

    Time complexity:  O(2n) = O(n). In the worst case each character will be visited twice by i and j.
    Space complexity: O(min(m, n)). Same as the previous approach. We need O(k) space for the sliding window,
    where k is the size of the Set. The size of the Set is upper bounded by the size of the string n and the size
    of the charset/alphabet m.
    """

    def lengthOfLongestSubstring(self, s: str) -> int:
        max_substr = 0
        substr = set()
        i, j = 0, 0
        while i < len(s) and j < len(s):
            if s[j] not in substr:
                substr.add(s[j])
                max_substr = max(max_substr, len(substr))
                j += 1
            else:
                substr.remove(s[i])
                i += 1
        return max_substr


class Solution5:
    """
    Algorithm: The above solution requires at most 2n steps. In fact, it could be optimized to require only n steps.
    Instead of using a set to tell if a character exists or not, we could define a mapping of the characters to its idx.
    Then we can skip the characters immediately when we found a repeated character.

    The reason is that if s[j] have a duplicate in the range [i, j] with index j′, we don't need to increase i
    little by little. We can skip all the elements in the range [i, j′] and let i to be j′+1 directly.

    Runtime: 64 ms, faster than 69.06% of Python3
    Memory Usage: 14.5 MB, less than 27.15% of Python3

    Time complexity: O(n). Index j will iterate n times.
    Space complexity (HashMap): O(min(m, n)). Same as the previous approach.
    """

    def lengthOfLongestSubstring(self, s: str) -> int:
        max_substr = 0
        mp = dict()  # mp stores the current index of a character
        i = 0

        for j in range(len(s)):  # try to extend the range [i, j]
            if s[j] in mp:  # duplicate found
                i = max(mp[s[j]], i)
                # print(f"duplicate found {s[j]} -> i = max{(mp[s[j]], i)}:", i, "j:", j)
            max_substr = max(max_substr, j - i + 1)
            mp[s[j]] = j + 1
        return max_substr


if __name__ == '__main__':
    solutions = [
        Solution(),
        Solution2(),
        Solution3(),
        Solution4(),
        Solution5(),
    ]
    tc = (
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("aab", 2),
        ("dvdf", 3),
        ("anviaj", 5),
        ("tvqnkvovks", 5),
        ("", 0),
        (" ", 1),
        ("cekwrebvhvtlesh", 7),
        ("gsqygebs", 6),
        ("au", 2),
    )
    for sol in solutions:
        for inp, exp in tc:
            res = sol.lengthOfLongestSubstring(inp)
            assert res == exp, f'{sol.__class__.__name__}: for input {inp} result {res} != {exp}'
