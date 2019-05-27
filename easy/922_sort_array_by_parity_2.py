"""
Given an array A of non-negative integers,
half of the integers in A are odd,
and half of the integers are even.

Sort the array so that whenever A[i] is odd, i is odd;
and whenever A[i] is even, i is even.

You may return any answer array that satisfies this condition.

Example 1:
Input: [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.

Note:
2 <= A.length <= 20000
A.length % 2 == 0
0 <= A[i] <= 1000
"""

class Solution:
    """
    Runtime: 172 ms, faster than 17.25% of Python3.
    Memory Usage: 15.4 MB, less than 37.84% of Python3.
    """
    def sortArrayByParityII(self, A: list) -> list:
        result = []
        even_nums = filter(lambda n: n % 2 == 0, A)
        odd_nums = filter(lambda n: n % 2, A)

        for even, odd in zip(even_nums, odd_nums):
            result.extend([even, odd])
        return result

class Solution2:
    """
    Runtime: 128 ms, faster than 97.36% of Python3.
    Memory Usage: 15.4 MB, less than 42.72% of Python3.

    More concise and prettier (and faster!) solution than the one listed above
    using list slicing and generator expressions.
    """
    def sortArrayByParityII(self, A: list) -> list:
        result = [None] * len(A)
        result[::2] = (n for n in A if n % 2 == 0)
        result[1::2] = (n for n in A if n % 2)
        return result

class Solution3:
    """
    Runtime: 172 ms, faster than 17.25% of Python3.
    Memory Usage: 15.4 MB, less than 37.84% of Python3.

    Sort in-place.
    Time complexity: O(N)  |  Space complexity: O(1)
    """
    def sortArrayByParityII(self, A: list) -> list:
        j = 1
        for i in range(0, len(A), 2):
            if A[i] % 2:
                while A[j] % 2:          # skip all odd as they already on its place
                    j += 2
                A[i], A[j] = A[j], A[i]  # found even num, swap with odd
        return A

if __name__ == "__main__":
    s = Solution()
    s2 = Solution2()
    s3 = Solution3()
    for idx, val in enumerate(s.sortArrayByParityII([4,2,5,7])):
        assert idx % 2 == val % 2
    for idx, val in enumerate(s2.sortArrayByParityII([4,2,5,7])):
        assert idx % 2 == val % 2
    for idx, val in enumerate(s3.sortArrayByParityII([4,2,5,7])):
            assert idx % 2 == val % 2
