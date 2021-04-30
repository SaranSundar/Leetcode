class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.ans = None

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.helper(root, p, q)
        return self.ans

    def helper(self, root: TreeNode, p: TreeNode, q: TreeNode) -> bool:
        # If reached the end of a branch, return False.
        if not root:
            return False

        left = self.helper(root.left, p, q)
        right = self.helper(root.right, p, q)

        mid = root == p or root == q

        if mid + right + left >= 2:
            self.ans = root

        return mid or right or left
