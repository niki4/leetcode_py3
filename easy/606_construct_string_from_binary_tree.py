"""
Given the root of a binary tree, construct a string consists of parenthesis and integers from a binary tree with
the preorder traversing way, and return it.

Omit all the empty parenthesis pairs that do not affect the one-to-one mapping relationship between the string and the
original binary tree.

Example 1:
    Input: root = [1,2,3,4]
    Output: "1(2(4))(3)"
    Explanation: Originallay it needs to be "1(2(4)())(3()())", but you need to omit all the unnecessary empty
                 parenthesis pairs. And it will be "1(2(4))(3)"

Example 2:
    Input: root = [1,2,3,null,4]
    Output: "1(2()(4))(3)"
    Explanation: Almost the same as the first example, except we cannot omit the first parenthesis pair to break the
                 one-to-one mapping relationship between the input and the output.

Constraints:
    The number of nodes in the tree is in the range [1, 104].
    -1000 <= Node.val <= 1000
"""
from tools.binary_tree import TreeNode


class Solution:
    """
    Preorder DFS traversal

    String concatenation is expensive operation

    Runtime: 56 ms, faster than 33.51% of Python3
    Memory Usage: 16.2 MB, less than 63.09% of Python3
    """

    def tree2str(self, root: TreeNode) -> str:
        def dfs(node: TreeNode) -> str:
            if not node:
                return ""
            result = (str(node.val) +
                      ("()" if not node.left and node.right else dfs(node.left)) +
                      dfs(node.right))
            return "(" + result + ")" if node != root else result

        return dfs(root)


if __name__ == '__main__':
    solutions = [Solution()]

    bt1 = TreeNode(1)
    bt1.left, bt1.right = TreeNode(2), TreeNode(3)
    bt1.left.left = TreeNode(4)

    bt2 = TreeNode(1)
    bt2.left, bt2.right = TreeNode(2), TreeNode(3)
    bt2.left.right = TreeNode(4)

    tc = (
        (bt1, "1(2(4))(3)"),  # root = [1,2,3,4]
        (bt2, "1(2()(4))(3)"),  # root = [1,2,3,null,4]
    )
    for sol in solutions:
        for bt_root, expected_output in tc:
            actual_result = sol.tree2str(bt_root)
            assert actual_result == expected_output, f"{sol.__class__.__name__}: {actual_result} != {expected_output}"
