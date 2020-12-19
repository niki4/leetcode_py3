"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3


But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3

"""
from problems.tools.binary_tree import TreeNode


class Solution:
    """
    Top-down approach.
    Pass level info to the next recursive call. Mark non-existing child node with None.

    Runtime: 32 ms, faster than 80.10% of Python3
    Memory Usage: 14.5 MB, less than 5.78% of Python3
    """

    def __init__(self):
        self.levels = []

    def level_traversal(self, node: TreeNode, level: int):
        if level == len(self.levels):
            self.levels.append([])

        if node:
            self.levels[level].append(node.val)
            self.level_traversal(node.left, level + 1)
            self.level_traversal(node.right, level + 1)
        else:
            self.levels[level].append(None)

    def isSymmetric(self, root: TreeNode) -> bool:
        self.level_traversal(root, 0)
        for level in self.levels:
            if level != level[::-1]:
                return False
        return True


class Solution2:
    """
    Algorithm idea: recursively go down the tree verifying mirrored nodes. If recursion ends on tree1=tree2=None then
    we have symmetric tree, otherwise its asymmetric.

    Runtime: 28 ms, faster than 93.71% of Python3
    Memory Usage: 14.6 MB, less than 5.78% of Python3
    """

    def _is_mirror(self, tree1: TreeNode, tree2: TreeNode) -> bool:
        if tree1 is None or tree2 is None:
            return tree1 == tree2
        if tree1.val != tree2.val:
            return False
        return (self._is_mirror(tree1.left, tree2.right) and
                self._is_mirror(tree1.right, tree2.left))

    def isSymmetric(self, root: TreeNode) -> bool:
        return self._is_mirror(root.left, root.right) if root else True


if __name__ == '__main__':
    def make_symmetric_tree():
        root = TreeNode(1)
        l2_l, l2_r = TreeNode(2), TreeNode(2)
        l2_l_l3_l, l2_l_l3_r, l2_r_l3_l, l2_r_l3_r = TreeNode(3), TreeNode(4), TreeNode(4), TreeNode(3)
        root.left, root.right = l2_l, l2_r
        l2_l.left, l2_l.right, l2_r.left, l2_r.right = l2_l_l3_l, l2_l_l3_r, l2_r_l3_l, l2_r_l3_r
        return root


    def make_asymmetric_tree():
        root = TreeNode(1)
        l2_l, l2_r = TreeNode(2), TreeNode(2)
        l2_l_l3_l, l2_l_l3_r, l2_r_l3_l, l2_r_l3_r = None, TreeNode(3), None, TreeNode(3)
        root.left, root.right = l2_l, l2_r
        l2_l.left, l2_l.right, l2_r.left, l2_r.right = l2_l_l3_l, l2_l_l3_r, l2_r_l3_l, l2_r_l3_r
        return root


    solutions = [Solution, Solution2]
    for s in solutions:
        assert s().isSymmetric(make_symmetric_tree()) is True
        assert s().isSymmetric(None) is True
        assert s().isSymmetric(make_asymmetric_tree()) is False
