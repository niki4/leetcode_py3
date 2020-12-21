"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that
 adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example: Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
"""
from problems.tools.binary_tree import TreeNode


class Solution:
    """
    Runtime: 44 ms, faster than 55.59% of Python3
    Memory Usage: 15.9 MB, less than 47.85% of Python3
    """

    def __init__(self):
        self.isPathFound = False
        self.targetSum = 0

    def isPathForTargetExist(self, node: TreeNode, prevSum: int):
        if node and not self.isPathFound:
            if (node.left is None and
                    node.right is None and
                    prevSum + node.val == self.targetSum):  # leaf
                self.isPathFound = True
            self.isPathForTargetExist(node.left, prevSum + node.val)
            self.isPathForTargetExist(node.right, prevSum + node.val)

    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        self.targetSum = sum
        self.isPathForTargetExist(root, 0)
        return self.isPathFound


class Solution2:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False

        node = root
        remain = sum
        remain -= node.val

        if node.left is None and node.right is None:  # leaf
            return remain == 0  # should be 0 if path found
        return self.hasPathSum(node.left, remain) or self.hasPathSum(node.right, remain)


if __name__ == '__main__':
    def make_binary_tree():
        root = TreeNode(5)
        l1_1, l1_2 = TreeNode(4), TreeNode(8)
        l2_1, l2_2, l2_3 = TreeNode(11), TreeNode(13), TreeNode(4)
        l3_1, l3_2, l3_3 = TreeNode(7), TreeNode(2), TreeNode(1)
        root.left, root.right = l1_1, l1_2
        l1_1.left, l1_2.left, l1_2.right = l2_1, l2_2, l2_3
        l2_1.left, l2_1.right, l2_3.right = l3_1, l3_2, l3_3
        return root


    target = 22
    solutions = [Solution, Solution2]
    for s in solutions:
        res = s().hasPathSum(make_binary_tree(), target)
        assert res is True, f'{s.__name__}: Expected true, got {res}'
