"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list,
and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Runtime: 40 ms  (Your runtime beats 95.20 % of python3 submissions.)
Status: Accepted  (https://leetcode.com/submissions/detail/150407185/)
"""


class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        int_num = int(''.join(str(x) for x in digits)) + 1
        return [int(x) for x in str(int_num)]


if __name__ == '__main__':
    sol = Solution()
    print(sol.plusOne([1, 2, 3]))   # expected: [1, 2, 4]
    print(sol.plusOne([9]))         # expected: [1, 0]
    print(sol.plusOne([9, 9]))      # expected: [1, 0, 0]
