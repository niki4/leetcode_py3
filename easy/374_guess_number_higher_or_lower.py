"""
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns 3 possible results:

-1: The number I picked is lower than your guess (i.e. pick < num).
1: The number I picked is higher than your guess (i.e. pick > num).
0: The number I picked is equal to your guess (i.e. pick == num).
Return the number that I picked.
"""

guessed_num = 6


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:
def guess(num: int) -> int:
    """ own dummy implementation for tests, real implementation provided by LC """
    if num == guessed_num:
        return 0
    if num > guessed_num:
        return -1
    if num < guessed_num:
        return 1


class Solution:
    """
    Bruteforce solution. Expectedly got Time Limit Exception.
    Time complexity: O(n) as we need to verify n elements assuming each guess() call takes O(1)
    """

    def guessNumber(self, n: int) -> int:
        for i in range(1, n + 1):
            if guess(i) == 0:
                return i


class Solution2:
    """
    Binary search

    Runtime: 28 ms, faster than 73.45% of Python3
    Memory Usage: 14.2 MB, less than 52.62% of Python3

    Time complexity: O(log n)
    Space complexity: O(1)
    """

    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            mid = left + (right - left) // 2
            api_ans = guess(mid)
            if api_ans == 0:
                return mid
            elif api_ans == -1:
                right = mid - 1
            elif api_ans == 1:
                left = mid + 1


if __name__ == '__main__':
    solutions = [Solution(), Solution2()]
    for s in solutions:
        assert s.guessNumber(10) == guessed_num
