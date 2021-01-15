"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Given two integers x and y, calculate the Hamming distance (https://en.wikipedia.org/wiki/Hamming_distance).

Note:
0 ≤ x, y < 2**31.

Example:
Input: x = 1, y = 4
Output: 2
Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
The above arrows point to positions where the corresponding bits are different.
"""


class Solution:
    """
    Compare bits one-by-one. Calculate number of different bits.

    Runtime: 28 ms, faster than 83.52% of Python3
    Memory Usage: 14 MB, less than 90.44% of Python3
    Time complexity: O(1) since we know the range is constant (from terms 0 ≤ x, y < 2**31)
    Space complexity: O(1) as the size is finite too, but there's still extra memory for string repr of bin's.
    """

    def hammingDistance(self, x: int, y: int) -> int:
        diff = 0
        bin_x = format(x, "032b")  # makes bin repr without 0b and with leading zeroes up to len 32
        bin_y = format(y, "032b")
        for i in range(32):
            if bin_x[i] != bin_y[i]:
                diff += 1
        return diff


class Solution2:
    """
    Use XOR (logical OR) comparison for bits of two nums:
        Explanation:
    1   (0 0 0 1)
    4   (0 1 0 0)
    XOR (0 1 0 1)
           ↑   ↑  (2)

    Runtime: 28 ms, faster than 83.52% of Python3
    Memory Usage: 14.3 MB, less than 43.97% of Python3
    Time and Space complexity: O(1)
    """

    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count("1")


class Solution3:
    """
    Bit Shift

    In order to count the number of bit 1, we could shift each of the bit to either the leftmost or
    the rightmost position and then check if the bit is one or not.

    More precisely, we should do the logical shift where zeros are shifted in to replace the discarded bits.
    https://leetcode.com/problems/hamming-distance/Figures/461/461_shift.png

    Runtime: 28 ms, faster than 83.52% of Python3
    Memory Usage: 14 MB, less than 98.22% of Python3
    Time and Space complexity: O(1)
    """

    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        distance = 0
        while xor:  # mask out the rest bits
            if xor & 1:
                distance += 1
            xor >>= 1
        return distance


class Solution4:
    """
    Brian Kernighan's Algorithm:
    1. "If we is asked to count the bits of one, as humans, rather than mechanically examining each bit,
    we could _skip_ the bits of zero in between the bits of one, e.g. 10001000."

    In the above example, after encountering the first bit of one at the rightmost position,
    it would be more efficient if we just jump at the next bit of one, skipping all the zeros in between.

    2. "When we do AND bit operation between number and number-1,
    the rightmost bit of one in the original number would be cleared."
    https://leetcode.com/problems/hamming-distance/Figures/461/461_brian.png
    Based on the above idea, we then can count the bits of one for the input of 10001000 in 2 iterations, rather than 8.

    Runtime: 32 ms, faster than 57.35% of Python3
    Memory Usage: 14.3 MB, less than 12.45% of Python3
    Time and Space complexity: O(1)
    """

    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        distance = 0
        while xor:
            distance += 1
            xor &= (xor - 1)  # remove the rightmost bit of "1"
        return distance


if __name__ == '__main__':
    solutions = [Solution(), Solution2(), Solution3(), Solution4()]
    tc = (
        (1, 4, 2),
        (93, 73, 2),
    )
    for s in solutions:
        for in_x, in_y, exp in tc:
            dist = s.hammingDistance(in_x, in_y)
            assert dist == exp, f"{s.__class__.__name__}: for x={in_x} y={in_y} expected distance {exp}, got {dist}"
