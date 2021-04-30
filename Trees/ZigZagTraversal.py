from typing import List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        levels = []
        self.levelOrder(root, levels, 0)
        return levels

    def levelOrder(self, root, levels, level):
        if root:
            if len(levels) == level:
                levels.append(deque([]))

            if level % 2 == 0:
                levels[level].append(root.val)
            else:
                levels[level].appendleft(root.val)
            self.levelOrder(root.left, levels, level + 1)
            self.levelOrder(root.right, levels, level + 1)
