from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: TreeNode, target: int) -> bool:
        traversal = self.preorder(root)
        map = set()
        for i in range(len(traversal)):

            if target - traversal[i] in map:
                return True

            if traversal[i] not in map:
                map.add(traversal[i])

        return False

    def preorder(self, root: TreeNode):
        if not root:
            return []
        return [root.val] + self.preorder(root.left) + self.preorder(root.right)
