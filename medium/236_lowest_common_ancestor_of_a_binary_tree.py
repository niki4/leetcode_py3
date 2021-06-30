"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as
the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Constraints:
    The number of nodes in the tree is in the range [2, 105].
    -109 <= Node.val <= 109
    All Node.val are unique.
    p != q
    p and q will exist in the tree.

Example 1:
        2
      /   \
    1       3
if take p as 1 and q as 3, then lowest common ancestor will be node with val 2

Example 2:
            6
          /   \
        4      7
      /   \
    2      5
  /   \
1      3
If take p as 4 and q as 3, then lowest common ancestor will be node 4 (so this is the case when q inside p subtree)
"""
from tools.binary_tree import TreeNode


class Solution:
    """
    Recursive Approach

    Algorithm
        1. Start traversing the tree from the root node.
        2. If the current node itself is one of p or q, we would mark a variable mid as True and continue the search for
            the other node in the left and right branches.
        3. If either of the left or the right branch returns True, this means one of the two nodes was found below.
        4. If at any point in the traversal, any two of the three flags left, right or mid become True, this means we
            have found the lowest common ancestor for the nodes p and q.

    Runtime: 72 ms, faster than 69.48% of Python3
    Memory Usage: 27.8 MB, less than 22.75% of Python3

    Time Complexity: O(N), where N is the number of nodes in the binary tree.
    Space Complexity: O(N). This is because the maximum amount of space utilized by the recursion stack would be N
                    since the height of a skewed binary tree could be N.

    """

    def __init__(self):
        self.lca_node = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def recurse_tree(curr: TreeNode):
            # if reached end of the branch
            if not curr:
                return False

            left = recurse_tree(curr.left)
            right = recurse_tree(curr.right)

            # if the current node is either p or q
            mid = curr in (p, q)

            # if any two of three flags are left, right or mid become True
            if mid + left + right == 2:  # "True + True == 2" in Python
                self.lca_node = curr

            # return True if either of the three values are True
            return mid or left or right

        # traverse the tree
        recurse_tree(root)
        return self.lca_node


class Solution2:
    """
    Optimized first solution (the same idea)

    Runtime: 72 ms, faster than 69.48% of Python3
    Memory Usage: 25.4 MB, less than 48.34% of Python3

    Time / Space complexity: O(n) - the same reason as in first solution
    """

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if (left and right) or (root in (p, q)):
            return root
        return left or right


class Solution3:
    """
     Iterative using parent pointers (using backtracking to find LCA)

     Algorithm
        1. Start from the root node and traverse the tree.
        2. Until we find p and q both, keep storing the parent pointers in a dictionary.
        3. Once we have found both p and q, we get all the ancestors for p using the parent dictionary and add to a set
            called ancestors.
        4. Similarly, we traverse through ancestors for node q.
            If the ancestor is present in the ancestors set for p, this means this is the first ancestor common between
            p and q (while traversing upwards) and hence this is the LCA node.

     Runtime: 60 ms, faster than 98.38% of Python3
     Memory Usage: 18.2 MB, less than 90.56% of Python3

     Time / Space complexity: O(n)
    """

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = [root]  # stack for tree traversal
        parent = {root: None}  # dict for holding parent pointers
        ancestors = set()  # ancestors set for node p

        # iterate until we find both the nodes p and q
        while p not in parent and q not in parent:
            node = stack.pop()

            # while traversing the tree, keep saving the parent pointers
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)

        # process all ancestors for node p using parent pointers
        while p:
            ancestors.add(p)
            p = parent[p]

        # the first ancestor of q which appears in p's ancestor set
        # is their lowest common ancestor.
        while q not in ancestors:
            q = parent[q]
        return q
