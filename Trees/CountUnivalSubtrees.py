class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.count = 0

    """
    Time O(N) Space O(H) H being tee height
    """

    def countUnivalSubtrees(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.count = 0
        self.helper(root)
        return self.count

    def helper(self, root: TreeNode):
        # Node is a leaf node
        if not root.left and not root.right:
            # Every leaf node is a unival subtree so return true and increment count
            self.count += 1
            return True

        is_uni = True

        if root.left:
            is_uni = self.helper(root.left) and is_uni and root.val == root.left.val

        if root.right:
            is_uni = self.helper(root.right) and is_uni and root.val == root.right.val

        if is_uni:
            self.count += 1

        return is_uni
