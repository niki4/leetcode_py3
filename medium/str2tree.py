"""
You need to construct a binary tree from a string consisting of parenthesis and integers.

The whole input represents a binary tree. It contains an integer followed by zero, one or two pairs of parenthesis.
The integer represents the root's value and a pair of parenthesis contains a child binary tree with the same structure.

You always start to construct the left child node of the parent first if it exists.

Example 1:
                      (4)
                    /     \
                  (2)     (6)
                 /  \     /
               (3)  (1)  (5)

    Input: s = "4(2(3)(1))(6(5))"
    Output: [4,2,6,3,1,5]

Example 2:
    Input: s = "4(2(3)(1))(6(5)(7))"
    Output: [4,2,6,3,1,5,7]

Example 3:
    Input: s = "-4(2(3)(1))(6(5)(7))"
    Output: [-4,2,6,3,1,5,7]

Constraints:
    0 <= s.length <= 3 * 104
    s consists of digits, '(', ')', and '-' only.
"""

from tools.binary_tree import TreeNode


class Solution:
    """
    Using stack to keep track of correct order of nodes.
    When bracket opening - we start new sequence and remember (push in stack) previous if it not closed yet.
    When bracket closing - we creating a node with the num seq if it exist or previous (unclosed) sequence. Then we link
                           that node with its parent (prev item in stack).

    Runtime: 88 ms, faster than 98.09% of Python3
    Memory Usage: 15.2 MB, less than 25.67% of Python3

    Time/Space complexity: O(n)
    """

    def str2tree(self, s: str) -> TreeNode:
        num, stack = "", []

        for ch in s:
            if ch.isdigit() or ch == "-":
                num += ch
            elif ch == "(":  # start seq
                if num:  # prev seq has not been closed, remember in stack
                    stack.append(TreeNode(num))
                    num = ""
            else:  # close seq
                node = TreeNode(num) if num else stack.pop()  # use curr num seq, if present, or prev (unclosed)
                if not stack[-1].left:  # always start from left child
                    stack[-1].left = node
                else:
                    stack[-1].right = node
                num = ""

        return stack[-1] if stack else TreeNode(num) if s else None
