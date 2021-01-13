"""
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”.
For numbers which are multiples of both three and five output “FizzBuzz”.
"""


class Solution:
    """
    Runtime: 44 ms, faster than 43.86% of Python3 online submissions for Fizz Buzz.
    Memory Usage: 14.8 MB, less than 6.38% of Python3 online submissions for Fizz Buzz.

    def fizzBuzz(self, n: int) -> List[str]
    """

    def fizzBuzz(self, n):
        res = []
        for num in range(1, n + 1):
            if num % 3 == 0 and num % 5 == 0:
                res.append("FizzBuzz")
            elif num % 3 == 0:
                res.append("Fizz")
            elif num % 5 == 0:
                res.append("Buzz")
            else:
                res.append(str(num))
        return res


if __name__ == '__main__':
    sol = Solution()
    expected = [
        "1",
        "2",
        "Fizz",
        "4",
        "Buzz",
        "Fizz",
        "7",
        "8",
        "Fizz",
        "Buzz",
        "11",
        "Fizz",
        "13",
        "14",
        "FizzBuzz"
    ]
    assert sol.fizzBuzz(15) == expected
