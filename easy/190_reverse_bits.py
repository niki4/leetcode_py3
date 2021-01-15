"""
Reverse bits of a given 32 bits unsigned integer.

Example 1:

Input:  ->00000010100101000001111010011100
Output:   00111001011110000010100101000000<-
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
import functools


class Solution:
    # @param n, an integer with base10
    # @return an integer with base10
    def reverseBits(self, n: int) -> int:
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
    def reverseBits(self, n: int) -> int:
        """
        Runtime: 16 ms, faster than 91.35% of Python.
        Memory Usage: 11.7 MB, less than 71.91% of Python.

        Mask and Shift:
        "The idea can be considered as a strategy of divide and conquer, where we divide the original 32-bits into
        blocks with fewer bits via bit masking, then we reverse each block via bit shifting, and at the end we merge
        the result of each block to obtain the final result."

        As per Python documentation (https://wiki.python.org/moin/BitwiseOperators):
            1. 'x & y Does a "bitwise AND".
            Each bit of the output is 1 if the corresponding bit of x AND of y is 1, otherwise it's 0.'
            2. 'x << y Returns x with the bits shifted to the left by y places
            (and new bits on the right-hand-side are zeros). This is the same as multiplying x by 2**y.'
            3. 'x | y Does a "bitwise OR".
            Each bit of the output is 0 if the corresponding bit of x AND of y is 0, otherwise it's 1.'
        """
        n = ((n & 0x55555555) << 1) | ((n & 0xAAAAAAAA) >> 1)
        n = ((n & 0x33333333) << 2) | ((n & 0xCCCCCCCC) >> 2)
        n = ((n & 0x0F0F0F0F) << 4) | ((n & 0xF0F0F0F0) >> 4)
        n = ((n & 0x00FF00FF) << 8) | ((n & 0xFF00FF00) >> 8)
        n = ((n & 0x0000FFFF) << 16) | ((n & 0xFFFF0000) >> 16)
        return n


class Solution3:
    """
    The same idea as in first solution, but more readable code

    Runtime: 32 ms, faster than 70.60% of Python3
    Memory Usage: 14.3 MB, less than 36.96% of Python3
    """

    def reverseBits(self, n: int) -> int:
        return int(format(n, "032b")[::-1], 2)


class Solution4:
    """
    Bit by Bit

    Algorithm: The key idea is that for a bit that is situated at the index i,
    after the reversion, its position should be 31-i (note: the index starts from zero).
    * We iterate through the bit string of the input integer, from right to left (i.e. n = n >> 1).
      To retrieve the right-most bit of an integer, we apply the bit AND operation (n & 1).
    * For each bit, we reverse it to the correct position (i.e. (n & 1) << power).
      Then we accumulate this reversed bit to the final result.
    * When there is no more bits of one left (i.e. n == 0), we terminate the iteration.
    https://leetcode.com/problems/reverse-bits/Figures/190/190_reverse_bits.png

    Runtime: 32 ms, faster than 70.60% of Python3
    Memory Usage: 13.9 MB, less than 98.13% of Python3
    """

    def reverseBits(self, n: int) -> int:
        ret, power = 0, 31
        while n:
            ret += (n & 1) << power
            n >>= 1
            power -= 1
        return ret


class Solution5:
    """
    Byte by Byte with Memoization

    * The idea is to reverse by bytes (block of bits of size 8) instead bits.
    https://leetcode.com/problems/reverse-bits/Figures/190/190_reverse_bytes.png
    * Another implicit advantage of using byte as the unit of iteration is that we could apply the technique
    of memoization, which caches the previously calculated values to avoid the re-calculation.
    * The algorithm is documented as "reverse the bits in a byte with 3 operations" on the online book called
    Bit Twiddling Hacks by Sean Eron Anderson, where one can find more details.
    http://graphics.stanford.edu/~seander/bithacks.html#ReverseByteWith64BitsDiv

    Runtime: 32 ms, faster than 70.60% of Python3
    Memory Usage: 14.3 MB, less than 7.24% of Python3
    """

    @functools.lru_cache(maxsize=256)  # for memoization
    def reverseByte(self, byte):
        return (byte * 0x0202020202 & 0x010884422010) % 1023

    def reverseBits(self, n: int) -> int:
        ret, power = 0, 24
        while n:
            ret += self.reverseByte(n & 0xff) << power
            n >>= 8
            power -= 8
        return ret


if __name__ == "__main__":
    solutions = [Solution(), Solution2(), Solution3(), Solution4(), Solution5()]
    tc = (
        (43261596, 964176192),
        (4294967293, 3221225471),
    )
    for s in solutions:
        for inp, exp in tc:
            assert s.reverseBits(inp) == exp
