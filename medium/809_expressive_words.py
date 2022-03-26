"""
Sometimes people repeat letters to represent extra feeling. For example:

"hello" -> "heeellooo"
"hi" -> "hiiii"
In these strings like "heeellooo", we have groups of adjacent letters that are all the same: "h", "eee", "ll", "ooo".

You are given a string s and an array of query strings words. A query word is stretchy if it can be made to be equal
to s by any number of applications of the following extension operation: choose a group consisting of characters c,
and add some number of characters c to the group so that the size of the group is three or more.

For example, starting with "hello", we could do an extension on the group "o" to get "hellooo", but we cannot get
"helloo" since the group "oo" has a size less than three. Also, we could do another extension like "ll" -> "lllll"
to get "helllllooo". If s = "helllllooo", then the query word "hello" would be stretchy because of these two extension
operations: query = "hello" -> "hellooo" -> "helllllooo" = s.
Return the number of query strings that are stretchy.

Example 1:
Input: s = "heeellooo", words = ["hello", "hi", "helo"]
Output: 1
Explanation:
    We can extend "e" and "o" in the word "hello" to get "heeellooo".
    We can't extend "helo" to get "heeellooo" because the group "ll" is not size 3 or more.
    Example 2:

Input: s = "zzzzzyyyyy", words = ["zzyy","zy","zyy"]
Output: 3

Constraints:
    1 <= s.length, words.length <= 100
    1 <= words[i].length <= 100
    s and words[i] consist of lowercase letters.
"""


from typing import List


class Solution:
    def find_adjacent_groups(self, s: str) -> List[List[any]]:
        s_counts = [
            [s[0], 1]
        ]
        for i in range(1, len(s)):
            # calc groups of adjacent letters
            if s_counts[-1][0] == s[i]:
                s_counts[-1][1] += 1
            else:
                s_counts.append([s[i], 1])
        return s_counts

    def expressiveWords(self, s: str, words: List[str]) -> int:
        target_s_groups = self.find_adjacent_groups(s)
        strechy_queries = 0

        for word in words:
            word_s_groups = self.find_adjacent_groups(word)
            candidate_word = False
            if len(target_s_groups) == len(word_s_groups):
                for i in range(len(target_s_groups)):
                    s_group_char = target_s_groups[i][0]
                    s_group_size = target_s_groups[i][1]
                    if s_group_char != word_s_groups[i][0]:  # makes no sense to test other groups
                        candidate_word = False
                        break
                    if s_group_size != word_s_groups[i][1] and s_group_size < 3:
                        # can't form target group, e.g. 'l' -> 'll'
                        candidate_word = False
                        break
                    if s_group_size < word_s_groups[i][1]:  # e.g., 'llll' cannot downgrade to 'lll'
                        candidate_word = False
                        break
                    if s_group_size < 3:  # check only groups len 3 or more
                        continue
                    if (s_group_size - word_s_groups[i][1]) > 0:
                        candidate_word = True
                if candidate_word:
                    strechy_queries += 1

        return strechy_queries


if __name__ == '__main__':
    solutions = [
        Solution(),
        ]
    tc = (
        ("heeellooo", ["hello", "hi", "helo"], 1),
        ("zzzzzyyyyy", ["zzyy","zy","zyy"], 3),
        ("heeelllooo", ["hellllo"], 0),
    )
    for solution in solutions:
        for inp_s, inp_words, exp_count in tc:
            assert solution.expressiveWords(inp_s, inp_words) == exp_count
