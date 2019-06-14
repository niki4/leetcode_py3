"""
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """
    Runtime: 72 ms, faster than 95.53% of Python3.
    Memory Usage: 24 MB, less than 21.89% of Python3.

    Runtime complexity: O(n). We have to visit all nodes.
    Memory complexity: O(n). We need additional storage for n values.
    """
    def isPalindrome(self, head: ListNode) -> bool:
        values = []

        while head is not None:
            values.append(head.val)
            head = head.next
        return values == values[::-1]


if __name__ == "__main__":
    s = Solution()
    ln1 = ListNode(1)
    ln2 = ListNode(2)
    ln1.next = ln2
    assert not s.isPalindrome(ln1)

    ln3 = ListNode(2)
    ln4 = ListNode(1)
    ln2.next = ln3
    ln3.next = ln4
    assert s.isPalindrome(ln1)
