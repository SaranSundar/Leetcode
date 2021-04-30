class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        values = set()
        self.preorder(root1, values)
        return self.preorder2(root2, values, target)

    def preorder(self, root: TreeNode, values: set):
        if root:
            values.add(root.val)
            self.preorder(root.left, values)
            self.preorder(root.right, values)

    def preorder2(self, root: TreeNode, values: set, target):
        if root:
            if (target - root.val) in values:
                return True
            return self.preorder2(root.left, values, target) or self.preorder2(root.right, values, target)
        return False
