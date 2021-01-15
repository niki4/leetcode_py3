"""
Write a function that takes an unsigned integer and returns the number of '1' bits it has (aka the Hamming weight).

Example 1:
Input: n == 11 (base10) == 00000000000000000000000000001011 (base2)
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
"""


class Solution:
    """
    Python built-ins

    Runtime: 28 ms, faster than 84.15% of Python3
    Memory Usage: 14.2 MB, less than 36.90% of Python3
    """

    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1")


class Solution2:
    """
    Loop and Flip

    Algorithm: Check each of the 32 bits of the number. If the bit is 1, we add one to the number of 1-bits.
    We can check the i-th bit of a number using a bit mask.
    We start with a mask m=1, because the binary representation of 1 is 0000 0000 0000 0000 0000 0000 0000 0001.
    Clearly, a logical AND between any number and the mask 1 gives us the least significant bit of this number.
    To check the next bit, we shift the mask to the left by one: 0000 0000 0000 0000 0000 0000 0000 0010
    And so on.

    Runtime: 28 ms, faster than 84.15% of Python3
    Memory Usage: 14.3 MB, less than 5.86% of Python3

    Time complexity: Because n in this piece of code is a 32-bit integer, the time complexity is O(1).
    Space complexity: O(1), since no additional space is allocated.
    """

    def hammingWeight(self, n: int) -> int:
        bits = 0
        mask = 1
        for _ in range(32):
            if n & mask != 0:
                bits += 1
            mask <<= 1
        return bits


class Solution3:
    """
    Bit Manipulation Trick

    Algorithm: Optimize algorithm from Solution 2. Instead of checking every bit of the number,
    we repeatedly flip the least-significant 1-bit of the number to 0, and add 1 to the sum.
    As soon as the number becomes 0, we know that it does not have any more 1-bits, and we return the sum.
    The key idea here is to realize that for any number n, doing a bit-wise AND of n and n−1 flips the least-significant
     1-bit in n to 0. Why? Consider the binary representations of n and n−1.
    https://assets.leetcode.com/static_assets/media/original_images/191_Number_Of_Bits.png

    In the binary representation, the least significant 1-bit in nn always corresponds to a 0-bit in n−1.
    Therefore, anding the two numbers n and n−1 always flips the least significant 1-bit in n to 0,
    and keeps all other bits the same.

    Runtime: 28 ms, faster than 84.15% of Python3
    Memory Usage: 14.2 MB, less than 66.48% of Python3

    Time and Space complexity: O(1) the same as in solution 2
    """

    def hammingWeight(self, n: int) -> int:
        bits = 0
        while n != 0:
            bits += 1
            n &= (n - 1)
        return bits


if __name__ == '__main__':
    solutions = [Solution(), Solution2(), Solution3()]
    tc = (
        (11, 3),  # bin 00000000000000000000000000001011
        (128, 1),  # bin 00000000000000000000000010000000
        (4294967293, 31),  # bin 11111111111111111111111111111101
    )
    for s in solutions:
        for inp, exp in tc:
            assert s.hammingWeight(inp) == exp
