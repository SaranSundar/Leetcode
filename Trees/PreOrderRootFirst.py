# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
Pre is root -> left -> right
In is left -> root -> right
post is left -> right -> root
level is bfs
"""
from collections import deque


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        traversal = []
        self.helper(root, traversal)
        return traversal

    def helper(self, root, traversal):
        if root:
            traversal.append(root.val)
            self.helper(root.left, traversal)
            self.helper(root.right, traversal)

    def iterative(self, root, traversal):
        if not root:
            return []
        stack = [root]
        while stack:
            node: TreeNode = stack.pop()
            traversal.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return traversal
