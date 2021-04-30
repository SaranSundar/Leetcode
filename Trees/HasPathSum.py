class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        return self.helper(root, targetSum)

    def helper(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False

        # Visit root, update target sum
        targetSum -= root.val

        # If at a root node, check if were down to 0
        if not root.left and not root.right:
            return targetSum == 0

        # Else recurse through tree and see if any path satisfies targetSum
        return self.helper(root.left, targetSum) or self.helper(root.right, targetSum)

    def iterative(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False

        stack = [(targetSum, root)]

        while stack:
            currentTarget, node = stack.pop()
            currentTarget -= node.val

            # We are at a root node, check if path sum is 0
            if node.right is None and node.left is None:
                if currentTarget == 0:
                    return True

            if node.right:
                stack.append((currentTarget, node.right))

            if node.left:
                stack.append((currentTarget, node.left))

        return False
