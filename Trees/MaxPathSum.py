class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.max_sum = float('-inf')

    def maxPathSum(self, root: TreeNode) -> int:
        self.max_sum = float('-inf')
        self.max_gain(root)
        return self.max_sum

    def max_gain(self, root: TreeNode):
        if not root:
            return 0

        left = max(self.max_gain(root.left), 0)
        right = max(self.max_gain(root.right), 0)

        # A path can be a triangle
        price_newpath = root.val + left + right
        self.max_sum = max(self.max_sum, price_newpath)

        return root.val + max(left, right)
