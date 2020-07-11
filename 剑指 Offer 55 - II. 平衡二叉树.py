class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isBalanced(root: TreeNode) -> bool:
    def recur(root: TreeNode) -> int:
        if not root:
            return 0
        l = recur(root.left)
        if l == -1:
            return -1
        r = recur(root.right)
        if r == -1:
            return -1
        return max(l, r) + 1 if abs(l - r) < 2 else -1
    if recur(root) != -1:
        return True
    else:
        return False
