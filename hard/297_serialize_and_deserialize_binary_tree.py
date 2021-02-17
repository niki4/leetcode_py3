"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored
in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or
another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your
serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a
string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily
need to follow this format, so please be creative and come up with different approaches yourself.

Example 1:
        1
     /    \
    2       3
          /   \
        4       5
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

Example 4:
Input: root = [1,2]
Output: [1,2]
"""
import collections

from problems.tools.binary_tree import TreeNode


class Codec:
    """
    BFS (breadth-first search) approach so that we traverse tree / values level by level

    Time / Space complexity: O(n) for both serialize and deserialize operations

    Runtime: 104 ms, faster than 96.15% of Python3
    Memory Usage: 18.8 MB, less than 57.76% of Python3
    """

    def serialize(self, root: TreeNode) -> str:
        """ Encodes a binary tree to a single string. """
        q, result = collections.deque([root]), []
        while q:
            node = q.popleft()
            if node:
                result.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                result.append("#")  # placeholder for None
        return " ".join(result)

    def deserialize(self, data: str) -> TreeNode or None:
        """ Decodes your encoded data to binary tree. """
        if data[0] == "#":
            return

        vals = iter(data.split())  # make list iterator to request one item at a time
        root = TreeNode(int(next(vals)))
        q = collections.deque([root])

        while q:
            node = q.popleft()
            left, right = next(vals), next(vals)
            node.left = TreeNode(int(left)) if left != "#" else None
            node.right = TreeNode(int(right)) if right != "#" else None
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return root
