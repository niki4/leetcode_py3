"""
Given two non-negative integers num1 and num2 represented as string,
return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or
convert the inputs to integer directly.
"""

class Solution:
    def addStrings_builtins(self, num1: str, num2: str) -> str:
        """
        Cheating :)

        Runtime: 52 ms, faster than 75.99% of Python3.
        Memory Usage: 13.3 MB, less than 40.91% of Python3.
        """
        return str(int(num1) + int(num2))

    def addStrings(self, num1: str, num2: str) -> str:
        """
        Runtime: 72 ms, faster than 20.34% of Python3.
        Memory Usage: 13.3 MB, less than 44.58% of Python3.
        """
        if len(num1) > len(num2):
            num2 = num2.zfill(len(num1))
        elif len(num1) < len(num2):
            num1 = num1.zfill(len(num2))

        high = int()
        res = str()
        for pair in list(zip(num1, num2))[::-1]:
            x, y = pair
            n1 = ord(x) - 48  # get num from unicode codepoint
            n2 = ord(y) - 48
            low = (n1 + n2) % 10
            res = str((high + low) % 10) + res
            high = (n1 + n2 + high) // 10

        if high:             #  if there any '10' (order) left
            res = str(high) + res

        return res

    def addStrings2(self, num1: str, num2: str) -> str:
        """
        Optimized version of the addStrings listed above

        Runtime: 48 ms, faster than 82.44% of Python3.
        Memory Usage: 13.2 MB, less than 68.90% of Python3.
        """
        max_len = max(len(num1), len(num2))
        num1 = num1.zfill(max_len)
        num2 = num2.zfill(max_len)

        high = int()
        res = str()
        for idx in range(max_len-1, -1, -1):
            x, y = num1[idx], num2[idx]
            n1 = ord(x) - 48
            n2 = ord(y) - 48
            low = (n1 + n2) % 10
            res = str((high + low) % 10) + res
            high = (n1 + n2 + high) // 10

        if high:
            res = str(high) + res

        return res


if __name__ == "__main__":
    s = Solution()
    assert s.addStrings_builtins("123", "321")  == "444"
    assert s.addStrings_builtins("0", "0") == "0"
    assert s.addStrings_builtins("9", "99") == "108"

    assert s.addStrings("123", "321")  == "444"
    assert s.addStrings("0", "0") == "0"
    assert s.addStrings("9", "99")  == "108"
    assert s.addStrings("1", "9")  == "10"
    assert s.addStrings("584", "18") == "602"

    assert s.addStrings2("123", "321")  == "444"
    assert s.addStrings2("0", "0") == "0"
    assert s.addStrings2("9", "99")  == "108"
    assert s.addStrings2("1", "9")  == "10"
    assert s.addStrings2("584", "18") == "602"
