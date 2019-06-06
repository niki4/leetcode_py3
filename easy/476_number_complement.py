"""
Given a positive integer, output its complement number.
The complement strategy is to flip the bits of its binary representation.

Note:
The given integer is guaranteed to fit within the range of a 32-bit signed integer.
You could assume no leading zero bit in the integer’s binary representation.

Example 1:
    Input: 5
    Output: 2
    Explanation: The binary representation of 5 is 101 (no leading zero bits),
    and its complement is 010. So you need to output 2.

Example 2:
    Input: 1
    Output: 0
    Explanation: The binary representation of 1 is 1 (no leading zero bits),
    and its complement is 0. So you need to output 0.
"""

class Solution:
    """
    Runtime: 28 ms, faster than 97.94% of Python3.
    Memory Usage: 13.1 MB, less than 58.82% of Python3.

    Naive implementation. Surprisingly fast.
    """
    def findComplement(self, num: int) -> int:
        bin_num = bin(num)[2:]
        res = ''
        for bit in bin_num:
            res += str('0') if bit == '1' else str('1')
        return int(res, 2)


class Solution2:
    """
    Runtime: 24 ms, faster than 99.79% of Python3.
    Memory Usage: 13.2 MB, less than 31.95% of Python3.

    ^ operator does a "bitwise exclusive or". So having 111 as a mask, 111 ^ 101 = 010
    """
    def findComplement(self, num: int) -> int:
        mask = 1 << len(bin(num)[2:])
        return (mask - 1) ^ num


if __name__ == "__main__":
    s = Solution()
    s2 = Solution2()
    assert s.findComplement(5) == 2
    assert s.findComplement(1) == 0
    assert s2.findComplement(5) == 2
    assert s2.findComplement(1) == 0
