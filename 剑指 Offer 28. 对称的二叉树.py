class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isSymmetric(root: TreeNode) -> bool:
    if not root:
        return True

    def helper(l: TreeNode, r: TreeNode) -> bool:
        if not l and not r:
            return True
        elif l and r:
            return l.val == r.val and helper(l.left, r.right) and helper(l.right, r.left)
        return False

    return helper(root.left, root.right)