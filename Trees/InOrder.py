# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        traversal = []
        self.helper(root, traversal)
        return traversal

    def helper(self, root, traversal):
        if root:
            self.helper(root.left, traversal)
            traversal.append(root.val)
            self.helper(root.right, traversal)

    def iterative(self, root, traversal):
        current = root
        stack = []
        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            traversal.append(current.val)
            current = current.right
