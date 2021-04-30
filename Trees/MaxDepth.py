class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        maxValue = [0]
        self.helper(root, 1, maxValue)
        return maxValue[0]

    def helper(self, root, depth, maxValue):
        if root:
            maxValue[0] = max(depth, maxValue[0])
            self.helper(root.left, depth + 1, maxValue)
            self.helper(root.right, depth + 1, maxValue)
            # Could also just return both + 1

    def iterative(self, root) -> int:
        if not root:
            return 0
        stack = [(1, root)]
        height = 0

        while stack:
            depth, node = stack.pop()
            height = max(height, depth)
            if node.right:
                stack.append((depth + 1, node.right))
            if node.left:
                stack.append((depth + 1, node.left))

        return height
