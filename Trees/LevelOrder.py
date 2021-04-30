from collections import deque
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        levels = []
        self.levelHelperRecursive(root, levels, 0)
        return levels

    def levelHelperIterative(self, root, levels, level):
        queue = deque([root])
        levels = []
        level = 0

        while queue:

            if len(levels) == level:
                levels.append([])

            level_length = len(queue)

            for i in range(level_length):
                node = queue.popleft()
                levels[level].append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            level += 1

    def levelHelperRecursive(self, node, levels, level):
        if node:
            # We are starting the level with an empty array
            if len(levels) == level:
                levels.append([])
            levels[level].append(node.val)
            self.levelHelperRecursive(node.left, levels, level + 1)
            self.levelHelperRecursive(node.right, levels, level + 1)
