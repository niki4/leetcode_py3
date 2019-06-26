"""
Reverse bits of a given 32 bits unsigned integer.

Example 1:

Input:  00000010100101000001111010011100
Output: 00111001011110000010100101000000
Explanation:
The input binary string 00000010100101000001111010011100 represents
the unsigned integer 43261596, so return 964176192 which its binary
representation is 00111001011110000010100101000000.

Example 2:
Input:  11111111111111111111111111111101
Output: 10111111111111111111111111111111
Explanation:
The input binary string 11111111111111111111111111111101 represents
the unsigned integer 4294967293, so return 3221225471 which its binary
representation is 10101111110010110010011101101001.
"""

class Solution:
    # @param n, an integer with base10
    # @return an integer with base10
    def reverseBits(self, n):
        """
        Runtime: 12 ms, faster than 97.09% of Python.
        Memory Usage: 11.9 MB, less than 7.77% of Python.

        {:08b} returns binary representation of int, without 0b prefix.
        zfill(32) appends 0s to begin of binary string so it always has len 32.
        [::-1] reverses string.
        int(x, 2) creates integer num from string representation of binary num
        """
        return int('{:08b}'.format(n).zfill(32)[::-1], 2)


class Solution2:
    def reverseBits(self, n):
        """
        Runtime: 16 ms, faster than 91.35% of Python.
        Memory Usage: 11.7 MB, less than 71.91% of Python.

        OMG, what's going on here?

        As per Python documentation (https://wiki.python.org/moin/BitwiseOperators):
            1. 'x & y Does a "bitwise AND".
            Each bit of the output is 1 if the corresponding bit of x AND of y is 1, otherwise it's 0.'
            2. 'x << y Returns x with the bits shifted to the left by y places
            (and new bits on the right-hand-side are zeros). This is the same as multiplying x by 2**y.'
            3. 'x | y Does a "bitwise OR".
            Each bit of the output is 0 if the corresponding bit of x AND of y is 0, otherwise it's 1.'
        """
        n = ((n & 0x55555555) << 1) | ((n& 0xAAAAAAAA) >> 1)
        n = ((n & 0x33333333) << 2) | ((n& 0xCCCCCCCC) >> 2)
        n = ((n & 0x0F0F0F0F) << 4) | ((n& 0xF0F0F0F0) >> 4)
        n = ((n & 0x00FF00FF) << 8) | ((n& 0xFF00FF00) >> 8)
        n = ((n & 0x0000FFFF) << 16) | ((n & 0xFFFF0000) >> 16)
        return n


if __name__ == "__main__":
    s = Solution()
    s2 = Solution2()
    s.reverseBits(43261596) == 964176192
    s.reverseBits(4294967293) == 3221225471
    s2.reverseBits(43261596) == 964176192
    s2.reverseBits(4294967293) == 3221225471
