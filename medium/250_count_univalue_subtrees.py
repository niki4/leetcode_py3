"""
Given the root of a binary tree, return the number of uni-value subtrees.
A uni-value subtree means all nodes of the subtree have the same value.

Example 1:
Input: root = [5,1,5,5,5,null,5]
Output: 4

Example 2:
Input: root = []
Output: 0

Example 3:
Input: root = [5,5,5,5,5,null,5]
Output: 6
"""
from problems.tools.binary_tree import TreeNode


class Solution:
    """
    The solution is based on one from @rohstar user:
    leetcode.com/problems/count-univalue-subtrees/discuss/465774/Recursive-Python-Solution-beats-99-Speed-100-Space

    The idea is that the following conditions result in the increment of the result counter:
        The node is a leaf (has no children)
        The node and it's children have the same value
        The node completes a tree recursively

    Failed on input [5,1,5,5,5,null,5,null,null,null,null,null,5]
    Output: 4, expected: 5
    """

    def __init__(self):
        self.count = 0

    def hasChildren(self, node):
        return node.left is not None or node.right is not None

    def isUniValueSubTree(self, node):
        if node is None:
            return
        if not self.hasChildren(node):  # leaf nodes are univalues by definition
            self.count += 1
            return

        self.isUniValueSubTree(node.left)

        if node.left and node.right:  # both children
            self.count += int(node.left.val == node.val == node.right.val)
        elif node.left:  # left child only
            self.count += int(node.left.val == node.val and not self.hasChildren(node.left))
        elif node.right:  # right child only
            self.count += int(node.right.val == node.val and not self.hasChildren(node.right))

        self.isUniValueSubTree(node.right)

    def countUnivalSubtrees(self, root: TreeNode) -> int:
        self.isUniValueSubTree(root)
        return self.count


class Solution2:
    """
    The solution is based on one from @alexxie17 user:
    leetcode.com/problems/count-univalue-subtrees/discuss/518646/Simple-Intuitive-python-solution

    Runtime: 36 ms, faster than 59.82% of Python3
    Memory Usage: 14.5 MB, less than 24.94% of Python3
    """

    def isUni(self, node: TreeNode, val) -> bool:
        # check if current subtree is uni-value subtree (all nodes downwards from current node has the same value)
        if not node:
            return True
        if node.val != val:
            return False
        if self.isUni(node.left, val) and self.isUni(node.right, val):
            return True
        return False

    def dfs(self, node: TreeNode) -> int:
        # recursively check all the nodes
        if not node:
            return 0
        count = 0
        val1 = self.dfs(node.left)
        if self.isUni(node, node.val):  # if there uni-value subtree from this node - add 1 to the result count
            count = 1
        val2 = self.dfs(node.right)
        return val1 + val2 + count

    def countUnivalSubtrees(self, root: TreeNode) -> int:
        return self.dfs(root)


class Solution3:
    """
    The solution is based on one from @gchen0119 user:
    leetcode.com/problems/count-univalue-subtrees/discuss/799990/Python-Iterative-Post-Order-Bottom-up-(with-comments)

    Runtime: 28 ms, faster than 94.63% of Python3
    Memory Usage: 14.4 MB, less than 48.27% of Python3
    """

    def countUnivalSubtrees(self, root):
        uni = {}  # the boolean dictionary to check if a subtree has uniform values
        stack = []
        counter = 0
        last = None
        while stack or root:
            if root:  # dfs left subtree
                stack.append(root)
                root = root.left
            else:
                root = stack[-1]
                # Keep backtracking if current node is a leaf or has a right child that has already been traversed (
                # bottom-up)
                if not root.right or root.right == last:
                    root = stack.pop()  # backtrack, i.e., go up the tree
                    left, right = uni.get(root.left), uni.get(root.right)  # get boolean condition for uniformity
                    if ((
                            left and right and root.left.val == root.right.val == root.val) or  # subtree with both children
                            (left is None and right and root.right.val == root.val) or  # subtree with only left child
                            (right is None and left and root.left.val == root.val) or  # subtree with only right child
                            (left is None and right is None)):  # at leaf node
                        counter += 1
                        uni[root] = True  # uniform
                    else:
                        uni[root] = False  # non-uniform, there are mixed child and root values
                    last = root  # keep track of right child for backtracking
                    root = None  # set root to None to backtrack right subtree
                # Otherwise traverse right child
                else:
                    root = root.right
        return counter


if __name__ == '__main__':
    def make_binary_tree():
        root = TreeNode(5)
        l1_1, l1_2 = TreeNode(1), TreeNode(5)
        l2_1, l2_2, l2_3 = TreeNode(5), TreeNode(5), TreeNode(5)
        root.left, root.right = l1_1, l1_2
        l1_1.left, l1_1.right, l1_2.right = l2_1, l2_2, l2_3
        return root


    solutions = [Solution, Solution2, Solution3]
    for s in solutions:
        res = s().countUnivalSubtrees(make_binary_tree())
        assert res == 4, f'expected {4}, got {res}'
