class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def inorderSuccessor(root: TreeNode, p: TreeNode) -> TreeNode:
    if not root:
        return None
    if p.val >= root.val:
        return inorderSuccessor(root.right,p)
    else:
        tmp = inorderSuccessor(root.left, p)
        if tmp:
            return tmp
        else:
            return root
