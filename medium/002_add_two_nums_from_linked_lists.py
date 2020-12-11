"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

Runtime: 100 ms, faster than 92.55% of Python3 online submissions
Memory Usage: 12.7 MB, less than 1.00% of Python3 online submissions.
"""

__author__ = 'Ivan Nikiforov'


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    Bruteforce solution - traverse lists first to extract values, then create new list based on those values sum.

    Runtime: 76 ms, faster than 23.42% of Python3
    Memory Usage: 14.4 MB, less than 15.33% of Python3

    Time and Space complexity: O(n)
    """

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_nums = []
        l2_nums = []
        while l1:
            l1_nums.append(l1.val)
            l1 = l1.next
        while l2:
            l2_nums.append(l2.val)
            l2 = l2.next

        max_len = max(len(l1_nums), len(l2_nums))
        first_num = int("".join(str(n) for n in l1_nums[::-1]).zfill(max_len)) if l1_nums else 0
        second_num = int("".join(str(n) for n in l2_nums[::-1]).zfill(max_len)) if l2_nums else 0

        head = None
        prev = None
        for n in reversed(str(first_num + second_num)):
            if head is None:
                head = ListNode(n)
                prev = head
            else:
                new_node = ListNode(n)
                prev.next = new_node
                prev = new_node
        return head


class Solution2:
    """
    Runtime: 72 ms, faster than 49.91% of Python3
    Memory Usage: 14.3 MB, less than 15.33% of Python3
    """

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)  # dummy head
        current = head

        while l1 or l2:
            if current is None:
                break

            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            sum_ = v1 + v2 + current.val

            current.val = sum_ % 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            current.next = ListNode(sum_ // 10) if any([sum_ >= 10, l1, l2]) else None
            current = current.next

        return head


if __name__ == '__main__':
    sol = Solution()
    node_a_1 = ListNode(2)
    node_a_1.next = ListNode(4)
    node_a_2 = node_a_1.next
    node_a_2.next = ListNode(3)
    node_a_3 = node_a_2.next

    # print(node_a_1.val)             # 2
    # print(node_a_1.next.val)        # 4
    # print(node_a_1.next.next.val)   # 3

    node_b_1 = ListNode(5)
    node_b_1.next = ListNode(6)
    node_b_2 = node_b_1.next
    node_b_2.next = ListNode(4)
    node_b_3 = node_b_2.next

    # print(node_b_1.val)             # 5
    # print(node_b_1.next.val)        # 6
    # print(node_b_1.next.next.val)   # 4

    res = sol.addTwoNumbers(node_a_1, node_b_1)
    # print(res.val)                  # 7
    # print(res.next.val)             # 0
    # print(res.next.next.val)        # 8
