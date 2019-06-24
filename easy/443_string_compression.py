"""
Given an array of characters, compress it in-place.
The length after compression must always be smaller than or equal to the original array.

Every element of the array should be a character (not int) of length 1.
After you are done modifying the input array in-place, return the new length of the array.

Follow up:
Could you solve it using only O(1) extra space?

Example 1:
    Input:
    ["a","a","b","b","c","c","c"]
    Output:
    Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
    Explanation:
    "aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".
"""


class Solution:
    """
    Runtime: 48 ms, faster than 96.81% of Python3 online submissions for String Compression.
    Memory Usage: 13 MB, less than 97.58% of Python3 online submissions for String Compression.

    Time complexity: O(N+K), where N because we iterated over chars list only once and K is size
    of elements for .extend() operations
    Space complexity: O(N-K) we're using temporary list for results, where N is the size of original
    list and K is say compression factor (it could be 0 though).
    """
    def compress(self, chars: list) -> int:
        char_counts = []
        i = 0
        while i < len(chars):
            prev = chars[i]
            i += 1
            count = 1
            while i < len(chars) and prev == chars[i]:
                i += 1
                count += 1
            char_counts.extend([prev, *list(str(count))]) if count > 1 else char_counts.append(prev)

        chars.clear()
        chars.extend(char_counts)
        return len(chars)


class Solution2:
    """
    Runtime: 48 ms, faster than 96.81% of Python3.
    Memory Usage: 13.3 MB, less than 39.49% of Python3.

    Algorithm idea:
        Use 2 pointers - left and right, representing begin and end indexes of the sequence.
        Once found new char, use these left/right indexes to change source list in place, then
        move left index pointer onto new char, right pointer to left+1 and continue with next iteration.

    Time complexity: O(N)
    Space complexity: O(1)
    """
    def compress(self, chars: list) -> list:
        if len(chars) <= 1:
            return len(chars)

        left, right = 0, 1
        while right < len(chars):
            while right < len(chars) and chars[left] == chars[right]:
                right += 1
            count = right - left

            if count > 1:
                chars[left+1:right] = str(count)
                left += 2        # offset to hold prev value counters e.g., ['a', '3']
                right = left + 1
            elif count == 1:
                left += 1        # offset to hold prev value unchanged, e.g. ['a']
            right = left + 1
        return len(chars)


if __name__ == "__main__":
    s1 = Solution()
    s2 = Solution2()
    src1 = ["a","a","b","b","c","c","c"]
    src2 = ["a"]
    src3 = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    src4 = ["a","a","a","b","b","a","a"]

    assert s1.compress(src1) == len(src1) == 6
    assert src1 == ["a","2","b","2","c","3"]

    assert s1.compress(src2) == len(src2) == 1
    assert src2 == ["a"]

    assert s1.compress(src3) == len(src3) == 4
    assert src3 == ["a","b","1","2"]

    assert s1.compress(src4) == len(src4) == 6
    assert src4 == ["a","3","b","2","a","2"]

    src1 = ["a","a","b","b","c","c","c"]
    src2 = ["a"]
    src3 = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    src4 = ["a","a","a","b","b","a","a"]

    assert s2.compress(src1) == len(src1) == 6
    assert src1 == ["a","2","b","2","c","3"]

    assert s2.compress(src2) == len(src2) == 1
    assert src2 == ["a"]

    assert s2.compress(src3) == len(src3) == 4
    assert src3 == ["a","b","1","2"]

    assert s2.compress(src4) == len(src4) == 6
    assert src4 == ["a","3","b","2","a","2"]

    from timeit import Timer
    t1 = Timer('s1.compress(src1)', 'from __main__ import Solution, src1; s1 = Solution()')
    t2 = Timer('s2.compress(src1)', 'from __main__ import Solution2, src1; s2 = Solution2()')
    print('Solution1 time:', t1.timeit())
    print('Solution2 time:', t2.timeit())
