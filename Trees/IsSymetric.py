class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isMirror(root, root)

    def isMirror(self, root1: TreeNode, root2: TreeNode):
        # If both null return true
        if not root1 and not root2:
            return True

        # If only one null return false
        if not root1 or not root2:
            return False

        # If both have values check both sides of tree
        return root1.val == root2.val and self.isMirror(root1.right, root2.left) and self.isMirror(root1.left,
                                                                                                   root2.right)


solution = Solution()
print(solution.isSymmetric(None))
