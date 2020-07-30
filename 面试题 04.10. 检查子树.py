class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def checkSubTree(t1:TreeNode, t2: TreeNode) -> bool:
    if not t2:
        return True
    if not t1:
        return False
    if t1.val == t2.val:
        return checkSubTree(t1.left,t2.left) and checkSubTree(t1.right,t2.right)
    else:
        return checkSubTree(t1.left,t2) or checkSubTree(t1.right,t2)