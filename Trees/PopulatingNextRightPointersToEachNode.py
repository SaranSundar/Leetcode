class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    """"""

    # https: // leetcode.com / problems / populating - next - right - pointers - in -each - node - ii / solution /
    def connect(self, root: 'Node') -> 'Node':
        self.levelOrder(root, [], 0)
        return root

    def levelOrder(self, root: 'Node', levels, level):
        if not root:
            return

        if len(levels) == level:
            levels.append([])

        levels[level].append(root)

        self.levelOrder(root.left, levels, level + 1)
        self.levelOrder(root.right, levels, level + 1)

        for i in range(len(levels[level]) - 1):
            levels[level][i].next = levels[level][i + 1]
