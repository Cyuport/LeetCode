class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isBalanced(root: TreeNode) -> bool:
    if not root:
        return True
    def depth(root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + max(depth(root.left),depth(root.right))
    return abs(depth(root.left)-depth(root.right))<2 and isBalanced(root.left) and isBalanced(root.right)