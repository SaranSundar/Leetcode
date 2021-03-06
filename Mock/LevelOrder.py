# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        levels = []
        self.helper(root, levels, 0)
        return levels

    def helper(self, node, levels, level):
        if len(levels) == level:
            levels.append([])

        levels[level].append(node.val)
        if node.left:
            self.helper(node.left, levels, level + 1)
        if node.right:
            self.helper(node.right, levels, level + 1)
