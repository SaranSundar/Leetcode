# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root:
            return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
        else:
            return []

    def iterative(self, root: TreeNode) -> List[int]:
        stack, output = [], []
        while root or stack:
            # push nodes: right -> node -> left
            while root:
                if root.right:
                    stack.append(root.right)
                stack.append(root)
                root = root.left

            root = stack.pop()

            # if the right subtree is not yet processed
            if stack and root.right == stack[-1]:
                stack[-1] = root
                root = root.right
            # if we're on the leftmost leaf
            else:
                output.append(root.val)
                root = None

        return output
