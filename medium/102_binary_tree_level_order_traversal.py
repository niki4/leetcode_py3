"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Recursive approach

    Runtime: 28 ms, faster than 94.32% of Python3
    Memory Usage: 14.9 MB, less than 13.88% of Python3
    """

    def __init__(self):
        self.result = []

    def _levelHelper(self, node: TreeNode, level: int):
        if node:
            if len(self.result) - 1 < level:
                self.result.append([node.val])
            else:
                self.result[level].append(node.val)
            self._levelHelper(node.left, level + 1)
            self._levelHelper(node.right, level + 1)

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        self._levelHelper(root, 0)
        return self.result


class Solution2:
    """
    Iterative approach
    Use mix of Preorder BFS (take root, explore left subtree, explore right subtree) with level tracking.

    Runtime: 32 ms, faster than 80.36% of Python3
    Memory Usage: 14.6 MB, less than 44.37% of Python3
    """

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        stack, result = [(root, 0)], []
        while stack:
            node, level = stack.pop()
            if level == len(result):
                result.append([node.val])
            else:
                result[level].append(node.val)

            if node.right:
                stack.append((node.right, level + 1))
            if node.left:
                stack.append((node.left, level + 1))
        return result


if __name__ == '__main__':
    rootN = TreeNode(3)
    l1_l = TreeNode(9)
    l1_r = TreeNode(20)
    l2_l = TreeNode(15)
    l2_r = TreeNode(7)
    rootN.left, rootN.right = l1_l, l1_r
    l1_r.left, l1_r.right = l2_l, l2_r
    expected = [
        [3],
        [9, 20],
        [15, 7]
    ]
    solutions = [Solution(), Solution2()]
    for s in solutions:
        res = s.levelOrder(rootN)
        assert len(res) == len(expected), f'Num of levels: want {len(expected)}, got {len(res)}'
        for i in range(len(res)):
            assert res[i] == expected[i], f'At level {i} expected {expected[i]}, got {res[i]}'
