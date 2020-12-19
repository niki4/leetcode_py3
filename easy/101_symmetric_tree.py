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
    def __init__(self):
        self.levels = []

    def level_traversal(self, node: TreeNode, level: int):
        if node:
            if level == len(self.levels):
                self.levels.append([node.val])
            else:
                self.levels[level].append(node.val)

            if node.left:
                self.level_traversal(node.left, level + 1)
            else:
                if level + 1 == len(self.levels):
                    self.levels.append([None])
                else:
                    self.levels[level + 1].append(None)

            if node.right:
                self.level_traversal(node.right, level + 1)
            else:
                if level + 1 == len(self.levels):
                    self.levels.append([None])
                else:
                    self.levels[level + 1].append(None)

    def isSymmetric(self, root: TreeNode) -> bool:
        self.level_traversal(root, 0)
        print(self.levels)
        for level in self.levels:
            if level != level[::-1]:
                return False
        return True


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


    solutions = [Solution]
    for s in solutions:
        assert s().isSymmetric(make_symmetric_tree()) is True
        assert s().isSymmetric(make_asymmetric_tree()) is False
